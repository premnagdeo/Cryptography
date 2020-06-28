import pyperclip

class Caesar_Cipher:
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    def encrypt(plain_text, shift):
        shift = shift % len(Caesar_Cipher.SYMBOLS)
        cipher_text = []
        for char in plain_text:
            if char not in Caesar_Cipher.SYMBOLS:
                cipher_text.append(char)
                continue
            index = Caesar_Cipher.SYMBOLS.find(char)
            new_index = index + shift
            new_index = new_index % len(Caesar_Cipher.SYMBOLS)
            cipher_text.append(Caesar_Cipher.SYMBOLS[new_index])

        return "".join(cipher_text)

    def decrypt(cipher_text, shift):
        shift = shift % len(Caesar_Cipher.SYMBOLS)
        plain_text = []
        for char in cipher_text:
            if char not in Caesar_Cipher.SYMBOLS:
                plain_text.append(char)
                continue
            index = Caesar_Cipher.SYMBOLS.find(char)
            new_index = index - shift
            new_index = new_index % len(Caesar_Cipher.SYMBOLS)
            plain_text.append(Caesar_Cipher.SYMBOLS[new_index])

        return "".join(plain_text)

    def brute_force_decrypt(cipher_text):
        all_combinations = []
        for shift in range(len(Caesar_Cipher.SYMBOLS)):

            shift = shift % len(Caesar_Cipher.SYMBOLS)
            plain_text = []
            for char in cipher_text:
                if char not in Caesar_Cipher.SYMBOLS:
                    plain_text.append(char)
                    continue
                index = Caesar_Cipher.SYMBOLS.find(char)
                new_index = index - shift
                new_index = new_index % len(Caesar_Cipher.SYMBOLS)
                plain_text.append(Caesar_Cipher.SYMBOLS[new_index])

            all_combinations.append("".join(plain_text))
        return all_combinations


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
                print("The accepted list of characters are:")
                print(Caesar_Cipher.SYMBOLS)
                print("Enter plain text to be encrypted: ")
                plain_text = input()
                print("Enter a number for encryption: ")
                shift = int(input())

                cipher_text = Caesar_Cipher.encrypt(plain_text, shift)
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
                    brute_force = Caesar_Cipher.brute_force_decrypt(cipher_text)
                    print("Decrypted plain texts:")
                    for i in range(len(Caesar_Cipher.SYMBOLS)):
                        print("Key = {}, Plain text = {}".format(i, brute_force[i]))

                else:
                    shift = int(input())
                    plain_text = Caesar_Cipher.decrypt(cipher_text, shift)
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
