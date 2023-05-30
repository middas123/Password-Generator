# Write a password generator in Python.
# strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.


import string
import random

characters = string.ascii_letters
chartest = [characters[i] for i in range(len(characters))]
digits = string.digits
special = string.punctuation
randomValue = characters + digits + special
#regex pattern is here = ""



def createpassword(randomValue, passlen):
    password = ''.join(random.sample(randomValue, passlen))
    return password


def mainstart():

    #try checks if all the following conditions are met
    try:
        passlen = int(input("Enter the length of your password greater than 6: "))
        if   6 < passlen <= 12:
            password = createpassword(randomValue, passlen)
            #regexHere
            print(password)

            reqagain = input("Want to try again? Y/N ").lower()
            if reqagain == 'y':
                mainstart()
            elif reqagain == 'n':
                print("Thank you for using the password generator.")
                quit()
            else:
                print("Invalid Input. Try again.")
                mainstart()

        else:
            print("Password should be greater than 6 and less than 12. Retry!")
            mainstart()
    #if not it will print the error and reset the code
    except ValueError:
            print("input is not a number!!")
            mainstart()
        


mainstart()
