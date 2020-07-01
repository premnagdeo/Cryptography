import pyperclip
import math

class Transposition_Cipher:

    def __init__(self):
        pass

    def encrypt(self, plain_text, key):
        cipher_text = [""] * key

        for column in range(key):
            position = column
            while position < len(plain_text):
                cipher_text[column] += plain_text[position]
                position += key

        return "".join(cipher_text)

    def decrypt(self, cipher_text, key):
        number_of_cols = math.ceil(len(cipher_text) / key)
        number_of_rows = key
        number_of_unchecked = (number_of_cols * number_of_rows) - len(cipher_text)
        plain_text = [""] * number_of_cols
        column = 0
        row = 0

        for char in cipher_text:
            plain_text[column] += char
            column += 1
            if column == number_of_cols or (column == number_of_unchecked - 1 and row >= number_of_rows - number_of_unchecked):
                column = 0
                row += 1

        return "".join(plain_text)


    def brute_force_decrypt(self, cipher_text):
        for key in range(1, len(cipher_text)):
            decrypted_text = self.decrypt(cipher_text, key)
            print("Key = {}, Plain text = {}".format(key, decrypted_text))

        return None


def ask_user():
    print("Select an option:")
    print("1. To continue")
    print("2. To exit")
    option = input()
    return option


if __name__ == "__main__":
    transposition_cipher = Transposition_Cipher()
    while True:
        try:
            print("Select an option:")
            print("1. Encrypt a message")
            print("2. Decrypt a message")
            option = input()
            if option == '1':
                print("Enter plain text to be encrypted: ")
                plain_text = input()
                print("Enter a number (key) for encryption: ")
                key = int(input())

                cipher_text = transposition_cipher.encrypt(plain_text, key)
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
                print("If you do not know the key and would like to brute force the combinations, enter the word - crack")

                key = input()
                if key == 'crack':
                    transposition_cipher.brute_force_decrypt(cipher_text)

                else:
                    key = int(key)

                    plain_text = transposition_cipher.decrypt(cipher_text, key)
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