import os
from fs import open_fs
import gnupg
from pki import KeyManager, Encrypt, Decrypt 

home_fs = open_fs('.')

if not os.path.exists('signatures/'):
    home_fs.makedir(u'signatures')
    print('Created signatures directory')

if not os.path.exists('.gnupg/'):
    home_fs.makedir(u'.gnupg/')
    print('Created gnupg directory')
    gpg = gnupg.GPG(gnupghome='./.gnupg')
    
    input_data = gpg.gen_key_input(key_type="RSA", key_length=4096, passphrase=input('Enter passphrase for your new key: '))
    key = gpg.gen_key(input_data)
    with open('userfp', 'w') as f:
        f.write(key.fingerprint)
    print('Created user key and saved fingerprint')

