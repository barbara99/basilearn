def lesson_variables():
    print("Welcome to Lesson 1: Variables and Data Types")
    print("-------------------------------------------------")
    print("A variable is a container for storing data values. In Python, you can assign a value to a variable like this:")
    print("    x = 5")
    print("    y = 'Hello'")
    print("Variables can hold different types of data, like numbers or text.\n")
    print("Type 'exit' at any time to quit the lesson.\n")

    input("Press Enter to continue...\n")

    # Section 1: Data Types
    print("Python has several basic data types:")
    print("1. Integer (int): Whole numbers, e.g., 10, -3")
    print("2. Float: Decimal numbers, e.g., 3.14, -0.01")
    print("3. String (str): Text, e.g., 'Hello', 'Python'\n")

    input("Press Enter to continue...\n")

    # Interactive example
    print("Let's try creating a variable!")
    print("Remember: Type 'exit' to quit at any time.\n")

    defined_variables = {}  # Track defined variables

    while True:
        print("\nType a variable assignment below (e.g., name = 'John' or num = 30):")
        user_input = input(">>> ").strip()  # Get user input

        if user_input.lower() == 'exit':
            print("\nRecap: A variable stores a value, and you assign it using the `=` operator. Different types include:")
            print("- Integer (int): Whole numbers (e.g., 10)")
            print("- Float: Decimal numbers (e.g., 3.14)")
            print("- String (str): Text (e.g., 'Python')\n")
            print("Thank you for completing Lesson 1!")

            print("\nExiting the lesson. Goodbye!")

            return  # Exit the function

        # Check if input format looks like variable assignment
        if "=" not in user_input or user_input.count("=") > 1:
            print("❌ Please assign only one variable in the format `name = value`.\n")
            continue

        try:
            local_scope = {}  # Local scope for the exec function
            exec(user_input, {}, local_scope)  # Execute the input safely

            # Ensure exactly one variable was assigned
            if len(local_scope) == 1:
                variable_name, value = next(iter(local_scope.items()))  # Get the variable name and value

                # Check if variable already exists
                if variable_name in defined_variables:
                    print(f"❌ Oops! The variable '{variable_name}' has already been assigned. Try using a different name.")
                else:
                    defined_variables[variable_name] = value
                    print(f"✅ Great! You've assigned the variable '{variable_name}' with the value: {value}")
                    print(f"🔍 The value '{value}' is of type: {type(value).__name__}\n")

                    # Ask if the user wants to continue
                    continue_experimenting = input("Do you want to assign another variable? (yes/no): ").strip().lower()
                    if continue_experimenting != 'yes':
                        print("\nRecap: A variable stores a value, and you assign it using the `=` operator. Different types include:")
                        print("- Integer (int): Whole numbers (e.g., 10)")
                        print("- Float: Decimal numbers (e.g., 3.14)")
                        print("- String (str): Text (e.g., 'Python')\n")
                        print("Thank you for completing Lesson 1!")

                        print("\nExiting the lesson. Goodbye!")
                        return
            else:
                print("❌ It looks like you didn't assign a single variable. Try again!\n")
        except SyntaxError as e:
            print(f"❌ Syntax error: {e}. Ensure you're using the correct format, like `num = 5`.\n")
        except Exception as e:
            print(f"❌ Error: {e}. Make sure you're using the correct format and try again!\n")