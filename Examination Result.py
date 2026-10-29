marks = [80, 75, 65]
total = sum(marks)

print("Total Marks:", total)

if all(m >= 35 for m in marks):
    print("Result: Pass")
else:
    print("Result: Fail")
