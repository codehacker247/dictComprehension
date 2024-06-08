# num = [1,2,3]
# v1num = [n+1 for n in num]
# print(v1num)
#
# name="Rohit"
# letters=[l for l in name ]
# print(letters)

# range_list=[num*2 for num in range(1,5)]
# print(range_list)

names = ["Rohit", "Sneha", "Aryan", "Sourabh"]
# print(names)
#
# short_names=[name for name in names if len(name)<=5]
# print(short_names)

# import random
# students_scores = {student:random.randint(1,100) for student in names}
#
# passed_students = {student:score for (student,score) in students_scores.items() if score >=60}
#
# print(students_scores)
# print(passed_students)

student_dict = {
    "student": ["Rohit", "Aryan", "Puja"],
    "score": [45, 28, 98]
}

# for (key,value) in student_dict.items():
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# for (key,value) in student_data_frame.items():
#     print (value)

for (index, row) in student_data_frame.iterrows():
    if row.student == "Rohit":
        print(row.student)
