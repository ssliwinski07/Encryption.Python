from cryptography.fernet import Fernet

class Encryption:
    #key = b'ZmDfcTF7_60GrrY167zsiPd67pEvs0aGOv2oasOM1Pg='

    _key = Fernet.generate_key()
    _cipher = Fernet(_key)

    def __init__(self, plain_password: str):
        self.plain_password = plain_password
        
    def encrypt_password(self):
        token = self.plain_password.encode()
        encrypted_password = self._cipher.encrypt(token).decode()
        return encrypted_password

    def decrypt_password(self, encrypted_password):
        decrypted_password = self._cipher.decrypt(encrypted_password).decode()
        return decrypted_password

    def print_encrypted_decrypted(self):

        encrypted_password = self.encrypt_password()
        decrypted_password = self.decrypt_password(encrypted_password)

        print(f"Encrypted pwd: {encrypted_password}")
        print(f"Decrypted pwd: {decrypted_password}")





