import pyperclip
import math

class Transposition_Cipher:
    secret_key = 5

    def encrypt(plain_text):
        cipher_text = [""] * Transposition_Cipher.secret_key

        for column in range(Transposition_Cipher.secret_key):
            position = column
            while position < len(plain_text):
                cipher_text[column] += plain_text[position]
                position += Transposition_Cipher.secret_key

        return "".join(cipher_text)

    def decrypt(cipher_text):
        number_of_cols = math.ceil(len(cipher_text) / Transposition_Cipher.secret_key)
        number_of_rows = Transposition_Cipher.secret_key
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


def ask_user():
    print("Select an option:")
    print("1. To retry")
    print("2. To exit")
    option = input()
    return option


if __name__ == "__main__":

    while True:
        try:
            print("Select an option:")
            print("1. Encrypt a message")
            print("2. Decrypt a message")
            option = input()
            if option == '1':
                print("Enter plain text to be encrypted: ")
                plain_text = input()

                cipher_text = Transposition_Cipher.encrypt(plain_text)
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

                plain_text = Transposition_Cipher.decrypt(cipher_text)
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
                ask_user()
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