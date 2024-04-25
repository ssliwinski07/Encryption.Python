from cryptography.fernet import Fernet
import base64
import logging

class Encryption:
    #key = b'ZmDfcTF7_60GrrY167zsiPd67pEvs0aGOv2oasOM1Pg='

    @staticmethod
    def encrypt_password(password: str, key: str):
        key_bytes = key.encode()
        cipher = Fernet(key_bytes)
        password_to_encrypt = password.encode()

        try: 
            encrypted_password = cipher.encrypt(password_to_encrypt).decode()              
        except Exception as e:
            print('En error occured during password encryption: {e}')
            return None
        
        return encrypted_password  
   
    @staticmethod
    def decrypt_password(encrypted_password: str, key: str):
        key_bytes = key.encode()
        cipher = Fernet(key_bytes)  
        
        try:
            decrypted_password = cipher.decrypt(encrypted_password).decode()     
        except Exception as e:
            print('En error occured during password decryption: {e}')
            return None
        
        return decrypted_password

    @staticmethod
    def print_encrypted_decrypted(password: str, key: str):
        encrypted_password = Encryption.encrypt_password(password, key)
        decrypted_password = Encryption.decrypt_password(encrypted_password, key)

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