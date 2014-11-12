# -*- coding: utf-8 -*-
import gnupg
import json


def check_data_sign(data):
    if not data:
        return None
    gpg = gnupg.GPG()
    if data.get('sign') and gpg.verify(data['sign']):
        return data['data']
    return None


def sign_data(data):
    gpg = gnupg.GPG()
    return gpg.sign(str(data))


def get_signed_json(data):
    return json.dumps({'sign': sign_data(data).data, 'data': data})
