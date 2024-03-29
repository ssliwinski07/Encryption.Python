from lib.encryption import Encryption
import sys

def main():
    if len(sys.argv) < 2:
        print('Usage: python3(macOS)/python(windows) main.py <password>')
        return
    
    plain_password = sys.argv[1]
    
    encryption = Encryption(plain_password=plain_password)

    encrypted_pwd = encryption.encrypt_password()
    decrypted_pwd = encryption.decrypt_password(encrypted_pwd)

    print(encrypted_pwd)
    print(decrypted_pwd)
     

if __name__ == "__main__":
    main()