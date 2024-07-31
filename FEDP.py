#requirement -> cryptography / pystyle

from cryptography.fernet import Fernet
import base64
import os
from pystyle import *

System.Clear()
System.Title("FEDP")
System.Size(120, 35)

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
    while True:
        banner = Center.XCenter(r"""     
    ███████╗███████╗██████╗ ██████╗ 
    ██╔════╝██╔════╝██╔══██╗██╔══██╗
    █████╗  █████╗  ██║  ██║██████╔╝
    ██╔══╝  ██╔══╝  ██║  ██║██╔═══╝ 
    ██║     ███████╗██████╔╝██║     
    ╚═╝     ╚══════╝╚═════╝ ╚═╝     
    -------------------------------  
          [1] encrypt a file
          [2] decrypt a file
    -------------------------------
        """[1:])
        print(Colorate.Horizontal(Colors.blue_to_cyan, banner))
        print("\n"*2)

        choose = str(input("1/2 >>> "))
        if choose == "1":
            file = str(input("File path >>> "))
            in_key = str(input("Create key >>> "))
            key = gen_key(in_key)
            encrypt_file(file, key)
            print("\n"*2)
            input("Go to started page ? ENTER")
        if choose == "2":
            file = str(input("File path >>> "))
            in_key = str(input("Enter key >>> "))
            key = gen_key(in_key)
            decrypt_file(file, key)
            print("\n"*2)
            input("Go to started page ? ENTER")

        System.Clear()

#By Mathsdev 2024
