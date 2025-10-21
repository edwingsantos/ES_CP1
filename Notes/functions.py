# ES 1 function notes 

def add(x,y):
    return x+y


def initials(name):
    names = name.split("")
    initials = ""
    for name in names:
        initials += name[0]
        

    return initials


add(5,5)
print(f"10+72{add(10+72)}")
x=0
while x<3:
    print("duck")
print(initials("Edwing Santos Arrieta"))


print(f"a = {ord("a")}")
print(f"98 = {chr("98")}")