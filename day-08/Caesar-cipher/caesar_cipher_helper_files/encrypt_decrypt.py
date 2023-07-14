from caesar_cipher_helper_files.alphabets import alphabet


def encrypt(text, shift):
    encrypted_text = ""
    for letter in text:
        if letter not in alphabet:
            encrypted_text += letter
            continue 
        letter_index = alphabet.index(letter)
        index = letter_index + shift
        encrypted_text += alphabet[index if letter_index +
                                   shift < 26 else abs(26-index)]

    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for letter in text:
        if letter not in alphabet:
            decrypted_text += letter
            continue 
        letter_index = alphabet.index(letter)
        index = letter_index - shift
        decrypted_text += alphabet[index if letter_index -
                                   shift >= 0 else 26-abs(index)]

    return decrypted_text