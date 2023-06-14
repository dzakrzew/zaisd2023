"""
Algorytm wyznaczania lat przestępnych Grzegorza XIII

Autor:  <@student.polsl.pl>
Data: 07-03-2023
"""

def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

if __name__ == "__main__":
    for y in range(2000, 2030):
        print('{}: {}'.format(y, is_leap(y)))
