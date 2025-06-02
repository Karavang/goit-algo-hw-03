from functools import lru_cache
from typing import Dict, List

start: Dict[str, List[int]] = {'A': [3, 2, 1], 'B': [], 'C': []}

@lru_cache(maxsize=None)
def towers():
    global start
    if len(start['A']) != 0:
        start['B'].append(start['A'][-1])
        start['A'].pop()
        print(start)
        towers()
    elif len(start['B']) != 0:
        start['C'].append(start['B'][-1])
        start['B'].pop()
        print(start)
        towers()
    else: 
        print(f'Алгоритм завершено. Остаточний стан: {start}')

if __name__ == "__main__":
    towers()