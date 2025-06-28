names = []

n = int(input("Enter number names : "))
for i in range(n) :
    name = input(f"Enter the name {i+1} : ")
    names.append(name)

user = input("Enter sarch name : ").lower()
sarch = True

for i in names :
    if i == user:
        print(f"saccses find the name {i}")
        sarch = False
        break

if sarch :
    print(f"name {user} not find ")        

