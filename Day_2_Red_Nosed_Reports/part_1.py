#Day 1 Part 1
from pathlib import Path

BASE_DIR = Path(__file__).parent
INPUT = BASE_DIR / 'input.txt'

def check_levels(report:list):
    increasing = report[0] < report[1]
    i = 0
    while i < len(report)-1:

        if increasing:
            if report[i] >= report[i+1]:
                return False
            i += 1
            continue

        if report[i] <= report[i+1]:
                return False
        i += 1

    return True

def check_safe(report:list):
    i = 1
    for x in report[:-1]:
        difference = abs(x - report[i])

        if difference > 3 or difference == 0:
            return False
        i += 1
        
    return True

def count_safe_reports(reports:list):
    safe_reports = 0
    for report in reports:
        if check_levels(report) and check_safe(report):
            safe_reports += 1
    
    return safe_reports



with open(INPUT, 'r') as raw:
    matrix = [[int(string) for string in line[:-1].split(' ')] 
                           for line in raw.readlines()]

print(count_safe_reports(matrix))