import gnupg
import os
import fs
from fs import open_fs
from gen_keys import retrieve

class Encrypt:
    '''
    Docs go here
    '''
    def __init__(self):
        self.gpg = gnupg.GPG(gnupghome='./.gnupg')
        self.home_fs = open_fs('.')
        # self.keys = 
