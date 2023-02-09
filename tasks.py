# We use operators to manipulate the value of operands (Values/Variables)
# Types of operators
# 1. Arithmetic operators (+,-,/,*,%,**,//)
# 2. Comparison operators (>,<,<=,>=,!=,==)
# 3. Assignment Operators (=,+=,-=,*=,%=,**=,//=)
# 4. Logical Operators (and,or,not)
# # week 2
# others , membership operators / bitwise / identity operators

#COMPARISON OPERATORS
#  ==  Equal  4==5  false. 4 == 4 true
#!=  Not Equal 4!= 5 true
#>  greater than 4 > 5 false. 5 > 4  true
#<  less than 4 < 5  true
#>= Greater than or equal to




a = 4
b = 5
#equal
print("a == b: ", a == b)

#Not eqaul
print("a != b", a != b)

# Greater than
print("a > b", a > b)

#Less Than
print("a < b", a < b)

# Greater than or Equal to
print("a >= b", a >= b)

#Less than
print("a <= b", a <= b)

#Assignment Operators
#  =   Assignment operator  a = 10
#  +=  Addition Assignment  a += 5 (same as a
#  Subtraction Assignment
# Multiplication Assignment
# Division Assignment
#  Remainder Assignment
# Exponentation Assignment
# Floor Division Assignment


a = 10

print("a += 5: ", a)

print("a -= 5: ", a)

print("a *= 5: ", a)

print("a /= 5: ", a)

print("a %= 5: ", a)

print("a **= 5: ", a)

print("a //= 5: ", a)


# Logical operators
# and Logica AND   if both operators are true then condition becomes true AND&&
# or Logical OR   if any of the two operands are non- zero the condition becomes true OR ||
# not Logical NOT   used to reverse the logical state of its operand !

# Conditionals or Control flow statements are used together with logical operators
# If ... ELSE ... statement
# if condition:
#      # code to execute if condition is true
# else:
#     # code to execute if condition is false

variableCompare = 5
secondVariable = 10

if variableCompare == 10:
    print("simple if")
else:
    print("condition not met")

if variableCompare == 10:
    print("from multi-conditional")
elif variableCompare == 7:
    print("from the multi-conditional")
elif variableCompare == 7:
    print("from the multi-conditional")
else:
    print("none meet condition")




if variableCompare == 10 or secondVariable == 6:
    print("from or")
elif variableCompare == 5 and secondVariable == 10:
    print("from and")
else:
    print("No condition met")




if 'age:' > 18:
    print("Too young")

elif "age" > 18 and "gender" == female:
    print("Go in and have drink." )
else:
    print("go in but no drink")