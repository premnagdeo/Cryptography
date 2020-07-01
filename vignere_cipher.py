import pyperclip
import string
import random


class Vignere_Cipher:

    def __init__(self):
        pass

    def check_key(self, key):
        for char in key:
            if not char.isalpha():
                return False
        return True


    def random_key(self):
        key = string.ascii_lowercase * random.randint(1,5)
        key = list(key)
        random.shuffle(key)
        key = random.choices(key, k=random.randint(12, 15))
        return "".join(key)


    def encrypt(self, plain_text, key):
        cipher_text = []

        keyindex = 0
        key = key.lower()

        for char in plain_text:
            index = string.ascii_lowercase.find(char.lower())
            if index != -1:
                index += string.ascii_lowercase.find(key[keyindex])
                index = index % 26

                if char.isupper():
                    cipher_text.append(string.ascii_uppercase[index])
                else:
                    cipher_text.append(string.ascii_lowercase[index])

                keyindex +=1
                if keyindex == len(key):
                    keyindex = 0
            else:
                cipher_text.append(char)

        return "".join(cipher_text)


    def decrypt(self, cipher_text, key):
        plain_text = []

        keyindex = 0
        key = key.lower()

        for char in cipher_text:
            index = string.ascii_lowercase.find(char.lower())
            if index != -1:
                index -= string.ascii_lowercase.find(key[keyindex])
                index = index % 26

                if char.isupper():
                    plain_text.append(string.ascii_uppercase[index])
                else:
                    plain_text.append(string.ascii_lowercase[index])

                keyindex += 1
                if keyindex == len(key):
                    keyindex = 0
            else:
                plain_text.append(char)

        return "".join(plain_text)


    def brute_force_decrypt(self, cipher_text):
        file = open('dictionary.txt')
        lines = file.readlines()
        file.close()

        for word in lines:
            word = word.strip()
            decrypted_text = self.decrypt(cipher_text, word)
            print("Key = {}, Plain text = {}".format(word, decrypted_text))

        return None


def ask_user():
    print("Select an option:")
    print("1. To continue")
    print("2. To exit")
    option = input()
    return option


if __name__ == "__main__":
    vignere_cipher = Vignere_Cipher()

    while True:
        try:
            print("Select an option:")
            print("1. Encrypt a message")
            print("2. Decrypt a message")
            option = input()
            if option == '1':
                print("Enter plain text to be encrypted: ")
                plain_text = input()
                print("Enter word (key) for encryption or leave blank (press enter) for randomly generated key: ")
                key = input()
                if key == '':
                    key = vignere_cipher.random_key()
                    print("Randomly Generated Key =", key)

                while vignere_cipher.check_key(key) == False:
                    print("Key contains not alphabet characters.")
                    print("Enter the new key for encryption or leave blank (press enter) for randomly generated key: ")
                    key = input()
                    if key == '':
                        key = vignere_cipher.random_key()
                        print("Randomly Generated Key =", key)

                cipher_text = vignere_cipher.encrypt(plain_text, key)
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
                    brute_force = vignere_cipher.brute_force_decrypt(cipher_text)

                else:
                    while vignere_cipher.check_key(key) == False:
                        print("Key contains not alphabet characters.")
                        print("Enter the correct key for decryption")
                        key = input()

                    plain_text = vignere_cipher.decrypt(cipher_text, key)
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