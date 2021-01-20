import random

'''
Saad 
TINST 310: Assignment 3
Deal or No Deal?
11/29/2020
it should be loop that iterates 10 times
each time it asks the user to enter the number and then store the number from amount_list and the case number in dict
3,5,7,and 9th iteration it asks accept the deal. The deal is calculated: 
(the sum of all values - the sum of values picked)/the quality of unpicked values
the game ends when uer picks deal then it shows the case value that the user could won
otherwise the user see the 9th case and the 10th
'''
amount_list = [1, 100, 500, 1000, 10000, 25000, 100000, 250000, 500000, 1000000]
all_sum = sum(amount_list)
cases = {}  # this dict is used for all picked numbers and their indexes from amount_list
random.shuffle(amount_list)  # shuffled list


def input_valid():
    # this function validates the input
    while True:
        inp = input('Enter your number:')  # ask the user for input
        try:  # try if its integer
            inp = int(inp)
        except ValueError:  # if not numeric rise error
            print('Please use numeric digits.')
            continue  # skip it
        if inp < 0 or inp > 9:  # if in the index range
            print('Please enter number in the scope.')
            continue # skip it
        elif inp in cases: # if already picked
            print("Please use the new number in the range")
            print("You already used ", list(cases.keys()))
            continue  # skip it
        break  # if the number passed all validation checks
    return inp


def deal():
    # this function calculates the deal
    quantity = len(amount_list) - len(cases) # quantity of all unpicked numbers equals: length of the list - length of the dict
    result = (all_sum - sum(cases.values())) / quantity
    print(str(result) + " = (" + str(all_sum) + " - " + str(sum(cases.values())) + ") / " + str(quantity))  # helpful output
    return "$"+"{:.2f}".format(result)


def interface():
    # the user enters 1 to 10 so we need index
    index = input_valid()  # we call validation of input function
    number = amount_list[index]  # the number is the number at specific index from list. This is validated iser decision
    cases[index] = number  # add this number and index to the dictionary
    return number


def ask_ok(prompt, retries=4, reminder="Please try again"):
    #  standart user asking function. No explanation needed. I took it from the official python tutorial
    while True:
        ok = input(prompt)
        if ok in ('y','ye','yes'):
            return True
        if ok in ('n','no','nop','nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('Invalid user response')
        print(reminder)


def final_output(out, value):  
    # this function prints final output 
    if out: # if the user accepted the deal
        print("User could won ", value) # amout that could be won if the user accepted the deal
        print("The User won", deal())
    else:
        print("The User won", value)


def game():
    # this function is the game mechanic
    print("this is sorted list", amount_list)
    flag = False  # this flag shows that the user did not choose deal
    print()
    for i in range(1, 10):  # it makes 10 moves
        print("counter = ", i)
        case_value = interface()  # this statement calls interface to ask the user for input and put it in the dictionary of the used numbers
        print("this is the new case dictionary after add", cases)
        if i == 3 or i == 5 or i == 7 or i == 9:  # every 3,5,7,9 move it asks the user for a deal wich is calculated with deal function
            print("The deal is: ", deal())
            if ask_ok("Do you want to accept the deal?"):  # if ask_ok function returns True then we break and finist the game
                flag = True  # since the user chose deal, we change to true
                break
    final_output(flag, case_value)


game()
