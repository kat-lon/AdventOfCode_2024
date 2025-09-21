#Day 1 Part 2
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


repetitions = {key:list2.count(key) for key in set(list1)}

result = 0
for i in list1:
    result += i * repetitions.get(i)



print(result)


