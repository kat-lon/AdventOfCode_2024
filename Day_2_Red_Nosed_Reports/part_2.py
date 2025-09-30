#Day 1 Part 1
from pathlib import Path

BASE_DIR = Path(__file__).parent
INPUT = BASE_DIR / 'input.txt'

def analize_report(report:list):
    report_analysis = {'steep_pairs':set(), 
                       'repeating_pairs':set(), 
                       'increasing_pairs':set(), 
                       'decreasing_pairs':set()}
    
    for i, j in zip(range(len(report) - 1), range(1, len(report))):

        if abs(report[i] - report[j]) > 3:
            report_analysis['steep_pairs'].add(i)
            report_analysis['steep_pairs'].add(j)

        if report[i] == report[j]:
            report_analysis['repeating_pairs'].add(i)
            report_analysis['repeating_pairs'].add(j)

        if report[i] < report[j]:
            report_analysis['increasing_pairs'].add(i)
            report_analysis['increasing_pairs'].add(j)
        else:
            report_analysis['decreasing_pairs'].add(i)
            report_analysis['decreasing_pairs'].add(j)

    return report_analysis
        


def problem_dampener(report_analysis:dict):
    n_increasing_pairs = len(report_analysis['increasing_pairs'])
    n_decreasing_pairs = len(report_analysis['decreasing_pairs'])
    
    if n_increasing_pairs > n_decreasing_pairs:
        spike = report_analysis['decreasing_pairs']
    else:
        spike = report_analysis['increasing_pairs'] 

    misreading, flag = -1, True
    flagging_levels = report_analysis['steep_pairs'].union(report_analysis['repeating_pairs']).union(spike)
    if len(flagging_levels) > 3:
        flag = False

    elif len(flagging_levels) == 2:

        if min(flagging_levels) == 0:
            misreading = min(flagging_levels)
        elif (n_decreasing_pairs != 0 and n_decreasing_pairs < n_increasing_pairs
            and (max(report_analysis['decreasing_pairs']) < n_increasing_pairs)):
            misreading = min(flagging_levels)
        else:
            misreading = max(flagging_levels)

    elif len(flagging_levels) == 3:
        misreading = list(flagging_levels)[1]

    return flag, misreading
    
def count_safe_reports(reports:list):
    safe_reports = 0
    for report in reports:
        report_analysis = analize_report(report)
        result_dampener = problem_dampener(report_analysis)

        if not result_dampener[0]:
            continue

        if result_dampener[0] and result_dampener[1] != -1:
            report.pop(result_dampener[1])
            report_analysis = analize_report(report)
            if problem_dampener(report_analysis)[1] != -1:
                continue

        safe_reports += 1
            
    
    return safe_reports


with open(INPUT, 'r') as raw:
    matrix = [[int(string) for string in line[:-1].split(' ')] 
                           for line in raw.readlines()]

print(count_safe_reports(matrix))