import gnupg
import logging

class Decrypt:
    '''
    A class for message decryption. \n
    Constructor takes user passphrase to unlock private key.\n
    Attributes:
        gpg -- a Gnu PG instance essential for accessing gpg binary.
    '''
    def __init__(self, user_passphrase):
        self.gpg = gnupg.GPG(gnupghome='./.gnupg')
        self.user_passphrase = user_passphrase

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
 
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        ch.setFormatter(formatter)

        if (self.logger.hasHandlers()):
            self.logger.handlers.clear()

        self.logger.addHandler(ch)

    def decrypt_string(self, string):
        '''
        Decrypt the received string using user's private key.
        '''
        try:
            decrypted = self.gpg.decrypt(string, passphrase=self.user_passphrase)
            return str(decrypted)
        except Exception as e:
            self.logger.error(f'{e} -- Unable to decrypt the provided string.')