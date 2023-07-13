from caesar_cipher_helper_files.encrypt_decrypt import encrypt,decrypt
from caesar_cipher_helper_files.caesar_cipher_input import caesar_cipher_input 

is_end = False

while not is_end:
    direction,text,shift = caesar_cipher_input()
    enc_text = ""

    if shift < 0:
        print("Invalid input. Please provide a valid number")
        exit()
        
    if direction.lower() == "encode":
        enc_text = encrypt(text,shift)
        print(f"Here is your encoded result: {enc_text}")
    elif direction.lower() == "decode":
        enc_text = decrypt(text,shift)
        print(f"Here is your decoded result: {enc_text}")
    
    user_input = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    
    if user_input == "no":
        is_end = True
