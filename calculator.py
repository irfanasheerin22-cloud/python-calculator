print("=" * 40)
print("      PYTHON CALCULATOR")
print("=" * 40)

while True:
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "5":
        print("\nThank you for using Python Calculator!")
        break

    if choice not in ("1", "2", "3", "4"):
        print("\n❌ Invalid choice! Please try again.")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        result = num1 + num2
        print(f"\n✅ Result = {result}")

    elif choice == "2":
        result = num1 - num2
        print(f"\n✅ Result = {result}")

    elif choice == "3":
        result = num1 * num2
        print(f"\n✅ Result = {result}")

    elif choice == "4":
        if num2 == 0:
            print("\n❌ Cannot divide by zero!")
        else:
            result = num1 / num2
            print(f"\n✅ Result = {result}")