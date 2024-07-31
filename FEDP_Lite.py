#requirement -> cryptography / os 
#USE python FEDP_Lite.py {encrypt/decrypt} file_path key
from cryptography.fernet import Fernet
import base64
import os
import argparse

def gen_key(k:str):
    key_bytes = k.encode('utf-8')
    key = base64.urlsafe_b64encode(key_bytes.ljust(32)[:32])
    return key
    
def encrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
    except:
        return print("Unable to access file")
        
    try:
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data)
    except:
        return print("Encrypt error")
        
    try:
        with open(file_path + '.fedp', 'wb') as file:
            file.write(encrypted_data)
            
        os.remove(file_path)
        return print(f'File encrypted successfully and saved as {file_path}.fedp')
    except:
        return print("Unable to save encrypted file")

def decrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()
    except:
        return print("Unable to access file")
        
    try:
        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data)
    except:
        return print("Decrypt error")

    try:
        original_file_path = file_path.replace('.fedp', '')
        if os.path.exists(original_file_path):
            original_file_path = f"_decrypted-{original_file_path}"
        with open(original_file_path, 'wb') as file:
            file.write(decrypted_data)

        os.remove(file_path)
        return print(f'File decrypted successfully and saved as {original_file_path}')
    except:
        return print("Unable to save decrypted file")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Encrypt or decrypt a file.')
    parser.add_argument('mode', choices=['encrypt', 'decrypt'], help='Mode : encrypt or decrypt')
    parser.add_argument('file_path', help='file path')
    parser.add_argument('key', help='key')
    
    args = parser.parse_args()
    
    key = gen_key(args.key)
    
    if args.mode == 'encrypt':
        encrypt_file(args.file_path, key)
    elif args.mode == 'decrypt':
        decrypt_file(args.file_path, key)


#By Mathsdev 2024