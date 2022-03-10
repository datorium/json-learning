import json

file = open("students.json")
data = json.load(file)

for student in data["Students"]:
    print(student["FirstName"])

#KOMANDAS UZDEVUMS 1
#Atrodi vidējo studentu vecumu (Age)
count = 0
total_age = 0
for student in data["Students"]:
    count += 1
    total_age += int(student["Age"])

print(f"Average age: {total_age/count}")

#UZDEVUMS 2
#Atrodi vidējo studentu atzīmi (Grade), pa vecuma grupām: 
#līdz 20 g., no 21 līdz 30 g un virs 30 g.
count_group_1 = 0
count_group_2 = 0
count_group_3 = 0

total_grade_group_1 = 0
total_grade_group_2 = 0
total_grade_group_3 = 0

for student in data["Students"]:
    if int(student["Age"]) < 20:
        count_group_1 += 1
        total_grade_group_1 += int(student["Grade"])
    elif int(student["Age"]) < 30:
        count_group_2 += 1
        total_grade_group_2 += int(student["Grade"])
    else:
        count_group_3 += 1
        total_grade_group_3 += int(student["Grade"])

print(f"Average grade Age<20: {total_grade_group_1/count_group_1}")
print(f"Average grade 20<Age<30: {total_grade_group_2/count_group_2}")
print(f"Average grade Age>30: {total_grade_group_3/count_group_3}")

#UZDEVUMS 3
#Atrodi vidējo studentu Age un Grade, pēc dzimuma (Gender)

count_female = 0
count_male = 0

total_age_female = 0
total_grade_female = 0
total_age_male = 0
total_grade_male = 0

for student in data["Students"]:
    if student["Gender"] == "Female":
        count_female += 1
        total_age_female += int(student["Age"])
        total_grade_female += int(student["Grade"])
    elif student["Gender"] == "Male":
        count_male += 1
        total_age_male += int(student["Age"])
        total_grade_male += int(student["Grade"])
    
print(f"{total_age_female/count_female} {total_grade_female/count_female}")
print(f"{total_age_male/count_male} {total_grade_male/count_male}")