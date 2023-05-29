# В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых. 
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. Какова вероятность того, что 3 мяча белые?

from math import factorial
def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

p1 = combinations(5, 2) / combinations(8, 2) * combinations(5, 1) * combinations(7, 3) / combinations(12, 4)
p2 = combinations(5, 1) * combinations(3, 1) / combinations(8, 2) * combinations(5, 2) * combinations(7, 2) / combinations(12, 4)
p3 = combinations(3, 2) / combinations(8, 2) * combinations(5, 3) * combinations(7, 1) / combinations(12, 4)
result = p1 + p2 + p3
print(f"вероятность того, что 3 мяча белые: {result}")