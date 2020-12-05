import gnupg
from pki.KeyManager import KeyManager

class Encrypt:
    '''
    Docs go here
    '''
    def __init__(self):
        self.gpg = gnupg.GPG(gnupghome='./.gnupg')
        self.key_manager = KeyManager()
    
    def encrypt_string(self, recipient, string):
        '''
        this method encrypts the recieved string with recipient's public key
        '''
        try:
            encrypted = self.gpg.encrypt(string, recipient)
            return str(encrypted)
        except Exception as e:
            print(e)

        
