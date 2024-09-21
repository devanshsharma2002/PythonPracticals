def get_valid_invalid_text_count(texts: list) -> tuple:
    def check_validity(text: str) -> str:
        brackets = {'(': ')', '{': '}', '[': ']', '<': '>'}
        stack = []
        
        for i, char in enumerate(text):
            if char in brackets.keys():  # If it's an opening bracket
                stack.append(char)
            elif char in brackets.values():  # If it's a closing bracket
                if not stack:
                    return "Invalid"
                last_open = stack.pop()
                if brackets[last_open] != char:
                    return "Invalid"
            elif char.isalnum() or char.isspace() or char in '+-*/':  # Ignore valid non-bracket characters
                continue
            else:
                return "Invalid"
        
        return "Invalid" if stack else "Valid"

    valid_count = 0
    invalid_count = 0

    for item in texts:
        if isinstance(item, str):  # Check only string objects
            if check_validity(item) == "Valid":
                valid_count += 1
            else:
                invalid_count += 1

    return (valid_count, invalid_count)

# Example usage:
texts = ['[{(', [45], '()', '', '()[]', 'invalid_char!']
print(get_valid_invalid_text_count(texts))   # Output: (3, 2)
