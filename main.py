# Warren Garrido's work-
def encode(password):
    new_password = ""
    for char in password:
        num = int(char)
        new_num = num + 3
        if len(str(new_num)) == 2:
            new_num = new_num - 10
        new_password += str(new_num)

    return new_password

def decode(password):
    decodedPass = ""
    for i in password:
        tempNum = int(i)
        tempNum = tempNum - 3
        if tempNum < 0:
            tempNum += 10
        decodedPass += str(tempNum)
    return decodedPass

if __name__ == "__main__":
    program_on = True
    while program_on:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
            print()
        try:
            if option == 2:
                decoded_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
        except:
            print("Encode password first.")
            print()
        if option == 3:
            exit()



