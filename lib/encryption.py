from cryptography.fernet import Fernet
import base64

class Encryption:
    #key = b'ZmDfcTF7_60GrrY167zsiPd67pEvs0aGOv2oasOM1Pg='

    _key = Fernet.generate_key()
    _cipher = Fernet(_key)
      
    @staticmethod
    def encrypt_password(password: str):
        password_to_encrypt = password.encode()
        encrypted_password = Encryption._cipher.encrypt(password_to_encrypt).decode()
        return encrypted_password
    
    @staticmethod
    def decrypt_password(encrypted_password):
        decrypted_password = Encryption._cipher.decrypt(encrypted_password).decode()
        return decrypted_password

    @staticmethod
    def print_encrypted_decrypted():
        encrypted_password = Encryption.encrypt_password()
        decrypted_password = Encryption.decrypt_password(encrypted_password)

        print(f"Encrypted pwd: {encrypted_password}")
        print(f"Decrypted pwd: {decrypted_password}")

    @staticmethod
    def encode64(password: str):
        password_to_encode = password.encode()
        encoded_password = base64.b64encode(password_to_encode).decode()
        return encoded_password
    
    @staticmethod
    def decode64(encoded_password):
        decoded = base64.b64decode(encoded_password).decode()
        return decoded
    
    @staticmethod
    def get_encryption_key():
        key = Fernet.generate_key().decode()
        return key