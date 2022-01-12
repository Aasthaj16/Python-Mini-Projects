import random
import string

welcomeMessage = """

----WELCOME TO PASSWORD GENERATOR----

CREATE YOUR PASSWORD JUST BY ANSWERING A FEW QUESTIONS"""

print(welcomeMessage)

# Function to generate random alphabets


def alpha_generator(len_alpha):
    return ''.join(random.sample(string.ascii_letters, alphabet))


# Function to generate random numbers
def num_generator(len_num):
    numList = ""
    for n in range(num):
        numList += str(random.randrange(0, 10))
    return numList


length = int(input("Enter length of the password: "))
num = int(input("How many digits it should contain? "))
alphabet = int(input("How many alphabets it should contain? "))

if num + alphabet != length:
    print("Please enter valid numbers to meet the provided length of password.")

else:
    ans = alpha_generator(alphabet) + num_generator(num)
    print("---------------------------")
    print("Generated Password is:", ''.join(random.sample(ans, len(ans))))
    print("---------------------------")
