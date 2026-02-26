def lesson_operators():
    print("Welcome to Lesson 2: Operators and Basic Math Operations")
    print("---------------------------------------------------------")
    print("Operators let Python perform calculations and comparisons.\n")
    print("We will practice:")
    print("1. Arithmetic operators")
    print("2. Comparison operators")
    print("3. Logical operators\n")
    print("Type 'exit' at any time to quit.\n")

    input("Press Enter to continue...\n")

    # ===============================
    # SECTION 1: ARITHMETIC OPERATORS
    # ===============================
    print("SECTION 1: Arithmetic Operators")
    print("Examples: +  -  *  /  %  **  //\n")
    print("Task:")
    print("• Write a math expression using at least ONE arithmetic operator")
    print("• Example: 5 + 3\n")

    while True:
        user_input = input(">>> ").strip()

        if user_input.lower() == "exit":
            print("\nLesson ended. Goodbye!")
            return

        if not user_input:
            print("❌ You didn't enter anything.\n")
            continue

        if not any(op in user_input for op in ["+", "-", "*", "/", "%", "**", "//"]):
            print("❌ Your expression must include an arithmetic operator.\n")
            continue

        try:
            result = eval(user_input, {})
            print(f"✅ Correct! Result: {result}\n")
            break
        except Exception as e:
            print(f"❌ Error: {e}\n")

    # ===============================
    # SECTION 2: COMPARISON OPERATORS
    # ===============================
    print("\nSECTION 2: Comparison Operators")
    print("Examples: ==  !=  >  <  >=  <=\n")
    print("Task:")
    print("• Write a comparison expression")
    print("• The result must be True or False")
    print("• Example: 10 > 5\n")

    while True:
        user_input = input(">>> ").strip()

        if user_input.lower() == "exit":
            print("\nLesson ended. Goodbye!")
            return

        if not any(op in user_input for op in ["==", "!=", ">", "<", ">=", "<="]):
            print("❌ You must use a comparison operator.\n")
            continue

        try:
            result = eval(user_input, {})
            if isinstance(result, bool):
                print(f"✅ Correct! Result: {result}\n")
                break
            else:
                print("❌ Your expression must return True or False.\n")
        except Exception as e:
            print(f"❌ Error: {e}\n")

    # ===============================
    # SECTION 3: LOGICAL OPERATORS
    # ===============================
    print("\nSECTION 3: Logical Operators")
    print("Examples: and  or  not\n")
    print("Task:")
    print("• Write an expression using a logical operator")
    print("• Example: 10 > 5 and 3 < 7\n")

    while True:
        user_input = input(">>> ").strip()

        if user_input.lower() == "exit":
            print("\nLesson ended. Goodbye!")
            return

        if not any(op in user_input for op in ["and", "or", "not"]):
            print("❌ You must use a logical operator (and / or / not).\n")
            continue

        try:
            result = eval(user_input, {})
            if isinstance(result, bool):
                print(f"✅ Excellent! Result: {result}\n")
                break
            else:
                print("❌ Logical expressions should return True or False.\n")
        except Exception as e:
            print(f"❌ Error: {e}\n")

    # ===============================
    # RECAP
    # ===============================
    print("\n🎉 Lesson 2 Recap: Operators")
    print("- Arithmetic operators perform calculations")
    print("- Comparison operators compare values")
    print("- Logical operators combine conditions")
    print("- Operators are the foundation of decision-making in Python\n")
    print("Great work! 🚀")
    
