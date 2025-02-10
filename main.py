def c_to_f(c):
    # Converts Celsius to Fahrenheit
    return (1.8 * c) + 32

def f_to_c(f):
    # Converts Fahrenheit to Celsius
    return (f - 32) / 1.8

def get_temperature():
    # Asks user for a temperature and returns it as a float
    while True:
        try:
            return float(input("Enter the temperature: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def main():
    while True:
        # Choosing what to convert
        while True:
            try:
                choice = int(input("Do you want to convert:\n1) Celsius to Fahrenheit\n2) Fahrenheit to Celsius\nChoose (1 / 2): "))
                if choice in [1, 2]:
                    break
                print("Invalid choice! Please enter 1 or 2.")
            except ValueError:
                print("Invalid input! Please enter a number (1 or 2).")

        # Getting the temperature from the user
        temp = get_temperature()

        # The conversion itself
        if choice == 1:
            print(f"Temperature in Fahrenheit: {c_to_f(temp):.2f}°F")
        else:
            print(f"Temperature in Celsius: {f_to_c(temp):.2f}°C")

        # Asks if the user wants to convert again
        again = input("Do you want to convert another temperature? (yes/no): ").strip().lower()
        if again not in ["y", "yes"]:
            print("Goodbye!")
            return  

if __name__ == "__main__":
    main()
