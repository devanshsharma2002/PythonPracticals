def rom(string, base):
    # Define Roman numeral symbols and their values
    roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # Convert Roman numeral string to integer
    def roman_to_integer(roman):
        total = 0
        prev_value = 0
        
        for char in roman:
            if char in roman_to_int:
                current_value = roman_to_int[char]
                if prev_value < current_value:
                    total += current_value - 2 * prev_value
                else:
                    total += current_value
                prev_value = current_value
            else:
                raise ValueError(f"Invalid Roman numeral character: {char}")
        return total

    # Convert integer to the desired base
    def integer_to_base(num, base):
        if num == 0:
            return "0"
        digits = []
        while num:
            digits.append(int(num % base))
            num //= base
        return ''.join(str(d) for d in digits[::-1])

    # Convert Roman numeral to integer
    integer_value = roman_to_integer(string)
    
    # Handle invalid base
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36.")

    # Convert integer to the desired base
    return integer_to_base(integer_value, base)

# Example usage
romans = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
bases = [2, 8, 16, 20]

for roman in romans:
    for base in bases:
        result = rom(roman, base)
        print(f"The Roman numeral '{roman}' converts to {result} in base {base}.")
