#ES 1 Mapping notes
numbers = [352,21683,273486,819]
#new_nums = []
#for number in numbers:
  #  new_nums.append(numbers/3)

def divide (num):
    return num/3
new_nums = map(lambda num: num/3, numbers)
print(list(new_nums))
for num in new_nums:
    print(num)
