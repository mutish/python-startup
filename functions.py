# Functions is simply a block of organized & reusable code that is used to perform a single, related action
# How to define a function in python
# 1. Are defined using the keyword def
# 2. Followed by a function name
# 3. Followed by a set of parentheses()
# 4. def checkout e.g
# 5. Function need to be called inorder for the code to be executed
# 6. to call the function we use the name of the function followed by a set of parentheses.

def checkout():
    #write the logic / block of code that the function should run
    # to end a function we use the RETURN keyword
    message = print("Hello from checkout")
    return message # final output of the function on call.
checkout()  #call to function

# 7. Functions can have parameters (info. that a function needs in its code execution)
# define a function with parameters

message = "hello from user"
def greeting_from_user(greet):
    print(greet)
    return

greeting_from_user(message)
def simple_add(num1,num2):
    print(int(num1) + int(num2))
    return

simple_add(1,1)

def default_arguments(num1,num2 = 1):
    division = (int(num1) / int(num2))
    print(int(division))
    return

default_arguments(20,10)

result = 0
def sum(num1,num2):
    message_local = "the operation result is"
    result = num1 + num2
    print(message_local + str(result))
    return result
def division(num1,num2):
    result = num1 / num2
    print(str(result))
    return result

sum(10,10)
division(10,10)

#ANONYMOUS FUNCTIONS
# created using the lambda keyword
# can take a number of arguments but can only return one value in the form of an expression
# print methods cannt be used directly when writing the lambda functions
# only access global variables and listed parameters
# lambda [arg.arg,arg] : expression
# to work well, store the lambda function inside a variables


sum = lambda num1, num2: num1 + num2
print("value of", sum(10,10))


def check_in(age = 12,gender = "male"):
    if age <= 17:
        print("Too young")
        return
    elif  age >= 18 and gender == "female":
        print(" go in and have a free drink.It's Ladies Night")
        return
    elif age >= 18 and gender == "male":
        print("go in but no free drink")
    else:
        print("invalid")
        return
age = int(input(" Enter your Age "))
gender = input(" Enter your gender(male,female)")

print(check_in(age,gender))

# elif age >= 18 and gender == "male"
# print("can go but no drink")
# else:
# print("invalid")
#     return
