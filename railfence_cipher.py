import pyperclip
import math


class Railfence_Cipher:

    def __init__(self):
        pass

    def encrypt(self, plain_text, key):

        rail = [['\n' for i in range(len(plain_text))] for j in range(key)]

        dir_down = False
        row, col = 0, 0

        for i in range(len(plain_text)):

            if (row == 0) or (row == key - 1):
                dir_down = not dir_down

            rail[row][col] = plain_text[i]
            col += 1

            if dir_down:
                row += 1
            else:
                row -= 1

        cipher_text = []
        for i in range(key):
            for j in range(len(plain_text)):
                if rail[i][j] != '\n':
                    cipher_text.append(rail[i][j])

        return "".join(cipher_text)

    def decrypt(self, cipher_text, key):

        rail = [['\n' for i in range(len(cipher_text))] for j in range(key)]

        dir_down = None
        row, col = 0, 0

        for i in range(len(cipher_text)):
            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False

            rail[row][col] = '*'
            col += 1

            if dir_down:
                row += 1
            else:
                row -= 1

        index = 0
        for i in range(key):
            for j in range(len(cipher_text)):
                if ((rail[i][j] == '*') and (index < len(cipher_text))):
                    rail[i][j] = cipher_text[index]
                    index += 1

        plain_text = []
        row, col = 0, 0
        for i in range(len(cipher_text)):

            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False

            if (rail[row][col] != '*'):
                plain_text.append(rail[row][col])
                col += 1

            if dir_down:
                row += 1
            else:
                row -= 1

        return "".join(plain_text)

    def brute_force_decrypt(self, cipher_text):
        for key in range(2, len(cipher_text)):
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
    railfence_cipher = Railfence_Cipher()
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

                cipher_text = railfence_cipher.encrypt(plain_text, key)
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
                    railfence_cipher.brute_force_decrypt(cipher_text)

                else:
                    key = int(key)

                    plain_text = railfence_cipher.decrypt(cipher_text, key)
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
