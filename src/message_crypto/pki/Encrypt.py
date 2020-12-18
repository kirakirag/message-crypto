import gnupg
import logging

class Encrypt:
    '''
    A class for message encryption.

    Attributes:
        gpg -- a Gnu PG instance essential for accessing gpg binary.
    '''
    def __init__(self):
        self.gpg = gnupg.GPG(gnupghome='./.gnupg')
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
 
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        ch.setFormatter(formatter)

        if (self.logger.hasHandlers()):
            self.logger.handlers.clear()

        self.logger.addHandler(ch)
    
    def encrypt_string(self, recipient, string):
        '''
        Encrypt the received string with recipient's public key.
        If encryption is unsuccessful, raises RuntimeError.
        '''
        try:
            encrypted = self.gpg.encrypt(string, recipient)
            if not encrypted.ok:
                raise RuntimeError(encrypted.status)
            return str(encrypted)
        except Exception as e:
            self.logger.error(f'{e} -- Unable to encrypt the provided string.')
