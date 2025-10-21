#ES 1 Loops notes

import time
nums = [4,2892, 4892, 2, 391, 7428, 67]

for num in nums:
    print(num)
#num represents the currect item listed 
#nums is the list
    num /= 2
    if num > 100:
        print(f"{num} is only half of {num*2}. It is a large number")
    else:
        print(num)

for num in range(20,-1, -2):
    print(num)


    