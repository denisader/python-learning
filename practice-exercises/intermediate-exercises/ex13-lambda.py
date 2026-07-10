employees = [
    {"name": "A", "salary": 50},
    {"name": "B", "salary": 70},
    {"name": "C", "salary": 60}
]

# the lambda x: x['salary'] tells Python:
# 'When you compare two dictionaries, don't look at the whole thing, only at 'salary' value
sorted_staff = sorted(employees, key=lambda x: x['salary'], reverse=True)
# sorted is a stable function 
# if two employees had the same salary -> their original order would not change

for emp in sorted_staff:
    print(emp)
