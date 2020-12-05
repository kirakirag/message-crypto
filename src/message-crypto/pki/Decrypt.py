import gnupg
from pki.KeyManager import KeyManager

class Decrypt:
    def __init__(self, user_passphrase):
        self.gpg = gnupg.GPG(gnupghome='./.gnupg')
        self.key_manager = KeyManager()
        self.user_passphrase = user_passphrase

    def decrypt_string(self, string):
        '''
        this method decrypts the recieved string using user's private key
        '''
        try:
            decrypted = self.gpg.decrypt(string, passphrase=self.user_passphrase)
            return str(decrypted)
        except Exception as e:
            print(e)