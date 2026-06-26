# Student Data Organizer
# Using while loop, match-case and if-else


print("Welcome to the Pattern Generator and Number Analyzer!")

while True:
    print("\nSelect an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = input("Enter your choice: ")

    match choice:

        case "1":
            rows = int(input("Enter the number of rows for the pattern: "))

            if rows > 0:
                print("\nPattern:")
                for i in range(1, rows + 1):
                    print("*" * i)
            else:
                print("Error: Number of rows must be positive!")

        case "2":
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))

            if end >= start:
                total = 0

                for num in range(start, end + 1):

                    if num % 2 == 0:
                        print(f"Number {num} is Even")
                    else:
                        print(f"Number {num} is Odd")

                    total += num

                print(f"Sum of all numbers from {start} to {end} is: {total}")

            else:
                print("Error: End value must be greater than or equal to Start value!")

        case "3":
            print("Thank you for using the Student Data Organizer.")
            print("Exiting the program. Goodbye!")
            break

        case _:
            print("Invalid choice! Please select 1, 2, or 3.")