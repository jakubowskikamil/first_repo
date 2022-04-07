
#x = 2
#if x > 1 and x < 3:
    #print("ok")

# Przygotuj kalkulator
# przypadek, gdy wybierzemy złą opcję w przypadku zmiennej operation
# zabezpiecz go przed dzieleniem przez zero

#moze byc zerem
# first_num = int(input("Podaj pierwsza liczbe: "))
#print(type(first_num))

#nie moze byc zerem
# second_num = int(input("Podaj druga liczbe: "))
#
# if second_num == 0:
#     int(input("Podaj druga liczbe rozna od zera: "))
#
# operation = input("Wybierz znak: + [dodawanie], - [odejmowanie], * [mnozenie], / [dzielenie]")
#
# if operation == "+":
#     print(first_num + second_num)


# Przygotuj kalkulator
# przypadek, gdy wybierzemy złą opcję w przypadku zmiennej operation
# zabezpiecz go przed dzieleniem przez zero

#moze byc zerem
first_num = int(input("Podaj pierwsza liczbe: "))
#print(type(first_num))

#nie moze byc zerem
second_num = int(input("Podaj druga liczbe: "))

if second_num == 0:
    int(input("Podaj druga liczbe rozna od zera: "))

operation = input("Wybierz znak: + [dodawanie], - [odejmowanie], * [mnozenie], / [dzielenie]")

if operation == "+":
    print(first_num + second_num)
elif operation == "-":
    print(first_num - second_num)
elif operation == "*":
    print(first_num * second_num)
elif operation == "/":
    print(first_num / second_num)
else:
    print("nie ma takiego dzialania")



