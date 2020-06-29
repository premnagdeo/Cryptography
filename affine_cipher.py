import pyperclip
import math

class Affine_Cipher:

    def __init__(self):
        self.SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

    def check_key(self, key):

        keyA = key // len(self.SYMBOLS)
        keyB = key % len(self.SYMBOLS)
        # Weak Key Checks
        if keyA == 1:
            print('Cipher is weak if key A is 1. Choose a different key.')
            return False
        if keyB == 0:
            print('Cipher is weak if key B is 0. Choose a different key.')
            return False
        if keyA < 0 or keyB < 0 or keyB > len(self.SYMBOLS) - 1:
            print('Key A must be greater than 0 and Key B must be between 0 and {}.'.format(len(self.SYMBOLS) - 1))
            return False
        if math.gcd(keyA, len(self.SYMBOLS)) != 1:
            print("Key A {} and the symbol set size {} are not relatively prime. Choose a different key.".format(keyA, len(self.SYMBOLS)))
            return False

        return True

    def mod_inv(self, a, m):
        if math.gcd(a, m) != 1:
            return False
        u1, u2, u3 = 1, 0, a
        v1, v2, v3 = 0, 1, m

        while v3 != 0:
            q = u3 // v3
            v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3

        return u1 % m

    def encrypt(self, plain_text, key):
        keyA = key // len(self.SYMBOLS)
        keyB = key % len(self.SYMBOLS)

        cipher_text = []

        for char in plain_text:
            if char in self.SYMBOLS:
                index = self.SYMBOLS.find(char)
                cipher_text.append(self.SYMBOLS[(index * keyA + keyB) % len(self.SYMBOLS)])
            else:
                cipher_text.append(char)

        return "".join(cipher_text)


    def decrypt(self, cipher_text, key):
        keyA = key // len(self.SYMBOLS)
        keyB = key % len(self.SYMBOLS)
        mod_inverse = self.mod_inv(keyA, len(self.SYMBOLS))
        if mod_inverse == False:
            print("MOD INV FALSE")

        plain_text = []

        for char in cipher_text:
            if char in self.SYMBOLS:
                index = self.SYMBOLS.find(char)
                plain_text.append(self.SYMBOLS[(index - keyB) * mod_inverse % len(self.SYMBOLS)])
            else:
                plain_text.append(char)

        return "".join(plain_text)


    def brute_force_decrypt(self, cipher_text):

        for key in range(len(self.SYMBOLS) ** 2):
            keyA = key // len(self.SYMBOLS)

            if math.gcd(keyA, len(self.SYMBOLS)) != 1:
                continue

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
    affine_cipher = Affine_Cipher()
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

                while affine_cipher.check_key(key) == False:
                    print("Enter the new key for encryption: ")
                    key = int(input())

                cipher_text = affine_cipher.encrypt(plain_text, key)
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
                    brute_force = affine_cipher.brute_force_decrypt(cipher_text)

                else:
                    key = int(key)

                    plain_text = affine_cipher.decrypt(cipher_text, key)
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