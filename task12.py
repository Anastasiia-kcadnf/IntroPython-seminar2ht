'''
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих 
чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
'''

sum = int(input('Введите сумму двух натуральных чисел X и Y (X,Y≤1000): '))
proiz = int(input('Введите произведение двух натуральных чисел X и Y (X,Y≤1000): '))
count = 0
for x in range(1, 1001):
        y = sum - x
        for y in range(1, 1001):
            if x + y == sum and x * y == proiz:
                count += 1
                print(x, y)
                break
if count == 0:
    print('Введены некорректные данные.')