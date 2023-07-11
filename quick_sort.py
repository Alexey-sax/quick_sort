  #  id 88941500

from array import ArrayType, array
import sys
from typing import List


class Competitor:
    """Класс для отображения участника."""

    def __init__(self, login: str, solved_number: str, penalty: str) -> None:
        self.login: str = login
        self.solved_number: int = int(solved_number)
        self.penalty: int = int(penalty)

    def __lt__(self, other: 'Competitor') -> bool:
#       if self.solved_number != other.solved_number:
            return (
                (-self.solved_number, self.penalty, self.login)
                < (-other.solved_number, other.penalty, other.login)
        )
#          return self.solved_number > other.solved_number
 
#        if self.penalty != other.penalty
#            return self.penalty < other.penalty
 #  https://habr.com/ru/articles/186608/ - Магические методы сравнения
#        return self.login < other.login

    def __str__(self) -> str:
        return self.login


def quick_sort(participants, lf, rg) -> int:
    if lf > rg:
        return -1
    
    left, right = lf, rg
    pivot = participants[lf]

    while left <= right:
        while participants[left] < pivot:
            left += 1
        while participants[right] > pivot:
            right -= 1
        if left <= right:
            participants[left], participants[right] = participants[right], participants[left]
            left +=1
            right -= 1
    
    quick_sort(participants, lf, right)
    quick_sort(participants, left, rg)

"""
def sortdata(participants):
    participants[1] = -int(participants[1])
    participants[2] = int(participants[2])
    return [participants[1], participants[2], participants[0]]
"""

def read_input():
    n = int(input())
    #participants = [sortdata(input().split()) for _ in range(n)]
    arr: List[Competitor] = [
        Competitor(*sys.stdin.readline().split()) for _ in range(n)
    ]
    return arr


def main():
    participants = read_input()
    quick_sort(participants, lf = 0, rg = len(participants) - 1)
    for username in participants:
        print(username[2])


if __name__ == '__main__':
    main()
