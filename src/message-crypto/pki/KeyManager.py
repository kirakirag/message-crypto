import gnupg

class KeyManager:
    def __init__(self):
        self.gpg = gnupg.GPG(gnupghome='./.gnupg')
        with open('userfp', 'r') as f:
            self.__user_fingerprint = f.read()
    
    def import_key(self, key_data):
        try:
            return self.gpg.import_keys(key_data)
        except Exception as e:
            print(e)

    def delete_key(self, fingerprint):
        try:
            return self.gpg.delete_keys(fingerprint)
        except Exception as e:
            print(e)

    def get_user_key(self):
        key = str(self.gpg.export_keys(self.__user_fingerprint))
        return key

    def get_user_fingerprint(self):
        return self.__user_fingerprint
