def lesson_loops():
    print("Welcome to Lesson 4: Loops")
    print("-------------------------------------------------")
    print("Loops allow your program to repeat actions.")
    print("The main types of loops in Python are `while` and `for`.\n")
    print("Type 'exit' at any time to quit the lesson.\n")

    input("Press Enter to continue...\n")

    # ===============================
    # SECTION 1: WHILE LOOPS
    # ===============================
    print("SECTION 1: While Loops")
    print("A `while` loop repeats as long as a condition is True.\n")
    print("Example:")
    print("    count = 1")
    print("    while count <= 3:")
    print("        print(count)")
    print("        count += 1\n")

    input("Press Enter to try a while loop...\n")

    while True:
        print("\nWrite a `while` loop.")
        print("• You MUST use `while`")
        print("• Include a condition")
        print("• Update the condition variable (to avoid infinite loops)")
        print("• Type 'END' on a new line when done\n")

        code_lines = []

        while True:
            line = input(">>> ")
            if line.lower() == "exit":
                print("\nLesson ended. Great job learning loops!")
                return
            if line.upper() == "END":
                break
            code_lines.append(line)

        code_string = "\n".join(code_lines)

        if not code_string.strip():
            print("❌ You didn't write any code. Please try again.\n")
            continue

        if "while " not in code_string:
            print("❌ Your code must include a `while` loop.\n")
            continue

        print("\nYour code:")
        print(code_string)
        print("\nExecuting your code...\n")

        try:
            exec(code_string, {})
            print("✅ Well done! Your `while` loop worked correctly.\n")
        except IndentationError:
            print("❌ Indentation error. Remember to indent code inside the loop.\n")
            continue
        except SyntaxError as e:
            print(f"❌ Syntax error: {e}. Check your condition and colon usage.\n")
            continue
        except Exception as e:
            print(f"❌ Runtime error: {e}. Check your logic.\n")
            continue

        again = input("Do you want to try another while loop? (yes/no): ").lower()
        if again != "yes":
            break

    # ===============================
    # SECTION 2: FOR LOOPS
    # ===============================
    print("\nSECTION 2: For Loops")
    print("A `for` loop repeats over a sequence (like a list or range).\n")
    print("Example:")
    print("    for i in range(5):")
    print("        print(i)\n")

    input("Press Enter to try a for loop...\n")

    while True:
        print("\nWrite a `for` loop.")
        print("• You MUST use `for`")
        print("• Loop over a sequence (range, list, string, etc.)")
        print("• Indent correctly")
        print("• Type 'END' on a new line when done\n")

        code_lines = []

        while True:
            line = input(">>> ")
            if line.lower() == "exit":
                print("\nLesson ended. Great job learning loops!")
                return
            if line.upper() == "END":
                break
            code_lines.append(line)

        code_string = "\n".join(code_lines)

        if not code_string.strip():
            print("❌ You didn't write any code. Please try again.\n")
            continue

        if "for " not in code_string:
            print("❌ Your code must include a `for` loop.\n")
            continue

        print("\nYour code:")
        print(code_string)
        print("\nExecuting your code...\n")

        try:
            exec(code_string, {})
            print("✅ Great job! Your `for` loop worked correctly.\n")
        except IndentationError:
            print("❌ Indentation error. Check spacing inside the loop.\n")
            continue
        except SyntaxError as e:
            print(f"❌ Syntax error: {e}. Check your loop structure.\n")
            continue
        except Exception as e:
            print(f"❌ Runtime error: {e}. Check your logic.\n")
            continue

        again = input("Do you want to try another for loop? (yes/no): ").lower()
        if again != "yes":
            break

    # ===============================
    # RECAP
    # ===============================
    print("\n🎉 Lesson 4 Recap: Loops")
    print("- `while` loops repeat while a condition is true.")
    print("- `for` loops repeat over a sequence.")
    print("- Always update loop conditions to avoid infinite loops.")
    print("- Indentation controls what runs inside the loop.\n")
    print("Excellent work! 🚀")
    
    
