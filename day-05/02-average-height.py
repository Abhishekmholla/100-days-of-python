print("Welcome to Average height calculator!!")
student_heights  = list(map(int,input("Please enter the heights in a comma seperated format...").split(',')))

total_value = 0

for student_height in student_heights:
    total_value+= student_height
    
total_value = round(total_value/len(student_heights),2)
print("The average height of the students entered is {0}".format(total_value))