from lib.encryption import Encryption
import sys

def main():
    if len(sys.argv) < 3:
        print('Usage: python3(macOS)/python(windows, linux) main.py <password> <key>')
        return
    
    plain_txt_password: str = sys.argv[1]
    encryption_key: str = sys.argv[2]
    
    encrypted_pwd = Encryption.encrypt_password(password=plain_txt_password, key=encryption_key)
    decrypted_pwd = Encryption.decrypt_password(encrypted_password=encrypted_pwd, key=encryption_key)
    encoded_pwd = Encryption.encode64(password=plain_txt_password)
    decoded_pwd = Encryption.decode64(encoded_password=encoded_pwd)

    print(f"Encoded password {encoded_pwd}")
    print(f"Decoded passowrd: {decoded_pwd}")
    print(f"Encrypted password: {encrypted_pwd}")
    print(f"Decrypted password: {decrypted_pwd}")
     
if __name__ == "__main__":
    main()