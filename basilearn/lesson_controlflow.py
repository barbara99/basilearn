def lesson_control_flow():
    print("Welcome to Lesson 3: Control Flow")
    print("-------------------------------------------------")
    print("Control flow lets your program make decisions based on conditions.")
    print("The main tools for this are `if`, `elif`, and `else` statements.\n")
    print("Type 'exit' at any time to quit the lesson.\n")

    input("Press Enter to continue...\n")

    # Section 1: `if` Statements
    print("An `if` statement allows you to execute code only if a condition is true.")
    print("Example:")
    print("    x = 10")
    print("    if x > 5:")
    print("        print('x is greater than 5')\n")

    input("Press Enter to try it yourself...\n")

    print("Now, let's try writing your own `if` statement!")
    print("You can write multi-line code. When you're done, type 'END' on a new line.")
    print("Remember: Type 'exit' to quit at any time.\n")

    while True:
        print("\nType your `if` statement below. To finish, type 'END' on a new line:")
        code_lines = []
        while True:
            line = input(">>> ").rstrip()  # Strip extra spaces, preserve indentation
            if line.lower() == "exit":
                print("\nRecap: Control flow allows programs to make decisions.")
                print("- `if`: Executes code if the condition is true.")
                print("- `elif`: Tests additional conditions if the previous ones are false.")
                print("- `else`: Executes code if all other conditions are false.\n")
                print("Thank you for completing Lesson 2!")
                return
            if line.upper() == "END":
                break
            code_lines.append(line)

        code_string = "\n".join(code_lines)
        
        # Check for empty input
        if not code_string.strip():
            print("❌ You didn't write any code. Please write an `if` statement before typing END.\n")
            continue

        print("\nYour code:")
        print(code_string)
        print("\nExecuting your code...")

        try:
            exec(code_string)
            print("✅ Great job! You successfully executed a control flow statement.\n")
        except SyntaxError as e:
            print(f"❌ Syntax error: {e}. Ensure your statement is properly formatted.\n")
        except Exception as e:
            print(f"❌ Error: {e}. Check your logic and try again!\n")

        # Ask if they want to continue experimenting
        continue_experimenting = input("Do you want to try another statement? (yes/no): ").strip().lower()
        if continue_experimenting != 'yes':
            print("\nRecap: Control flow allows programs to make decisions.")
            print("- `if`: Executes code if the condition is true.")
            print("- `elif`: Tests additional conditions if the previous ones are false.")
            print("- `else`: Executes code if all other conditions are false.\n")
            print("Thank you for completing Lesson 3!")
            return