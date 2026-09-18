num=input("Enter number:")

def check_even_odd(num):
    if num%2==0:
        print("Even Number")
    else:
        print("Odd Number")


def check_prime(num):
    if num<1:
        return False
    for i in range(2,num):
        if num % i==0:
            return False
    return True
    