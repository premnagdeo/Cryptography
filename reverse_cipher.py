import pyperclip

class Reverse_Cipher:

    def __init__(self):
        pass

    def encrypt(self, plain_text):
        return plain_text[::-1]

    def decrypt(self, cipher_text):
        return cipher_text[::-1]


def ask_user():
    print("Select an option:")
    print("1. To continue")
    print("2. To exit")
    option = input()
    return option


if __name__ == "__main__":
    reverse_cipher = Reverse_Cipher()
    while True:
        try:
            print("Select an option:")
            print("1. Encrypt a message")
            print("2. Decrypt a message")
            option = input()
            if option == '1':
                print("Enter plain text to be encrypted: ")
                plain_text = input()

                cipher_text = reverse_cipher.encrypt(plain_text)
                print("Cipher text =", cipher_text)
                pyperclip.copy(cipher_text)
                pyperclip.paste()
                print("The cipher text has been copied to your clipboard" + "\n")

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

            elif option == '2':
                print("Enter cipher text to be decrypted: ")
                cipher_text = input()

                plain_text = reverse_cipher.decrypt(cipher_text)
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