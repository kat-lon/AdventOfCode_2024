#Day 1 Part 1
from pathlib import Path

BASE_DIR = Path(__file__).parent
INPUT = BASE_DIR / 'input.txt'

with open(INPUT, 'r') as raw:
    lines = raw.readlines()
    list1, list2 = [], []

    for line in lines:
        element1, element2 = line[:-1].split('   ')
        list1.append(int(element1))
        list2.append(int(element2))

list1.sort()
list2.sort()

result = 0
for x, y in zip(list1, list2):
    result += abs(x - y)

print(result)

