import base64

BASE64_TABLE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def b64encode(table, data):
    return base64.b64encode(data).decode().translate(str.maketrans(BASE64_TABLE, table)).encode()

def b64decode(table, data):
    return base64.b64decode(data.decode().translate(str.maketrans(table, BASE64_TABLE)))

if __name__ == '__main__':
    table = 'abcdefghijklmnopqrstuvwxyz0123456789+/ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print(b64encode(table, b'th1s_1s_k3y!!!!!'))
    print(b64decode(table, b'3g6L2PWL2PXFmR+7ise7iq=='))