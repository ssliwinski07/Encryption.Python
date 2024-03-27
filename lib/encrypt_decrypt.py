from cryptography.fernet import Fernet
import sys

pwd = sys.argv[1]

key = b'ZmDfcTF7_60GrrY167zsiPd67pEvs0aGOv2oasOM1Pg='
# key2 = Fernet.generate_key()

def encrypt_password(plain_password: str, key):
    token = plain_password.encode()
    cipher = Fernet(key)
    encrypted_password = cipher.encrypt(token).decode()
    return encrypted_password

def decrypt_password(encrypted_password, key):
    cipher = Fernet(key)
    decrypted_password = cipher.decrypt(encrypted_password).decode()
    return decrypted_password

encrypted_password = encrypt_password(pwd, key)

decrypted_password = decrypt_password(encrypted_password, key)

print(f"Encrypted pwd: {encrypted_password}")

print(f"Decrypted pwd: {decrypted_password}")





