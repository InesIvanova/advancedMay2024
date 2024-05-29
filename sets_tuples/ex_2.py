n = int(input())

students = {}

for _ in range(n):
    data = tuple(input().split())
    name, grade = data[0], float(data[1])

    if name not in students:
        students[name] = []
    students[name].append(grade)


for student, grades in students.items():
    avg = sum(grades)/len(grades)
    print(f"{student} -> {' '.join([f'{g:.2f}' for g in grades])} (avg: {avg:.2f})")
