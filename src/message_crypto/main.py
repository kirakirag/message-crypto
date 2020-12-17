import pki

# encrypt = pki.Encrypt.Encrypt()
# decrypt = pki.Decrypt.Decrypt(input('Enter your passphrase: '))
keys = pki.KeyManager.KeyManager()

print(keys.gpg.list_keys())
# we need to run telegram here


# upon receiving 

# '-----BEGIN PGP PUBLIC KEY BLOCK' in a message

# we add a (user_id, user_key_id) to our database

# and do keys.import_key(keydata)


# upon receiving

# '-----BEGIN PGP MESSAGE' in a message

# we pass it to decrypt.decrypt_string(msg)

# and display plain text


# if we want to send a message to user with username

# we need to first resolve the username into a

# telegram user_id and then look up this user's public key

# in our database

# if key entry exists, we pass the plain text message

# to encrypt.encrypt(msg, key_id) and then send 

# the armored output over telegram