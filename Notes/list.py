#ES 1 list notes 

#comlex datat types hold mutliple things of information

sibs = ["Edgar", "Irving", "Edwing", 5.10, 3, True]
#list needs to have brackens. Every item needs comas in bewteen each other. Proper datat type\

print(sibs[0])
print(len(sibs))
sibs[0] = "erick"
sibs.pop()
sibs.remove(3)
sibs.append(3)
sibs.extend(7, 1, "james")
print(sibs)


board = [[1,2,3],
         [4,5,6],
         [7,8,9]
         ]


#tuple ordered, not vhageable
