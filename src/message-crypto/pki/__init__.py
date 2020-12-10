import os
from fs import open_fs
import gnupg
import logging
import KeyManager, Encrypt, Decrypt 

home_fs = open_fs('.')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ch.setFormatter(formatter)

logger.addHandler(ch)

if not os.path.exists('signatures/'):
    home_fs.makedir(u'signatures')
    logger.info('Created signatures directory.')
else:
    logger.info('signatures directory already exists, skipping...')

if not os.path.exists('.gnupg/'):
    home_fs.makedir(u'.gnupg/')
    gpg = gnupg.GPG(gnupghome='./.gnupg')
    logger.info('Created gnupg home directory.')
    
    input_data = gpg.gen_key_input(key_type="RSA", key_length=4096, passphrase=input('Enter passphrase for your new key: '))
    key = gpg.gen_key(input_data)
    logger.info('Generated a new user key.')
    with open('userfp', 'w') as f:
        f.write(key.fingerprint)
    logger.info('Wrote user key fingerprint into file.\n Ready for the first run.')
else:
    logger.info('gnupg directory already exists, skipping...')
