import base64

ORIG_BASE64_TABLE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
ALTERED_BASE64_TABLE = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/'


def b64encode(data):
    return base64.b64encode(data).decode().translate(str.maketrans(ORIG_BASE64_TABLE, ALTERED_BASE64_TABLE)).encode()

def b64decode(data):
    return base64.b64decode(data.decode().translate(str.maketrans(ALTERED_BASE64_TABLE, ORIG_BASE64_TABLE)))

if __name__ == '__main__':
    print(b64decode(b'tvjdvez7D0vSyZbnzv90mf9nuKnurL8YBZiXiseHFq==').decode())