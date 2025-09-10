#ES 1 random number
import random
print(f"This is a random number from 0-1 : {random.random()}")
print(random.randint(1,20))

stat_one = random.randint(1,10) + random.randint(1,10)
stat_two = random.randint(1,10) + random.randint(1,10)
stat_three = random.randint(1,10) + random.randint(1,10)
stat_four = random.randint(1,10) + random.randint(1,10)
stat_five = random.randint(1,10) + random.randint(1,10)
stat_six = random.randint(1,10) + random.randint(1,10)
stat_seven = random.randint(1,10) + random.randint(1,10)

print(f"you stat options are: {stat_one},{stat_two},{stat_three},{stat_four},{stat_five},{stat_six},{stat_seven}")
strengh = int(input("which stat do you want as your strength: "))