"""
Author: Nikita Sinkha
Date: 1/31/2018
File: iterative-functions.py
"""
def gcd(a, b):
    """
    func: gcd():
    Takes 2 positive numbers and computes the Greatest Common Divisor using the method
    of iteration.
    param1: a -> A positive number.
    param2: b -> A positive number.
    """
    while b != 0:
        (a, b) = (b , a%b)
    return a

def test_gcd():
    """
    test_gcd():
    Function that checks the working of the GCD function.
    """
    print(gcd(2, 4))
    print(gcd(3, 6))
    print(gcd(5, 9))
    print(gcd(7, 8))
    print(gcd(8, 3))


def lcm(x, y):
    """
    func: lcm():
    Takes 2 positive numbers and computes the Least Common Multiple using the method
    of iteration.
    param1: x -> A positive number.
    param2: y -> A positive number.
    """
    if x > y:
        x, y = y, x
    for i in range(y, x*y+1, y):
        if i%x == 0:
            return i
        

def test_lcm():
    """
    test_lcm():
    Function that checks the working of the LCM function.
    """
    print(lcm(2, 4))
    print(lcm(4, 4))
    print(lcm(7, 13))
    print(lcm(8, 5))
    print(lcm(9, 8))


def pow(n, e):
    """
    func: pow():
    Takes in a base and an exponent and computes the output as base to the power exponent
    using the mwthod of iteration.
    param1: n -> Acts as a base.
    param2: e -> Acts as an exponent.
    """
    temp = 1
    if e == 0:
        return 1
    for i in range(e):
        temp = temp*n
    return temp


def test_pow():
    """
    test_pow():
    Function that checks the working of the pow function.
    """
    print(pow(2, 0))
    print(pow(3, 3))
    print(pow(4, 4))
    print(pow(5, 5))
    print(pow(6, 2))


def is_factor(q, w):
    """
    func: is_factor():
    Takes 2 positive numbers and sees if the first number 'q' is a factor of 'w' using the method
    of iteration.
    param1: q -> A positive number.
    param2: w -> A positive number.
    """
    if q > w:
        print("2nd number should be greater than first")
        return "Try again"
    else:
        temp = 1
        for i in range(1):
            if w%q != 0:
                return False
            else:
                return True


def test_is_factor():
    """
    func: test_is_factor():
    Function that checks the working of is_factor function.
    """
    print(is_factor(2, 5))
    print(is_factor(2, 8))
    print(is_factor(3, 9))
    print(is_factor(3, 7))
    print(is_factor(6, 12))



def main():
    """
    func: main()
    Executes the program in order to produce the required outcome.
    """
    
    ######################################################
    #Remove comments to see the working of test functions#
    ######################################################
    """
    print("#################Test Functions#################")
    print("Test results for test_pow() function")
    test_pow()
    print("")
    print("Test results for test_gdc() function")
    test_gdc()
    print("")
    print("Test results for test_lcm() function")
    test_lcm()
    print("")
    print("Test results for test_is_factor() function")
    test_is_factor()
    print("")
    """
    print("List of operations:")
    print("1. POW")
    print("2. GCD")
    print("3. LCM")
    print("4. is_factor")
    print("")
    
    while True:
        user = str(input("Enter a number from 1-4 to select an operation (stop to quit):"))
        if user in "stop":
            return False
        else:
            if user in '1':
                print("You have selected the POW function.")
                base = int(input("Enter the base:"))
                expo = int(input("Enter the exponent:"))
                print("Your output would be processed as", base, "to the power", expo)
                print("Answer:", pow(base, expo))
                print("")
                return main()
            elif user in '2':
                print("You have selected the GCD function.")
                n1 = int(input("Enter a positive number:"))
                n2 = int(input("Enter a positive number:"))
                print("Your output would be processed as", "gcd("+str(n1)+","+str(n2)+")")
                print("Answer:", gcd(n1, n2))
                print("")
                return main()
            elif user in '3':
                print("You have selected the LCM function.")
                n1 = int(input("Enter a positive number:"))
                n2 = int(input("Enter a positive number:"))
                print("Your output would be processed as", "lcm("+str(n1)+","+str(n2)+")")
                print("Answer:", lcm(n1, n2))
                print("")
            elif user in '4':
                print("You have selected the is_factor function.")
                n1 = int(input("Enter a positive number:"))
                n2 = int(input("Enter a positive number:"))
                print("Your output would be processed as", "is_factor("+str(n1)+","+str(n2)+")")
                print("Answer:", is_factor(n1, n2))
                print("")
                return main()
    exit()

if __name__ == "__main__" :
    main()
    



    
