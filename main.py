from Encryption.encryption import Encryption
import sys
import argparse

def main():

    parser = argparse.ArgumentParser(description='Encrypt and decrypt a password using a key.')

    if len(sys.argv) < 3:
        print('Usage: python3(macOS)/python(windows, linux) main.py <password> <key>')
        return
    
    parser.add_argument('--password', type=str, required=True)
    parser.add_argument('--encryption_key', type=str, required=True)

    args = parser.parse_args()
       
    encrypted_pwd = Encryption.encrypt_password(password=args.password, key=args.encryption_key)
    decrypted_pwd = Encryption.decrypt_password(encrypted_password=encrypted_pwd, key=args.encryption_key)

    print(f"Encrypted password: {encrypted_pwd}")
    print(f"Decrypted password: {decrypted_pwd}")
     
if __name__ == "__main__":
    main()