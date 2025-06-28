names = []

n = int(input("Enter number names : "))
for i in range(n) :
    name = input(f"Enter the name {i+1} : ").lower()
    names.append(name)

user = input("Enter sarch name : ").lower()

if user in names :
    print(f"Succse find name {user}")
else :
    print(f"Name {user} not find ")
