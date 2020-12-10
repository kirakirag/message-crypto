import gnupg
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ch.setFormatter(formatter)

logger.addHandler(ch)

class Decrypt:
    '''
    A class for message decryption.
    '''
    def __init__(self, user_passphrase):
        self.gpg = gnupg.GPG(gnupghome='./.gnupg')
        self.user_passphrase = user_passphrase

    def decrypt_string(self, string):
        '''
        Decrypt the received string using user's private key.
        '''
        try:
            decrypted = self.gpg.decrypt(string, passphrase=self.user_passphrase)
            return str(decrypted)
        except Exception as e:
            logger.error(f'{e} -- Unable to decrypt the provided string.')