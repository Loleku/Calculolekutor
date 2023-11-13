from fractions import Fraction
import math

def sumfunction(*sumcomponent):
    return sum(sumcomponent)

def difffunction(*diffcomponent):
    return diffcomponent[0] - diffcomponent[1]

def multiplyfunction(*multicomponent):
    return multicomponent[0] * multicomponent[1]

def divfunction(*divcomponent):
    return divcomponent[0] / divcomponent[1]

def secondpower(secondpowernum):
    return secondpowernum ** 2

def sqrt(sqrtnum):
    return math.sqrt(sqrtnum)

type1 = """
Welcome to the calculator made by Loleku.
Choose the math operation type:
1. Simple operations
"""

simpleop = """
What specific simple math operation would you like to do?
1. Sum
2. Difference
3. Multiplication
4. Division
5. Numbers to the second power
6. Numbers under the square root
"""


while True:
    try:
        print(type1)
        type1_input = float(input(">> "))

        if type1_input == 1:
            print(simpleop)
            simop_input = float(input(">> "))
            if simop_input == 1:
                while True:
                    try:
                        if 'sumcomponent1' not in locals():
                            sumcomponent1 = float(input("Input the first sum component: "))
                        else:
                            while True:
                                import_result = input("Do you want to import the result of the previous operation? Y for yes, any other string to don't: ")
                                if import_result.lower() == "y":
                                    sumcomponent1 = resultsum
                                    break
                                else:
                                    sumcomponent1 = float(input("Input the first sum component: "))
                                    break
                        sumcomponent2 = float(input("Input second sum component: "))
                        resultsum = sumfunction(sumcomponent1, sumcomponent2)
                        if sumcomponent2 >= 0:
                            print(f"{sumcomponent1} + {sumcomponent2} = {resultsum}")
                        else:
                            print(f"{sumcomponent1} + ({sumcomponent2}) = {sumcomponent1} - {abs(sumcomponent2)} = {resultsum}")
                        continuesum = input("Would you like to continue? Y for yes, any other string to exit: ")
                        if continuesum.lower() != "y":
                            break

                    except ValueError:
                        print("You inputted an incorrect value (Make sure that you provided a number)")
                        exit_input = float(input("Enter 1 to try again, or any other number to exit: "))
                        if exit_input != 1:
                            print("Exiting the program.")
                            break

            if simop_input == 2:
                while True:
                    try:
                        if 'diffcomponent1' not in locals():
                            diffcomponent1 = float(input("Input the first difference component (minuend): "))
                        else:
                            while True:
                                import_result = input("Do you want to import the result of the previous operation? Y for yes, any other string to don't: ")
                                if import_result.lower() == "y":
                                    diffcomponent1 = resultdiff
                                    break
                                else:
                                    diffcomponent1 = float(input("Input the first difference component (minuend): "))
                                    break
                        diffcomponent2 = float(input("Input the second difference component (subtrahend): "))
                        resultdiff = difffunction(diffcomponent1, diffcomponent2)
                        if diffcomponent2 >= 0:
                            print(f"{diffcomponent1} - {diffcomponent2} = {resultdiff}")
                        else:
                            print(f"{diffcomponent1} - ({diffcomponent2}) = {diffcomponent1} + {abs(diffcomponent2)} = {resultdiff}")
                        continuediff = input("Would you like to continue? Y for yes, any other string to exit: ")
                        if continuediff.lower() != "y":
                            break
                    except ValueError:
                        print("You inputted an incorrect value (Make sure that you provided a number)")
                        exit_input = float(input("Enter 1 to try again, or any other number to exit: "))
                        if exit_input != 1:
                            print("Exiting the program.")
                            break

            if simop_input == 3:
                while True:
                    try:
                        if 'multicomponent1' not in locals():
                            multicomponent1 = float(input("Input first multiply component: "))
                        else:
                            while True:
                                import_result = input("Do you want to import the result of the previous operation? Y for yes, any other string to don't: ")
                                if import_result.lower() == "y":
                                    multicomponent1 = resultmultiply
                                    break
                                else:
                                    multicomponent1 = float(input("Input first multiply component: "))
                                    break

                        multicomponent2 = float(input("Input second multiply component: "))
                        resultmultiply = multiplyfunction(multicomponent1, multicomponent2)
                        if multicomponent2 >= 0:
                            print(f"{multicomponent1} x {multicomponent2} = {resultmultiply}")
                        else:
                            print(f"{multicomponent1} x ({multicomponent2}) = {resultmultiply}")

                        continuemultiply = input("Would you like to continue? Y for yes, any other string to exit: ")
                        if continuemultiply.lower() != "y":
                            break
                    except ValueError:
                        print("You inputted an incorrect value (Make sure that you provided a number)")
                        exit_input = float(input("Enter 1 to try again, or any other number to exit: "))
                        if exit_input != 1:
                            print("Exiting program.")
                            break

            if simop_input == 4:
                while True:
                    try:
                        if 'divcomponent1' not in locals():
                            divcomponent1 = float(input("Input first division component (dividend): "))
                        else:
                            while True:
                                import_result = input("Do you want to import the result of the previous operation? Y for yes, any other string to don't: ")
                                if import_result.lower() == "y":
                                    divcomponent1 = resultdiv
                                    break
                                else:
                                    divcomponent1 = float(input("Input first multiply component: "))
                                    break
                        divcomponent2 = float(input("Input the second division component (divisor): "))
                        resultdiv = divfunction(divcomponent1, divcomponent2)
                        if divcomponent2 > 0:
                            print(f"{divcomponent1} : {divcomponent2} = {resultdiv}")
                        else:
                            print(f"{divcomponent1} : ({divcomponent2} = {resultdiv})")
                        continuediv = input("Would you like to continue? Y for yes, any other string to exit: ")
                        if continuediv.lower() != "y":
                            break
                    except ValueError or ZeroDivisionError:
                        print("You inputted an incorrect value (Make sure that you provided a number) OR You inputted zero which is theoretical impossible to divide by it.")
                        exit_input = float(input("Enter 1 to try again, or any other number to exit: "))
                        if exit_input != 1:
                            print("Exiting program.")
                            break

            if simop_input == 5:
                while True:
                    try:
                        if 'secondpowernum' not in locals():
                            secondpowernum = float(input("Input number that you want in the second power: "))
                        else:
                            while True:
                                import_result = input("Do you want to import the result of the previous operation? Y for yes, any other string to don't: ")
                                if import_result.lower() == "y":
                                    secondpowernum = secondpowerresult
                                    break
                                else:
                                    secondpowernum = float(input("Input number that you want in the second power: "))
                                    break
                        secondpowerresult = secondpower(secondpowernum)
                        print(f"{secondpowernum}^2 = {secondpowerresult}")
                        continuesecondpower = input("Would you like to continue? Y for yes, any other string to exit: ")
                        if continuesecondpower.lower() != "y":
                            break
                    except ValueError:
                        print("You inputted an incorrect value (Make sure that you provided a number)")
                        exit_input = float(input("Enter 1 to try again, or any other number to exit: "))
                        if exit_input != 1:
                            print("Exiting the program.")
                            break

            if simop_input == 6:
                while True:
                    try:
                        if 'sqrtnum' not in locals():
                            sqrtnum = float(input("Input number you want under the square root: "))
                        else:
                            while True:
                                import_result = input("Do you want to import the result of the previous operation? Y for yes, any other string to don't: ")
                                if import_result.lower() == "y":
                                    sqrtnum = sqrtresult
                                    break
                                else:
                                    sqrtnum = float(input("Input number you want under the square root: "))
                                    break
                        sqrtresult = sqrt(sqrtnum)
                        print(f"sqrt({sqrtnum}) = {sqrtresult}")
                        continuesqrt = input("Would you like to continue? Y for yes, any other string to exit: ")
                        if continuesqrt.lower() != "y":
                            break
                    except ValueError:
                        print("You inputted an incorrect value (Make sure that you provided a number)")
                        exit_input = float(input("Enter 1 to try again, or any other number to exit: "))
                        if exit_input != 1:
                            print("Exiting the program.")
                            break
    except ValueError:
        print("You inputted an incorrect value (Make sure that you provided a number)")
        exit_input = float(input("Enter 1 to try again, or any other number to exit: "))
        if exit_input != 1:
            print("Exiting the program.")
            break
