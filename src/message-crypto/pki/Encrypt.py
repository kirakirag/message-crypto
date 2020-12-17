import gnupg
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ch.setFormatter(formatter)

logger.addHandler(ch)

class Encrypt:
    '''
    A class for message encryption.
    '''
    def __init__(self):
        self.gpg = gnupg.GPG(gnupghome='./.gnupg')
    
    def encrypt_string(self, string, recipient):
        '''
        This method encrypts the received string with recipient's public key.
        '''
        try:
            encrypted = self.gpg.encrypt(string, recipients=recipient, armor=True)
            if not encrypted:
                raise Exception('Something went wrong')
            return str(encrypted)
        except Exception as e:
            logger.error(f'{e} -- Unable to encrypt the provided string.')

        
