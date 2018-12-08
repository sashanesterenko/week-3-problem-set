import csv

dicts = [
            {'name': 'Mary', 'age': 25, 'job': 'Scientist'},
            {'name': 'Basil', 'age': 8, 'job': 'Programmer'},
            {'name': 'Edward', 'age': 48, 'job': 'Big boss'}
        ]

def dict_to_csv (dicts):
    with open('csv_problem.csv', 'w', encoding='utf-8') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for user in dicts:
            writer.writerow(user)
        #нужен ли здесь return?

if __name__ == "__main__":
    dict_to_csv(dicts)