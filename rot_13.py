import pyperclip

class Rot_13:

    def __init__(self):
        self.SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    def encrypt(self, plain_text):
        cipher_text = []
        for char in plain_text:
            if char not in self.SYMBOLS:
                cipher_text.append(char)
                continue
            index = self.SYMBOLS.find(char)
            new_index = index + 13
            new_index = new_index % len(self.SYMBOLS)
            cipher_text.append(self.SYMBOLS[new_index])

        return "".join(cipher_text)

    def decrypt(self, cipher_text):
        plain_text = []
        for char in cipher_text:
            if char not in self.SYMBOLS:
                plain_text.append(char)
                continue
            index = self.SYMBOLS.find(char)
            new_index = index - 13
            new_index = new_index % len(self.SYMBOLS)
            plain_text.append(self.SYMBOLS[new_index])

        return "".join(plain_text)


def ask_user():
    print("Select an option:")
    print("1. To continue")
    print("2. To exit")
    option = input()
    return option

if __name__ == "__main__":
    rot_13 = Rot_13()
    while True:
        try:
            print("Select an option:")
            print("1. Encrypt a message")
            print("2. Decrypt a message")
            option = input()
            if option == '1':
                print("The accepted list of characters are:\n", rot_13.SYMBOLS)
                print("Enter plain text to be encrypted: ")
                plain_text = input()

                cipher_text = rot_13.encrypt(plain_text)
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

                plain_text = rot_13.decrypt(cipher_text)
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