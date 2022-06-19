import math as m

def Calc():
    while(True):
        try:
            ch1 = int(input("Число 1: "))
            doing = input("Действие\n(log10 - логарифм по основанию 10, log2 - логарифм по основанию 10, ! - факториал, √ - корень\n* - умножение, / - деление, + - сложение, - - вычитание\n** - возведение в степень, // - деление нацело, % - остаток от деления,\nP - периметр параллелепипеда, S - площадь параллелепипеда, 0 - выход): ")
            if doing == "!":
                ch1 = m.factorial(ch1)
            elif doing =="log10":
                ch1=m.log10(ch1)
            elif doing =="log2":
                ch1=m.log2(ch1)
            elif doing =="√":
                ch1=m.sqrt(ch1)
            elif doing =="0":
                return
            else:
                ch2 = int(input("Число 2: "))
                if doing == "+":
                    ch1=ch1+ch2
                elif doing == "-":
                    ch1=ch1-ch2
                elif doing == "*":
                    ch1=ch1*ch2
                elif doing == "/":
                    ch1=ch1/ch2
                elif doing == "**":
                    ch1=ch1**ch2
                elif doing == "//":
                    ch1=ch1//ch2
                elif doing == "%":
                    ch1=ch1%ch2
                elif doing == "P":
                    ch3 = int(input("Число 3: "))
                    P = lambda a, b, c: 4 *(a + b + c)
                    ch1 = P(ch1, ch2, ch3)
                elif doing == "S":
                    ch3 = int(input("Число 3: "))
                    S = lambda a, b, c: 2 *(a * b + b * c + a * c)
                    ch1 = S(ch1, ch2, ch3)
            print("Итог: %s"%ch1)
        except:
            print("Неправильный ввод")
            continue

def String():
    simvols = 0
    prob = 0
    zap = 0
    stroka = input("Cтрока: ")
    for i in stroka:
        if i ==" ":
            prob+=1
        if i ==",":
            zap+=1
        simvols+=1
    print("Символов: %s" %simvols)
    print("Пробелов: %s" %prob)
    print("Запятых: %s" %zap)

def Matrix(stolbec, stroka, nachalo, shag):
    chislo = nachalo
    print("Итог:\n")
    for i in range(nachalo, stroka*shag+nachalo, shag):
        for j in range (nachalo, stolbec*shag+nachalo, shag):
            print(chislo, end=" ")
            chislo+=shag
        print()

while(True):
    try:
        vibor = int(input("Выберите номер задания (1-3): "))
        if(vibor == 1):
            Calc()
        elif(vibor == 2):
            String()
        elif(vibor == 3):
            stolbci = int(input("Количество столбцов: "))
            if stolbci==0:
                continue
            stroki = int(input("Количество строк: "))
            if stroki==0 :
                continue
            nachalo = int(input("Начальное значение матрицы: "))
            shag = int(input("Шаг: "))
            if shag == 0:
                continue
            Matrix(stolbci, stroki, nachalo, shag)
        else:
            print("Неправильный номер задания")
    except:
        print("Неправильный ввод")