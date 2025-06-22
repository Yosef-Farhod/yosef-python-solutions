# Second Lowest Score Finder:
# This script reads student names and scores, then prints the names of all students
# who have the second lowest score, sorted alphabetically.

if __name__ == '__main__' :
    students = []

    n = int(input('Enter number : '))

    for _ in range(n) :
        name = input('Enter name :')
        score = float(input('Enter diger : ')) 
        students.append([name,score])

    scores = []
    for student in students : 
        scores.append(student[1])


    lower_score = min(scores)
  

    filtered_scores =[]
    for score in scores : 
        if score != lower_score :
            filtered_scores.append(score)

    
    second_score = min(filtered_scores)
  

    second_students =[]

   
    for student in students :
        if student[1] == lower_score :
            second_students.append(student[0])
        elif student[1] == second_score :
            second_students.append(student[0])
        else :
            a=a+1

    second_students.sort()

    for name in second_students :
        print(name)