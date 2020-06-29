import pyperclip

class Caesar_Cipher:

    def __init__(self):
        self.SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'


    def encrypt(self, plain_text, shift):
        shift = shift % len(self.SYMBOLS)
        cipher_text = []
        for char in plain_text:
            if char not in self.SYMBOLS:
                cipher_text.append(char)
                continue
            index = self.SYMBOLS.find(char)
            new_index = index + shift
            new_index = new_index % len(self.SYMBOLS)
            cipher_text.append(self.SYMBOLS[new_index])

        return "".join(cipher_text)

    def decrypt(self, cipher_text, shift):
        shift = shift % len(self.SYMBOLS)
        plain_text = []
        for char in cipher_text:
            if char not in self.SYMBOLS:
                plain_text.append(char)
                continue
            index = self.SYMBOLS.find(char)
            new_index = index - shift
            new_index = new_index % len(self.SYMBOLS)
            plain_text.append(self.SYMBOLS[new_index])

        return "".join(plain_text)

    def brute_force_decrypt(self, cipher_text):
        all_combinations = []
        for shift in range(len(self.SYMBOLS)):
            decrypted_text = self.decrypt(cipher_text, shift)
            print("Key = {}, Plain text = {}".format(key, decrypted_text))

        return None

def ask_user():
    print("Select an option:")
    print("1. To continue")
    print("2. To exit")
    option = input()
    return option

if __name__ == "__main__":
    caesar_cipher = Caesar_Cipher()
    while True:
        try:
            print("Select an option:")
            print("1. Encrypt a message")
            print("2. Decrypt a message")
            option = input()
            if option == '1':
                print("The accepted list of characters are:")
                print(caesar_cipher.SYMBOLS)
                print("Enter plain text to be encrypted: ")
                plain_text = input()
                print("Enter a number (key) for encryption: ")
                shift = int(input())

                cipher_text = caesar_cipher.encrypt(plain_text, shift)
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
                shift = input()
                if shift == 'crack':
                    brute_force = caesar_cipher.brute_force_decrypt(cipher_text)

                else:
                    shift = int(shift)

                    plain_text = caesar_cipher.decrypt(cipher_text, shift)
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
