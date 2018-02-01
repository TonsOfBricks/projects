"""
Author: Nikita Sinkha
File: recursive_fruitfull.py
Date: 1/30/2018
"""

def pow(num, exp):
    """
    func: pow():
    Takes in a base and an exponent and computes the output as base to the power exponent
    using the mwthod of recursion.
    param1: num -> Acts as a base.
    param2: exp -> Acts as an exponent.
    """
    if exp == 0:
        return 1
    if exp > 0:
        return num*pow(num, exp-1)


def test_pow():
    """
    test_pow():
    Function that checks the working of the pow function.
    """
    print(pow(2,0))#Passed
    print(pow(3,1))#Passed
    print(pow(4,2))#Passed
    print(pow(5,3))#Passed
    print(pow(6,4))#Passed


def GCD(a, b):
    """
    func: GCD():
    Takes 2 positive numbers and computes the Greatest Common Divisor using the method
    of recursion.
    param1: a -> A positive number.
    param2: b -> A positive number.
    """
    if b == 0:
        return a
    if b != 0:
        return GCD(b, a % b)


def test_GCD():
    """
    test_GCD():
    Function that checks the working of the GCD function.
    """
    print(GCD(2,0))#Passed
    print(GCD(3,9))#Passed
    print(GCD(6,4))#Passed
    print(GCD(10,20))#Passed
    print(GCD(7,21))#Passed


def lcm(x, y, z):
    """
    func: lcm()
    A helper function that computes the logic of LCM function.
    """
    if (z%x == 0 and z%y == 0):
        return z
    else:
        return lcm(x, y, z+1)


def LCM(x, y):
    """
    func: LCM():
    Takes 2 positive numbers and computes the Least Common Multiple using the method
    of recursion.
    param1: x -> A positive number.
    param2: y -> A positive number.
    """
    z = 1
    return lcm(x, y, z+1)
    


def test_LCM():
    """
    test_LCM():
    Function that checks the working of the LCM function.
    """
    print(LCM(5,2))#Passed
    print(LCM(12,3))#Passed
    print(LCM(2,9))#Passed
    print(LCM(4,5))#Passed
    print(LCM(3,11))#Passed


def main():
    """
    func: main()
    Executes the program in order to produce the required outcome.
    """
    
    ##################################################
    #Uncomment the testing functions below if needed.#
    ##################################################

    """
    print("##########Testing Functions##########") 
    print("Results of test_pow() function:")
    test_pow()
    print("")
    print("Results of test_GCD() function:")
    test_GCD()
    print("")
    print("Results of test_LCM() function:")
    test_LCM()
    print("")
    print("##########Testing Functions##########")
    """

    print("")
    print("List of functions:")
    print("1. POW")
    print("2. GCD")
    print("3. LCM")

    user = str(input("Select a function(1-3 or type exit to close program):"))
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
        print("Your output would be processed as", "GCD("+str(n1)+","+str(n2)+")")
        print("Answer:", GCD(n1, n2))
        print("")
        return main()
    elif user in '3':
        print("You have selected the LCM function.")
        n1 = int(input("Enter a positive number:"))
        n2 = int(input("Enter a positive number:"))
        print("Your output would be processed as", "LCM("+str(n1)+","+str(n2)+")")
        print("Answer:", LCM(n1, n2))
        print("")
        return main()
    elif user in "exit":
        exit()


if __name__ == '__main__' :
    main()



        
