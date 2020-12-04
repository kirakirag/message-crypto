import os
from fs import open_fs

home_fs = open_fs('.')

if not os.path.exists('signatures/'):
    home_fs.makedir(u'signatures')
    print('Created signatures directory')

if not os.path.exists('.gnupg/'):
    home_fs.makedir(u'.gnupg/')
    print('Create gnupg directory')
