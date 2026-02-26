def lesson_variables():
    print("Welcome to Lesson 1: Variables and Data Types")
    print("-------------------------------------------------")
    print("A variable is a container for storing data values.")
    print("Example:")
    print("    x = 5")
    print("    name = 'Ama'\n")
    print("Type 'exit' at any time to quit the lesson.\n")

    input("Press Enter to continue...\n")

    # ===============================
    # SECTION 1: DATA TYPES
    # ===============================
    print("Python has several basic data types:")
    print("1. Integer (int): Whole numbers (e.g., 10, -3)")
    print("2. Float (float): Decimal numbers (e.g., 3.14)")
    print("3. String (str): Text (e.g., 'Hello')\n")

    input("Press Enter to try creating variables...\n")

    defined_variables = {}

    while True:
        print("\nCreate ONE variable using the format:")
        print("name = value")
        print("Examples:")
        print("age = 20")
        print("price = 12.5")
        print("city = 'Accra'\n")

        user_input = input(">>> ").strip()

        if user_input.lower() == "exit":
            print("\n🎉 Lesson 1 Recap: Variables")
            print("- Variables store data")
            print("- Use = to assign values")
            print("- Common types: int, float, str\n")
            print("Great job! 🚀")
            return

        if "=" not in user_input or user_input.count("=") != 1:
            print("❌ You must assign exactly ONE variable using `=`.\n")
            continue

        left, right = user_input.split("=", 1)

        variable_name = left.strip()
        value_part = right.strip()

        if not variable_name.isidentifier():
            print("❌ Invalid variable name. Use letters, numbers, and underscores only.\n")
            continue

        if variable_name in defined_variables:
            print(f"❌ The variable '{variable_name}' already exists. Use a new name.\n")
            continue

        try:
            local_scope = {}
            exec(user_input, {}, local_scope)

            if len(local_scope) != 1:
                print("❌ Assign only ONE variable.\n")
                continue

            value = local_scope[variable_name]
            defined_variables[variable_name] = value

            print(f"✅ Correct!")
            print(f"Variable name : {variable_name}")
            print(f"Value         : {value}")
            print(f"Data type     : {type(value).__name__}\n")

        except SyntaxError:
            print("❌ Syntax error. Example: x = 5 or name = 'Ama'\n")
            continue
        except Exception as e:
            print(f"❌ Error: {e}\n")
            continue

        again = input("Do you want to create another variable? (yes/no): ").strip().lower()
        if again != "yes":
            print("\n🎉 Lesson 1 Complete!")
            print("- Variables store information")
            print("- Python decides the data type automatically")
            print("- You created real variables like a Python programmer!\n")
            print("Excellent work! 🚀")
            return
        
