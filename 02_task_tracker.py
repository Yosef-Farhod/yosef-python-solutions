# Task Tracker:
# This script takes a list of today's tasks, asks the user which ones are done or ongoing,
# and then shows a summary of completed and pending tasks.


done_tasks=[]
ongoing_tasks=[]

tasks=input('Enter your tasks for today separatd by a comma:').split(', ')

for x in tasks :
    print(f"\n{x}")
    q=input (f"Did you finsh {x} alrady").lower()
    if q =='yes' :
        print(' Nice Jop')
        done_tasks.append(x)
    elif q=='no' :
        print('try not to put it off')
        ongoing_tasks.append(x)
    print ('------')

s=input ("Do you want to see your today's programss ?(yes/no)").lower()

if s =='yes' :
    print(f"    # Task Tracker:
# This script takes a list of today's tasks, asks the user which ones are done or ongoing,
# and then shows a summary of completed and pending tasks.


done_tasks=[]
ongoing_tasks=[]

tasks=input('Enter your tasks for today separatd by a comma:').split(', ')

for x in tasks :
    print(f"\n{x}")
    q=input (f"Did you finsh {x} alrady").lower()
    if q =='yes' :
        print(' Nice Jop')
        done_tasks.append(x)
    elif q=='no' :
        print('try not to put it off')
        ongoing_tasks.append(x)
    print ('------')

s=input ("Do you want to see your today's programss ?(yes/no)").lower()

if s =='yes' :
    print(f"    *****Done Tasks****\n {done_tasks}")
    print(f"    *****Ongoing Tasks****\n{ongoing_tasks}")
else :
    print('ok')

naum=input ('What is your name ?')
print(f"Welcome {naum} to your program")

