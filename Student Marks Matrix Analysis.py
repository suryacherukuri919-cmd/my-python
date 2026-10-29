marks = [
    [80, 70, 90],
    [60, 75, 85],
    [90, 95, 80]
]

for i in range(len(marks)):
    total = sum(marks[i])
    print("Student", i + 1, "Total:", total)
