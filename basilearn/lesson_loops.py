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
        print("When you're done, type 'END' on a new line.")
        print("Example condition: count < 5\n")

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

        print("\nYour code:")
        print(code_string)
        print("\nExecuting your code...\n")

        try:
            exec(code_string)
            print("\n✅ Well done! Your while loop worked.\n")
        except IndentationError:
            print("❌ Indentation error. Check your spacing.\n")
        except SyntaxError:
            print("❌ Syntax error. Check your loop structure.\n")
        except Exception as e:
            print(f"❌ Error: {e}\n")

        again = input("Do you want to try another while loop? (yes/no): ").lower()
        if again != "yes":
            break

    # ===============================
    # SECTION 2: FOR LOOPS
    # ===============================
    print("\nSECTION 2: For Loops")
    print("A `for` loop repeats over a sequence (like a range of numbers).\n")
    print("Example:")
    print("    for i in range(5):")
    print("        print(i)\n")

    input("Press Enter to try a for loop...\n")

    while True:
        print("\nWrite a `for` loop.")
        print("When you're done, type 'END' on a new line.")
        print("Example: for i in range(1, 6):\n")

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

        print("\nYour code:")
        print(code_string)
        print("\nExecuting your code...\n")

        try:
            exec(code_string)
            print("\n✅ Great job! Your for loop worked.\n")
        except IndentationError:
            print("❌ Indentation error. Check your spacing.\n")
        except SyntaxError:
            print("❌ Syntax error. Check your loop structure.\n")
        except Exception as e:
            print(f"❌ Error: {e}\n")

        again = input("Do you want to try another for loop? (yes/no): ").lower()
        if again != "yes":
            break

    # ===============================
    # RECAP
    # ===============================
    print("\n🎉 Lesson 4 Recap: Loops")
    print("- `while` loops repeat while a condition is True.")
    print("- `for` loops repeat over a sequence.")
    print("- Indentation is very important in loops.")
    print("- Use loops to avoid repeating code.\n")
    print("Excellent work! 🚀")