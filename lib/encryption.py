from cryptography.fernet import Fernet
import base64

class Encryption:
    #key = b'ZmDfcTF7_60GrrY167zsiPd67pEvs0aGOv2oasOM1Pg='

    _key = Fernet.generate_key()
    _cipher = Fernet(_key)

    def __init__(self, password: str):
        self.password = password
        
    def encrypt_password(self):
        password_to_encrypt = self.password.encode()
        encrypted_password = self._cipher.encrypt(password_to_encrypt).decode()
        return encrypted_password

    def decrypt_password(self, encrypted_password):
        decrypted_password = self._cipher.decrypt(encrypted_password).decode()
        return decrypted_password

    def print_encrypted_decrypted(self):

        encrypted_password = self.encrypt_password()
        decrypted_password = self.decrypt_password(encrypted_password)

        print(f"Encrypted pwd: {encrypted_password}")
        print(f"Decrypted pwd: {decrypted_password}")

    def encode64(self):
        password_to_encode = self.password.encode()
        encoded_password = base64.b64encode(password_to_encode).decode()
        return encoded_password
    
    @staticmethod
    def decode64(encoded):
        decoded = base64.b64decode(encoded).decode()
        return decoded





