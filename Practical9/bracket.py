

def check_validity(text: str) -> str:
    # Set of valid opening and closing brackets
    brackets = {'(': ')', '{': '}', '[': ']', '<': '>'}
    stack = []

    for i, char in enumerate(text):
        if char in brackets.keys():  # If it's an opening bracket
            stack.append(char)
        elif char in brackets.values():  # If it's a closing bracket
            if not stack:
                return f"Invalid: Extra closing bracket '{char}' at position {i}"
            last_open = stack.pop()
            if brackets[last_open] != char:
                return f"Invalid: Mismatched brackets '{last_open}' and '{char}' at position {i}"
        elif char.isalnum() or char.isspace() or char in '+-*/':  # Ignore valid non-bracket characters
            continue
        else:
            return f"Invalid: Invalid character '{char}' at position {i}"

    if stack:
        return f"Invalid: Unmatched opening bracket '{stack[-1]}'"

    return "Valid"

# Example usage:
print(check_validity("(<>))"))   # Output: Invalid due to extra closing bracket
print(check_validity("{1+2}"))   # Output: Valid
print(check_validity("[+()]"))   # Output: Valid
