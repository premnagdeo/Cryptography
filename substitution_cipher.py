import pyperclip
import string
import random


class Substitution_Cipher:

    def __init__(self):
        pass

    def check_key(self, key):
        key = "".join(sorted(list(key)))
        key.upper()
        return key == string.ascii_uppercase

    def random_key(self):
        randomList = list(string.ascii_uppercase)
        random.shuffle(randomList)
        return ''.join(randomList)


    def encrypt(self, plain_text, key):
        cipher_text = []
        for char in plain_text:
            if char.upper() in string.ascii_uppercase:
                index = string.ascii_uppercase.find(char.upper())
                if char.isupper():
                    cipher_text.append(key[index].upper())
                else:
                    cipher_text.append(key[index].lower())
            else:
                cipher_text.append(char)

        return "".join(cipher_text)


    def decrypt(self, cipher_text, key):
        plain_text = []
        for char in cipher_text:
            if char.upper() in string.ascii_uppercase:
                index = key.find(char.upper())
                if char.isupper():
                    plain_text.append(string.ascii_uppercase[index].upper())
                else:
                    plain_text.append(string.ascii_uppercase[index].lower())
            else:
                plain_text.append(char)

        return "".join(plain_text)


def ask_user():
    print("Select an option:")
    print("1. To continue")
    print("2. To exit")
    option = input()
    return option


if __name__ == "__main__":
    substitution_cipher = Substitution_Cipher()
    while True:

        try:
            print("Select an option:")
            print("1. Encrypt a message")
            print("2. Decrypt a message")
            option = input()
            if option == '1':
                print("Enter plain text to be encrypted: ")
                plain_text = input()
                print("Enter alphabet key list for encryption or leave blank (press enter) for randomly generated key: ")
                key = input()
                if key == '':
                    key = substitution_cipher.random_key()
                    print("Randomly Generated Key =", key)

                while substitution_cipher.check_key(key) == False:
                    print("Key did not include all 26 letters of the alphabet.")
                    print("Enter the new key for encryption or leave blank (press enter) for randomly generated key: ")
                    key = input()
                    if key == '':
                        key = substitution_cipher.random_key()
                        print("Randomly Generated Key =", key)

                cipher_text = substitution_cipher.encrypt(plain_text, key)
                print("Cipher text =", cipher_text)

                pyperclip.copy(cipher_text)
                pyperclip.paste()
                print("The cipher text has been copied to your clipboard" + "\n")

                option = ask_user()
                if option == '1':
                    continue
                elif option == '2':
                    break
                else:
                    print("Incorrect input.")
                    print("Exiting program")
                    break

            elif option == '2':
                print("Enter cipher text to be decrypted: ")
                cipher_text = input()
                print("Enter key for decryption: ")

                key = input()

                plain_text = substitution_cipher.decrypt(cipher_text, key)
                print("Plain text =", plain_text)

                pyperclip.copy(plain_text)
                pyperclip.paste()
                print("The plain text has been copied to your clipboard" + "\n")

                option = ask_user()
                if option == '1':
                    continue
                elif option == '2':
                    print("Exiting program")
                    break
                else:
                    print("Incorrect input.")
                    print("Exiting program")
                    break

            else:
                print("Incorrect input.")
                option = ask_user()
                if option == '1':
                    continue
                elif option == '2':
                    print("Exiting program")
                    break
                else:
                    print("Incorrect input.")
                    print("Exiting program")
                    break

        except Exception as e:
            option = ask_user()
            if option == '1':
                continue
            elif option == '2':
                print("Exiting program")
                break
            else:
                print("Incorrect input.")
                print("Exiting program")
                break