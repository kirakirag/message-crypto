import unittest

from pki import Decrypt, Encrypt

encryption = Encrypt.Encrypt()
decryption = Decrypt.Decrypt('12345')

class EncryptTest(unittest.TestCase):
    def test_simple_string(self):
        self.assertEqual(decryption.decrypt_string(encryption.encrypt_string('4FC94BFCCB82491E', 'abc')), 'abc')
    
    def test_long_string(self):
        self.assertEqual(decryption.decrypt_string(encryption.encrypt_string('4FC94BFCCB82491E', 'abc'*100)), 'abc'*100)
    
    def test_string_with_numbers(self):
        self.assertEqual(decryption.decrypt_string(encryption.encrypt_string('4FC94BFCCB82491E', 'a8890012bacsdas9882131823--0--0')), 'a8890012bacsdas9882131823--0--0')

    def test_nonexistent_keyid(self):
        self.assertFalse(decryption.decrypt_string(encryption.encrypt_string('1', 'a8890012bacsdas9882131823--0--0')), 'a8890012bacsdas9882131823--0--0')
        
if __name__ == "__main__":
    unittest.main()