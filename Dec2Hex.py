import sys

def dec_to_hex(decimal_value):
    try:
        # Ensure an argument is provided
        if not decimal_value:
            raise ValueError("Error: No input provided. Please enter an integer.")

        # Convert input to integer
        decimal_value = int(decimal_value)
        
        # Convert to hexadecimal
        return hex(decimal_value)

    except ValueError:
        return "Error: Invalid input. Please enter an integer."

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No input provided. Please enter an integer.")
        sys.exit(1)

    user_input = sys.argv[1]
    result = dec_to_hex(user_input)
    print(result)
