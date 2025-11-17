#Args and kwags 1 ES
#def hello(name="Tia",age=34):
    #return f"hello {name}"

##print(hello())
#print(hello("treyson", 14))
#print(hello(age=14)

def hello(*names,**kwargs):
    print(type(names))
    print(kwargs)
    for n in names:
        print(f"hello {n}{kwargs['last_name']}")
hello("Alex","Edwing","james", last_name= "Santos", dad = "Alonso", age= 23)
#The * means all 

def full_name(**names):
    if 'middle' in names.keys():
        return f"{names['first']}{names['middle']}{names['last']}"
    else:
        return f"{names['first']}{names['last']}"
     
full_name(first="Koro", last="sensei")
full_name(first="Edwing", middle = "Fernando", last = "Santos")

def summary(**story):
    sum = ""
    if "name" in story.keys():
        sum+= f"{story['name']} is the main character of this story"
    if "place" in story.keys():
        sum+= f"The sotyr takes place in {story['place']}"
    if "conflict" in story.keys():
        sum+= f"The problem is {story['conflict']}"

    return sum 
print(summary)