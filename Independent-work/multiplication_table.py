#ES 1 multiplication table 

biggest_num = int(input("What do you want the biggest number to be?"))
times = 1

for num in range(1,biggest_num +1):
  number = []
  # the i will tell the code to print 1-12
  for i in range(1,13):
    #this will the the code to multiply it by which ever number the user chose
    number.append(i*times)
  times += 1
  print(number)
          #The number that the user chose, will be the amount of lines down in the multipication table 
