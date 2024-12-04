def lesson_operators():
    print("Welcome to Lesson 2: Operators and Basic Math Operations")
    print("---------------------------------------------------------")
    print("In Python, operators are used to perform operations on variables and values.\n")
    print("We'll cover the following types of operators:")
    print("1. Arithmetic Operators (addition, subtraction, etc.)")
    print("2. Comparison Operators (checking equality, greater than, etc.)")
    print("3. Logical Operators (combining conditions)\n")
    print("Type 'exit' at any time to quit the lesson.\n")

    input("Press Enter to continue...\n")

    # Section 1: Arithmetic Operators
    print("### Arithmetic Operators ###")
    print("These operators are used to perform basic math operations.")
    print("1. Addition (+): Adds two values.")
    print("2. Subtraction (-): Subtracts the right value from the left.")
    print("3. Multiplication (*): Multiplies two values.")
    print("4. Division (/): Divides the left value by the right.")
    print("5. Modulus (%): Returns the remainder of a division.")
    print("6. Exponentiation (**): Raises a number to the power of another.")
    print("7. Floor Division (//): Divides and returns the quotient without the remainder.\n")

    input("Press Enter to continue...\n")

    # Section 2: Comparison Operators
    print("### Comparison Operators ###")
    print("These operators are used to compare two values.")
    print("1. Equal to (==): Checks if two values are equal.")
    print("2. Not equal to (!=): Checks if two values are not equal.")
    print("3. Greater than (>): Checks if the left value is greater than the right.")
    print("4. Less than (<): Checks if the left value is less than the right.")
    print("5. Greater than or equal to (>=): Checks if the left value is greater than or equal to the right.")
    print("6. Less than or equal to (<=): Checks if the left value is less than or equal to the right.\n")

    input("Press Enter to continue...\n")

    # Section 3: Logical Operators
    print("### Logical Operators ###")
    print("These operators are used to combine conditional statements.")
    print("1. AND: Returns True if both conditions are true.")
    print("2. OR: Returns True if at least one condition is true.")
    print("3. NOT: Reverses the result, returns True if the condition is false.\n")

    input("Press Enter to continue...\n")

    # Interactive Example
    print("Let's experiment with some operators! You can type expressions using the operators we just learned.")
    print("For example, you can try:")
    print("    5 + 3  (Addition)")
    print("    10 > 5 (Comparison)")
    print("    True and False (Logical)\n")

    while True:
        user_input = input("Type an expression below (e.g., 5 + 3 or 10 > 5) or 'exit' to quit: ").strip()

        if user_input.lower() == 'exit':
            print("\nRecap: We covered the following operators:")
            print("- Arithmetic: +, -, *, /, %, **, //")
            print("- Comparison: ==, !=, >, <, >=, <=")
            print("- Logical: and, or, not\n")
            print("Thank you for completing Lesson 2!")
            print("\nExiting the lesson. Goodbye!")
            break  # Exit the loop when 'exit' is typed

        try:
            result = eval(user_input)  # Evaluate the expression safely
            print(f"✅ The result of '{user_input}' is: {result}\n")

            # Ask the user if they want to try another example
            continue_example = input("Do you want to try another example? (yes/no): ").strip().lower()
            if continue_example != 'yes':
                print("\nRecap: We covered the following operators:")
                print("- Arithmetic: +, -, *, /, %, **, //")
                print("- Comparison: ==, !=, >, <, >=, <=")
                print("- Logical: and, or, not\n")
                print("Thank you for completing Lesson 2!")
                print("\nExiting the lesson. Goodbye!")
                break  # Exit the loop if the user doesn't want to try another example
        except Exception as e:
            print(f"❌ Error: {e}. Please ensure you're using the correct syntax and try again.\n")



def lesson_operators():
    print("Welcome to Lesson 2: Operators and Basic Math Operations")
    print("---------------------------------------------------------")
    print("In Python, operators are used to perform operations on variables and values.\n")
    print("We'll cover the following types of operators:")
    print("1. Arithmetic Operators (addition, subtraction, etc.)")
    print("2. Comparison Operators (checking equality, greater than, etc.)")
    print("3. Logical Operators (combining conditions)\n")
    print("Type 'exit' at any time to quit the lesson.\n")

    input("Press Enter to continue...\n")

    # Section 1: Arithmetic Operators
    print("### Arithmetic Operators ###")
    print("These operators are used to perform basic math operations.")
    print("1. Addition (+): Adds two values.")
    print("2. Subtraction (-): Subtracts the right value from the left.")
    print("3. Multiplication (*): Multiplies two values.")
    print("4. Division (/): Divides the left value by the right.")
    print("5. Modulus (%): Returns the remainder of a division.")
    print("6. Exponentiation (**): Raises a number to the power of another.")
    print("7. Floor Division (//): Divides and returns the quotient without the remainder.\n")

    input("Press Enter to continue...\n")

    # Section 2: Comparison Operators
    print("### Comparison Operators ###")
    print("These operators are used to compare two values.")
    print("1. Equal to (==): Checks if two values are equal.")
    print("2. Not equal to (!=): Checks if two values are not equal.")
    print("3. Greater than (>): Checks if the left value is greater than the right.")
    print("4. Less than (<): Checks if the left value is less than the right.")
    print("5. Greater than or equal to (>=): Checks if the left value is greater than or equal to the right.")
    print("6. Less than or equal to (<=): Checks if the left value is less than or equal to the right.\n")

    input("Press Enter to continue...\n")

    # Section 3: Logical Operators
    print("### Logical Operators ###")
    print("These operators are used to combine conditional statements.")
    print("1. AND: Returns True if both conditions are true.")
    print("2. OR: Returns True if at least one condition is true.")
    print("3. NOT: Reverses the result, returns True if the condition is false.\n")

    input("Press Enter to continue...\n")

    # Interactive Example
    print("Let's experiment with some operators! You can type expressions using the operators we just learned.")
    print("For example, you can try:")
    print("    5 + 3  (Addition)")
    print("    10 > 5 (Comparison)")
    print("    True and False (Logical)\n")

    while True:
        user_input = input("Type an expression below (e.g., 5 + 3 or 10 > 5) or 'exit' to quit: ").strip()

        if user_input.lower() == 'exit':
            print("\nRecap: We covered the following operators:")
            print("- Arithmetic: +, -, *, /, %, **, //")
            print("- Comparison: ==, !=, >, <, >=, <=")
            print("- Logical: and, or, not\n")
            print("Thank you for completing Lesson 2!")
            print("\nExiting the lesson. Goodbye!")
            break  # Exit the loop when 'exit' is typed

        try:
            result = eval(user_input)  # Evaluate the expression safely
            print(f"✅ The result of '{user_input}' is: {result}\n")

            # Ask the user if they want to try another example
            continue_example = input("Do you want to try another example? (yes/no): ").strip().lower()
            if continue_example != 'yes':
                print("\nRecap: We covered the following operators:")
                print("- Arithmetic: +, -, *, /, %, **, //")
                print("- Comparison: ==, !=, >, <, >=, <=")
                print("- Logical: and, or, not\n")
                print("Thank you for completing Lesson 2!")
                print("\nExiting the lesson. Goodbye!")
                break  # Exit the loop if the user doesn't want to try another example
        except Exception as e:
            print(f"❌ Error: {e}. Please ensure you're using the correct syntax and try again.\n")



