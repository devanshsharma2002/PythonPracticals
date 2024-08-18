def modulo(num1, num2):
    if num2 == 0:
        return "The divisor b cannot be zero."
    return num1 - (num1 // num2) * num2


print(modulo(10, 3))

