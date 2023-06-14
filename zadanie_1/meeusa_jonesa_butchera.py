"""
Algorytm Meeusa-Jonesa-Butchera wyznaczania daty Wielkanocy

Autor:  <@student.polsl.pl>
Data: 07-03-2023
"""

def meeusa(year):
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4   
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1
    month_str = "marzec" if month == 3 else "kwiecień"
    return [day, month_str]


if __name__ == "__main__":
    for y in [2023, 2024, 2025, 2026]:
        d, m = meeusa(y)
        print('{}: {} {}'.format(y, d, m))
