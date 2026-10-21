students = [['Monika', 90],
            ['Annu', 20],
            ['Manup', 97]]

print(list(filter(lambda row: row[0].startswith('M'), students)))