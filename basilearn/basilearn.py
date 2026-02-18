from basilearn.lesson_operators import lesson_operators as op_lesson
from basilearn.lesson_variables import lesson_variables as var_lesson
from basilearn.lesson_controlflow import lesson_control_flow as cf_lesson
from basilearn.lesson_loops import lesson_loops as lps_lesson
from basilearn.lesson_functions import lesson_functions as ftns_lesson

class Basilearn:
    def __call__(self):
        print("Welcome to the Python Learning Program!\n")
        
        while True:
            print("Choose a lesson to start:")
            print("1. Lesson 1: Variables and Data Types")
            print("2. Lesson 2: Operators and Expressions")
            print("3. Lesson 3: Control Flow")
            print("4. Lesson 4: Loops")   
            print("5. Lesson 5: Functions")         
            print("6. Exit the program")

            choice = input("Enter the number of your choice: ").strip()

            if choice == '1':
                var_lesson()  # Call Lesson 1
            elif choice == '2':
                op_lesson()  # Call Lesson 2
            elif choice == '3':
                cf_lesson()  # Call Lesson 3
            elif choice == '4':
                lps_lesson()  # Call Lesson 4
            elif choice == '5':
                ftns_lesson()  # Call Lesson 5
            elif choice == '6':
                print("Thank you for using the Python Learning Program! Goodbye!")
                break  # Exit the program
            else:
                print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.\n")
