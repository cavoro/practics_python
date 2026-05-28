def create_rating(students: list) -> list:
    n = len(students)

    for i in range(n):
        max_index = i

        for j in range(i + 1, n):
            if students[j][1] > students[max_index][1]:
                max_index = j

        students[i], students[max_index] = students[max_index], students[i]

    return students


students = [
    ("Іван", 88),
    ("Марія", 95),
    ("Олег", 78),
    ("Анна", 95)
]

rating = create_rating(students)

for student in rating:
    print(student)
