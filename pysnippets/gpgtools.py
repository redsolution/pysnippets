# -*- coding: utf-8 -*-
import gnupg
import json


def check_data_sign(data):
    if not data:
        return None
    gpg = gnupg.GPG()
    gpg.encoding = 'utf-8'
    if data.get('sign') and gpg.verify(data['sign']):
        return data['data']
    return None


def sign_data(data):
    gpg = gnupg.GPG()
    gpg.encoding = 'utf-8'
    return gpg.sign(str(data))


def get_signed_json(data):
    return json.dumps({'sign': sign_data(data).data, 'data': data})


def encrypt_data(data, key_name):
    gpg = gnupg.GPG()
    gpg.encoding = 'utf-8'
    enc = gpg.encrypt(data, key_name)
    if enc.data and enc.status == 'encryption ok':
        return enc.data
    else:
        return None


def decrypt_data(data):
    if not data:
        return data
    gpg = gnupg.GPG()
    gpg.encoding = 'utf-8'
    return gpg.decrypt(data).data
