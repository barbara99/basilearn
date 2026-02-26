def lesson_control_flow():
    print("Welcome to Lesson 3: Control Flow")
    print("-------------------------------------------------")
    print("Control flow lets your program make decisions based on conditions.")
    print("The main tools for this are `if`, `elif`, and `else` statements.\n")
    print("Type 'exit' at any time to quit the lesson.\n")

    input("Press Enter to continue...\n")

    # ===============================
    # SECTION 1: IF STATEMENTS
    # ===============================
    print("SECTION 1: `if` Statements")
    print("An `if` statement allows your program to run code only if a condition is true.\n")
    print("Example:")
    print("    x = 10")
    print("    if x > 5:")
    print("        print('x is greater than 5')\n")

    input("Press Enter to try writing your own `if` statement...\n")

    while True:
        print("\nWrite an `if` statement.")
        print("• You MUST use `if`")
        print("• Include a condition")
        print("• Indent the code inside the if block")
        print("• Type 'END' on a new line when done\n")

        code_lines = []

        while True:
            line = input(">>> ")
            if line.lower() == "exit":
                print("\nLesson ended. Great job learning control flow!")
                return
            if line.upper() == "END":
                break
            code_lines.append(line)

        code_string = "\n".join(code_lines)

        # Empty input check
        if not code_string.strip():
            print("❌ You didn't write any code. Please try again.\n")
            continue

        # Must contain if
        if "if " not in code_string:
            print("❌ Your code must include an `if` statement.\n")
            continue

        print("\nYour code:")
        print(code_string)
        print("\nExecuting your code...\n")

        try:
            exec(code_string, {})
            print("✅ Great! Your `if` statement works correctly.\n")
        except IndentationError:
            print("❌ Indentation error. Remember to indent code inside `if`.\n")
            continue
        except SyntaxError as e:
            print(f"❌ Syntax error: {e}. Check your condition and colon usage.\n")
            continue
        except Exception as e:
            print(f"❌ Runtime error: {e}. Check your logic.\n")
            continue

        again = input("Do you want to try another `if` statement? (yes/no): ").lower()
        if again != "yes":
            break

    # ===============================
    # SECTION 2: IF / ELSE
    # ===============================
    print("\nSECTION 2: `if` / `else`")
    print("An `else` block runs when the `if` condition is false.\n")
    print("Example:")
    print("    age = 15")
    print("    if age >= 18:")
    print("        print('Adult')")
    print("    else:")
    print("        print('Minor')\n")

    input("Press Enter to try `if` with `else`...\n")

    while True:
        print("\nWrite an `if` statement WITH an `else`.")
        print("• Use `if` and `else`")
        print("• Indent correctly")
        print("• Type 'END' when done\n")

        code_lines = []

        while True:
            line = input(">>> ")
            if line.lower() == "exit":
                print("\nLesson ended. Great job learning control flow!")
                return
            if line.upper() == "END":
                break
            code_lines.append(line)

        code_string = "\n".join(code_lines)

        if not code_string.strip():
            print("❌ You didn't write any code. Please try again.\n")
            continue

        if "if " not in code_string or "else:" not in code_string:
            print("❌ Your code must include BOTH `if` and `else`.\n")
            continue

        print("\nExecuting your code...\n")

        try:
            exec(code_string, {})
            print("✅ Excellent! Your `if/else` logic works.\n")
        except IndentationError:
            print("❌ Indentation error. Check spacing inside blocks.\n")
            continue
        except SyntaxError as e:
            print(f"❌ Syntax error: {e}\n")
            continue
        except Exception as e:
            print(f"❌ Error: {e}\n")
            continue

        again = input("Do you want to try another one? (yes/no): ").lower()
        if again != "yes":
            break

    # ===============================
    # SECTION 3: IF / ELIF / ELSE
    # ===============================
    print("\nSECTION 3: `if` / `elif` / `else`")
    print("Use `elif` to check multiple conditions.\n")
    print("Example:")
    print("    score = 75")
    print("    if score >= 80:")
    print("        print('A')")
    print("    elif score >= 70:")
    print("        print('B')")
    print("    else:")
    print("        print('C')\n")

    input("Press Enter to try all three...\n")

    while True:
        print("\nWrite a program using `if`, `elif`, and `else`.")
        print("• Must include all three")
        print("• Type 'END' when done\n")

        code_lines = []

        while True:
            line = input(">>> ")
            if line.lower() == "exit":
                print("\nLesson ended. Great job learning control flow!")
                return
            if line.upper() == "END":
                break
            code_lines.append(line)

        code_string = "\n".join(code_lines)

        if not code_string.strip():
            print("❌ You didn't write any code.\n")
            continue

        if "if " not in code_string or "elif" not in code_string or "else:" not in code_string:
            print("❌ Your code must include `if`, `elif`, and `else`.\n")
            continue

        print("\nExecuting your code...\n")

        try:
            exec(code_string, {})
            print("✅ Fantastic! You used full control flow correctly.\n")
        except IndentationError:
            print("❌ Indentation error.\n")
            continue
        except SyntaxError as e:
            print(f"❌ Syntax error: {e}\n")
            continue
        except Exception as e:
            print(f"❌ Error: {e}\n")
            continue

        again = input("Do you want to try again? (yes/no): ").lower()
        if again != "yes":
            break

    # ===============================
    # RECAP
    # ===============================
    print("\n🎉 Lesson 3 Recap: Control Flow")
    print("- `if` runs code when a condition is true.")
    print("- `else` runs when the condition is false.")
    print("- `elif` allows multiple conditions.")
    print("- Indentation is VERY important in Python.\n")
    print("Great work! 🚀")
    
