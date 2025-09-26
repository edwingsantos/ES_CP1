#ES 1 basic calculator


number1 = int(input("Choose a number: "))
number2 = int(input("Choose another number: "))
result1 = (number1 + number2)
result2 = (number1 - number2)
result3 = (number1 * number2)
result4 = (number1 / number2)
result5 = (number1 // number2)
result6 = (number1 % number2)
result7 = (number1 ** number2)
print(f"{number1}+{number2}={result1:.2f}")
print(f"{number1}-{number2}={result2:.2f}")
print(f"{number1}*{number2}={result3:.2f}")
print(f"{number1}/{number2}={result4:.2f}")
print(f"{number1}//{number2}={result5:.2f}")
print(f"{number1}%{number2}={result6:.2f}")
print(f"{number1}**{number2}={result7:.2f}")
