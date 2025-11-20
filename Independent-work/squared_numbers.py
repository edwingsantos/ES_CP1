#ES 1 squared numbers
#make a list named numbers and put the nujmbers that Ms LaRose gave us 
numbers = [3, 7, 12, 25, 30, 45, 50, 65, 70, 85, 90, 105, 110, 125, 130, 145, 150, 165, 170, 185, 190, 205, 210, 225, 230, 245, 250, 265, 270, 285]
#make a varible named squared, that is where we are keeping the squared numbers
#use map and list so it acces the number list, then use lambda n: (n**2), numbers 
squared = list(map(lambda n: (n**2), numbers))
print(squared)