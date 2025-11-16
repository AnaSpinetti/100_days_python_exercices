result = 0
first_number = input("Enter first number: ")
continue_calculation = 'y'

while continue_calculation == 'y':
    operator = input("Enter operator (+, -, *, /): ")

    if operator not in ['+', '-', '*', '/']:
        print("Invalid operator. Please try again.")
        continue

    next_number = input("Enter second number: ")

    if continue_calculation == 'y':
        match operator:
            case '+':
                result = float(first_number) + float(next_number)
            case '-':
                result = float(first_number) - float(next_number)
            case '*':
                result = float(first_number) * float(next_number)
            case '/':
                if float(next_number) == 0:
                    print("Cannot divide by zero.")
                    continue
                result = float(first_number) / float(next_number)
            

        continue_calculation = input("Do you want to continue with the result? Press 'y' to continue or 'n' to exit: ")
    if continue_calculation == 'y':
            first_number = result
    print(result)