import re

print("Building a Calculator Project")
print("Type 'quit' to exit\n")

#input_number = 0
prev_number = 0
run = True

def calculate():
    global run
    #global input_number
    global prev_number
    equation = ""


    if prev_number == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(prev_number))


    if equation == 'quit':
        print("Goodbye")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)

        if prev_number == 0:
            #input_number = equation
            prev_number = eval(equation)
        else:
            #input_number = equation
            prev_number = eval(str(prev_number) + equation)

        #print("You typed", "'", input_number, "'", "the result is", prev_number)

while run:
    calculate()

