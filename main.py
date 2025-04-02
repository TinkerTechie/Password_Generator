import string
import random
if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    plen = int(input("Ener password length\n"))
    s = list(s1+s2+s3+s4)
    print(s)
    random.shuffle(s)
    print("Your password is: ")
    print("".join(s[0:plen]))