import csv

dicts = [
            {'name': 'Mary', 'age': 25, 'job': 'Scientist'},
            {'name': 'Basil', 'age': 8, 'job': 'Programmer'},
            {'name': 'Edward', 'age': 48, 'job': 'Big boss'}
        ]
with open('csv_problem.csv', 'w', encoding='utf-8') as f:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for user in dicts:
        writer.writerow(user)
