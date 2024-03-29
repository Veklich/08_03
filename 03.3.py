# На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень. 
# Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6. 
# Найти вероятность того, что выстрел произведен: 
# a). первым спортсменом 
# б). вторым спортсменом 
# в). третьим спортсменом.


p = 1/3 * 0.9 + 1/3 * 0.8 + 1/3 * 0.6

result1 = 1/3 * 0.9 / p
result2 = 1/3 * 0.8 / p
result3 = 1/3 * 0.6 / p

print(f"выстрел произведен первым спортсменом: {result1}")
print(f"выстрел произведен вторым спортсменом: {result2}")
print(f"выстрел произведен вторым спортсменом: {result3}")