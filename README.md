# Overview

This is a simple Telegram client based on [Telethon](https://github.com/LonamiWebs/Telethon) with GPG encryption.

## Install

`git clone https://github.com/kirakirashit/message-crypto.git`

To log into Telegram you will need to create a file named _credentials_ and put your api*id and api_hash in there all in one line separated by a semicolon *;\_.

User's public key fingerprints are currently stored in a text file named _keys_ next to their corresponding *chat_id*s separated by a minus _-_

## Usage

Run t_client.py in the src/message-crypto folder. You will be prompted for a passphrase to encrypt your private key on the first run.
