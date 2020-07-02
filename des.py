import pyperclip
from Crypto.Cipher import DES3
from Crypto import Random

class DES:

    def __init__(self):
        pass


    def padding(self, string):
        # Pad the plain_text with blank spaces to the right
        padded_string = string + (8 - len(string) % 8) * ' '
        return padded_string


    def check_key(self, key):
        length = len(key.encode('utf-8'))

        if (key.startswith('b\'') and key.endswith('\'')) or length == 16 or length == 24:
            return True
        return False


    def random_key(self):
        key = Random.get_random_bytes(24)
        return key


    def encrypt(self, plain_text, key):
        cipher = DES3.new(key)
        cipher_text = cipher.encrypt(plain_text)
        return str(cipher_text)


    def decrypt(self, cipher_text, key):
        # Convert string representation of bytes to actual bytes
        cipher_text = eval(cipher_text)

        if (key.startswith('b\'') and key.endswith('\'')):
            key = eval(key)

        cipher = DES3.new(key)
        plain_text = cipher.decrypt(cipher_text).decode(encoding="utf-8")

        # Remove extra padding spaces to the right of the plain_text
        plain_text = plain_text.rstrip()
        return plain_text



def ask_user():
    print("Select an option:")
    print("1. To continue")
    print("2. To exit")
    option = input()
    return option


if __name__ == "__main__":
    des = DES()

    while True:
        #try:
            print("Select an option:")
            print("1. Encrypt a message")
            print("2. Decrypt a message")
            option = input()
            if option == '1':
                print("Enter plain text to be encrypted: ")
                plain_text = input()
                print("Enter 16 or 24 byte key for encryption or leave blank (press enter) for randomly generated key: ")
                key = input()
                if key == '':
                    key = des.random_key()
                    print("Randomly Generated Key =", key)
                else:
                    while not des.check_key(key):
                        print("Key length is not 16 or 24 bytes long.")
                        print("Enter the new key for encryption or leave blank (press enter) for randomly generated key: ")
                        key = input()
                        if key == '':
                            key = des.random_key()
                            print("Randomly Generated Key =", key)
                plain_text = des.padding(plain_text)
                cipher_text = des.encrypt(plain_text, key)
                print("Cipher text =", cipher_text)

                pyperclip.copy(str(cipher_text))
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

                while not des.check_key(key):
                    print("Key length is not 16 or 24 bytes long.")
                    print("Enter the correct key for decryption")
                    key = input()

                plain_text = des.decrypt(cipher_text, key)
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

        # except Exception as e:
        #     option = ask_user()
        #     if option == '1':
        #         continue
        #     elif option == '2':
        #         print("Exiting program")
        #         break
        #     else:
        #         print("Incorrect input.")
        #         print("Exiting program")
        #         break