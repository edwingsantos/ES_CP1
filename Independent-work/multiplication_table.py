#ES 1 multiplication table 

many = int(input("What do you want to be the range?: "))

multipication = 1

for num in range(1,many,+1):
    number = []
    for i in range(1,13):
        number.append(i*multipication)
        multipication += 1
        print(num)