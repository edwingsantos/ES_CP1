#ES 1 formating outputs
name = "jake"
age = 12
money = 67.2
percentege = .74
print("hello {}, you are  {:,}. And you are a good boy, you have ${:.2f} you must be rich. Random percente is {:%}".format(name,age,money))

print(f"hello {name}, you are {age:,}. That is so old. you have ${money:.2f},random percente id {percentege:%}.")