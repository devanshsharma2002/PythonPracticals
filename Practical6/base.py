def base(text, textbase, outputbase):
    # Validate base values
    if not (2 <= textbase <= 34) or not (2 <= outputbase <= 34):
        raise ValueError("Base must be between 2 and 34.")

    # Define character mapping for bases higher than 10
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Convert from any base to decimal
    def to_decimal(text, base):
        num = 0
        for char in text:
            if char not in chars[:base]:
                raise ValueError(f"Invalid character '{char}' for base {base}.")
            num = num * base + chars.index(char)
        return num

    # Convert from decimal to any base
    def from_decimal(num, base):
        if num == 0:
            return "0"
        digits = []
        while num:
            digits.append(chars[num % base])
            num //= base
        return ''.join(digits[::-1])

    # Convert input text to decimal
    decimal_value = to_decimal(text, textbase)

    # Convert decimal value to the desired output base
    return from_decimal(decimal_value, outputbase)

# Example usage
texts = ["1010", "1A", "1101", "Z"]
textbases = [2, 16, 10, 36]
outputbases = [10, 2, 16, 34]

for text in texts:
    for textbase in textbases:
        for outputbase in outputbases:
            try:
                result = base(text, textbase, outputbase)
                print(f"'{text}' in base {textbase} is '{result}' in base {outputbase}.")
            except ValueError as e:
                print(e)
