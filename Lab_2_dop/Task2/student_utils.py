import csv

def get_top_students(students, n=3):
    return sorted(students, key=lambda s: -s[2])[:n]

def get_average_age(students):
    return round(sum(s[1] for s in students) / len(students), 1) if students else 0

def filter_by_grade(students, g):
    return [s for s in students if s[2] > g]

def load(f):
    with open(f, 'r', encoding='utf-8') as file:
        return [[row[0], int(row[1]), float(row[2])] for row in csv.reader(file)][1:]