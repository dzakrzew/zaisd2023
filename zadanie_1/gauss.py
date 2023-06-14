"""
Algorytm Gaussa wyznaczania daty Wielkanocy

Autor:  <@student.polsl.pl>
Data: 07-03-2023
"""

def gauss(year):
    a = year % 19
    b = year % 4
    c = year % 7
    k = year // 100
    p = (13 + 8 * k) // 25
    q = k // 4
    m = (15 - p + k - q) % 30
    n = (4 + k - q) % 7
    d = (19 * a + m) % 30
    e = (2 * b + 4 * c + 6 * d + n) % 7
    march_day = d + e + 22

    if march_day < 32:
        return '{} marzec'.format(march_day)

    if d == 29 and e == 6:
        return '19 kwiecień'

    if d == 28 and e == 6 and a > 10:
        return '18 kwiecień'

    april_day = d + e - 9
    return '{} kwiecień'.format(april_day)

if __name__ == "__main__":
    for y in [2023, 2024, 2025, 2026]:
        print('{}: {}'.format(y, gauss(y)))
