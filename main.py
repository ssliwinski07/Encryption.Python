from lib.encryption import Encryption
import sys

plain_password = sys.argv[1]

def main():
    
    encryption = Encryption()

    encrypted_pwd = encryption.encrypt_password(plain_password)
    decrypted_pwd = encryption.decrypt_password(encrypted_pwd)

    print(encrypted_pwd)
    print(decrypted_pwd)
     

if __name__ == "__main__":
    main()