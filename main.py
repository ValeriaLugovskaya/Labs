
HEIGHT = 173
WEIGHT = 60
STEPS = 1000
TIME = 60
ENERGY = 0.035*WEIGHT+((STEPS/TIME)**2 / HEIGHT) * 0.029*WEIGHT
DISTANCE = STEPS*(HEIGHT/4+0.37)/10000
if (DISTANCE<2):
    print(f"Сегодня вы пробежали всего {DISTANCE} км")
elif (2<DISTANCE<4):
    print(f"Результат лучше среднего: {DISTANCE} км!")
elif (DISTANCE>4):
    print(f"Это уже слишком..... Ваша дистанция: {DISTANCE} км!")

word = input()
if str(word) == str(word)[::-1]:
    print("It's palindrome")
else:
    print("It's not palindrome")

