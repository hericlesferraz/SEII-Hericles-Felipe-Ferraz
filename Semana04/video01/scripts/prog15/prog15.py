'''
Aluno: Hericles Felipe Ferraz
Matricula: 11811EMT022
'''

import csv

with open('names.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    for line in csv_reader:

        with open('new_names.csv', 'w') as new_file:
            fieldnames = ['first_name', 'last_name']

            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

            csv_writer.writeheader()