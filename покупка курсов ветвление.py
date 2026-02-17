bank = int(input("Сколько денег на счету? "))
curses = 45000
remains = bank - curses

if bank >= curses:
    print("Курс успешно приобретен!")
    print("Остаток денег на счете:", remains)
else:
    print("На счете не хватает денежных средств")
    print("У вас на счету:", bank)

cont = input("Желаете пополнить счет? " )

if cont.lower() in ("yes", "да"):
   cont2 = int(input("Введите сумму пополнения: "))
   bank += cont2
   print("Счет успешно пополнен!")
   print("У вас на счету:", bank)
else:
    print("Хорошо")
    print("Хорошего дня!")
    exit()

cont3 = input("Желаете теперь купить курс? " )

if cont3.lower() in ("yes", "да") and bank >= curses:
    print("Курс успешно приобретен!")
    print("Остаток денег на счете:", bank-curses)
elif cont3.lower() in ("no", "нет"):
    print("Хорошо")
    print("Хорошего дня!")
else:
    print("На счете не хватает денежных средств")
    print("У вас на счету:", bank)









