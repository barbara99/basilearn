def lesson_functions():
    print("Welcome to Lesson 5: Functions")
    print("-------------------------------------------------")
    print("Functions help you group code so you can reuse it.")
    print("They make programs cleaner, shorter, and easier to understand.\n")
    print("Type 'exit' at any time to quit the lesson.\n")

    input("Press Enter to continue...\n")

    # ===============================
    # SECTION 1: WHAT IS A FUNCTION?
    # ===============================
    print("SECTION 1: What is a Function?")
    print("A function is a block of code that runs only when it is called.\n")
    print("Example:")
    print("    def greet():")
    print("        print('Hello!')\n")
    print("    greet()\n")

    input("Press Enter to try creating a function...\n")

    while True:
        print("\nWrite a simple function.")
        print("• Use def")
        print("• Call the function after defining it")
        print("• Type 'END' on a new line when done\n")

        code_lines = []

        while True:
            line = input(">>> ")
            if line.lower() == "exit":
                print("\nLesson ended. Great job learning functions!")
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
            print("\n✅ Nice! Your function worked.\n")
        except IndentationError:
            print("❌ Indentation error. Check your spacing.\n")
        except SyntaxError:
            print("❌ Syntax error. Remember to use def and proper colons.\n")
        except Exception as e:
            print(f"❌ Error: {e}\n")

        again = input("Do you want to try another function? (yes/no): ").lower()
        if again != "yes":
            break

    # ===============================
    # SECTION 2: FUNCTIONS WITH PARAMETERS
    # ===============================
    print("\nSECTION 2: Functions with Parameters")
    print("Functions can receive values (called parameters).\n")
    print("Example:")
    print("    def greet(name):")
    print("        print('Hello', name)\n")
    print("    greet('Ama')\n")

    input("Press Enter to try a function with parameters...\n")

    while True:
        print("\nWrite a function that takes at least ONE parameter.")
        print("Call the function with a value.")
        print("Type 'END' when done.\n")

        code_lines = []

        while True:
            line = input(">>> ")
            if line.lower() == "exit":
                print("\nLesson ended. Great job learning functions!")
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
            print("\n✅ Excellent! Your function with parameters worked.\n")
        except IndentationError:
            print("❌ Indentation error. Check your spacing.\n")
        except SyntaxError:
            print("❌ Syntax error. Check function definition and call.\n")
        except Exception as e:
            print(f"❌ Error: {e}\n")

        again = input("Do you want to try another one? (yes/no): ").lower()
        if again != "yes":
            break

    # ===============================
    # SECTION 3: RETURN VALUES
    # ===============================
    print("\nSECTION 3: Returning Values")
    print("Functions can send values back using `return`.\n")
    print("Example:")
    print("    def add(a, b):")
    print("        return a + b\n")
    print("    result = add(3, 4)")
    print("    print(result)\n")

    input("Press Enter to try a function with return...\n")

    while True:
        print("\nWrite a function that RETURNS a value.")
        print("Store the result in a variable and print it.")
        print("Type 'END' when done.\n")

        code_lines = []

        while True:
            line = input(">>> ")
            if line.lower() == "exit":
                print("\nLesson ended. Great job learning functions!")
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
            print("\n✅ Awesome! Your function returned a value correctly.\n")
        except IndentationError:
            print("❌ Indentation error. Check your spacing.\n")
        except SyntaxError:
            print("❌ Syntax error. Check return statement.\n")
        except Exception as e:
            print(f"❌ Error: {e}\n")

        again = input("Do you want to try another one? (yes/no): ").lower()
        if again != "yes":
            break

    # ===============================
    # RECAP
    # ===============================
    print("\n🎉 Lesson 5 Recap: Functions")
    print("- Functions help you reuse code.")
    print("- Use `def` to define a function.")
    print("- Functions can take parameters.")
    print("- Functions can return values.")
    print("- Indentation is very important.\n")
    print("Great work! 🚀")


