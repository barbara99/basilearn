from lesson_operators import lesson_operators as op_lesson
from lesson_variables import lesson_variables as var_lesson

class Basilearn:
    def __call__(self):
        print("Welcome to the Python Learning Program!\n")
        
        while True:
            print("Choose a lesson to start:")
            print("1. Lesson 1: Variables and Data Types")
            print("2. Lesson 2: Operators and Expressions")
            print("3. Exit the program")

            choice = input("Enter the number of your choice: ").strip()

            if choice == '1':
                op_lesson()  # Call Lesson 1
            elif choice == '2':
                var_lesson()  # Call Lesson 2
            elif choice == '3':
                print("Thank you for using the Python Learning Program! Goodbye!")
                break  # Exit the program
            else:
                print("Invalid choice. Please enter 1, 2, or 3.\n")
