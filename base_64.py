import pyperclip
import base64

class Base64:

    def encode(plain_text):
        ascii = plain_text.encode()
        base64_text = base64.b64encode(ascii)
        return base64_text.decode()


    def decode(base64_text):
        ascii = base64_text.encode()
        plain_text = base64.b64decode(ascii)
        return plain_text.decode()


def ask_user():
    print("Select an option:")
    print("1. To retry")
    print("2. To exit")
    option = input()
    return option

if __name__ == "__main__":

    while True:
        #try:
        print("Select an option:")
        print("1. Encode a message")
        print("2. Decode a message")
        option = input()
        if option == '1':
            print("Enter plain text to be encoded: ")
            plain_text = input()

            base64_text = Base64.encode(plain_text)
            print("Base64 text =", base64_text)
            pyperclip.copy(base64_text)
            pyperclip.paste()
            print("The Base64 text has been copied to your clipboard" + "\n")

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
            print("Enter Base64 text to be decoded: ")
            base64_text = input()

            plain_text = Base64.decode(base64_text)
            print("Base64 text =", plain_text)
            pyperclip.copy(plain_text)
            pyperclip.paste()
            print("The Base64 text has been copied to your clipboard" + "\n")

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

        #
        # except Exception as e:
        #     option = ask_user()
        #     if option == '1':
        #         continue
        #     elif option == '2':
        #         print("Exiting program")
        #         break
        #     else:
        #         print("Incorrect input.")
        #         print("Exiting program")
        #         break