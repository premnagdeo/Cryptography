import pyperclip

class Reverse_Cipher:
    def encrypt(plain_text):
        return plain_text[::-1]

    def decrypt(cipher_text):
        return cipher_text[::-1]


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

                cipher_text = Reverse_Cipher.encrypt(plain_text)
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

                plain_text = Reverse_Cipher.decrypt(cipher_text)
                print("Plain text =", plain_text)
                pyperclip.copy(plain_text)
                pyperclip.paste()
                print("The plain text has been copied to your clipboard" + "\n")

                option = ask_user()
                if option == '1':
                    continue
                elif option == '2':
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
                break
            else:
                print("Incorrect input.")
                print("Exiting program")
                break