import time
saldo=0
print("CARD ACCEPTED")
p1=input("Hello, first time using credit card?\nPlease, register your card by entering four-digit pin number: ")
p1=int(p1)
time.sleep(1)
print("Please wait...")
time.sleep(3)
print("Your card has been registered successfully")
time.sleep(1)
print("SYSTEM IS RESTARTING...")
time.sleep(3)
l=0
time.sleep(1)
print("CARD ACCEPTED")
time.sleep(1)
while l<=0 or l>3:
    print("1. Polski\n2. English\n3. Español")
    l=input("Choose language: ")
    l=int(l)
    time.sleep(2)
    if l==1:
        p = input("Podaj pin: ")
        p = int(p)
        time.sleep(2)
        while p != p1:
            print("Niepoprawny pin")
            time.sleep(1)
            p=input("Podaj pin: ")
            p=int(p)
            time.sleep(2)
        print("1. Wpłata gotówki\n2. Wypłata gotówki\n3. Stan konta\n4. Wyjdź")
        o=input("Wybierz operację: ")
        o=int(o)
        while o != 4:
            if o<1 or o>4:
                print("NIEPOPRAWNY NUMER OPERACJI!")
                time.sleep(2)
            elif o==1:
                wp=input("Podaj kwotę wpłaty: ")
                wp=int(wp)
                time.sleep(1)
                saldo+=wp
                print("Saldo po wpłacie wynosi: ",saldo)
                time.sleep(2)
            elif o==2:
                wyp = input("Podaj kwotę wypłaty: ")
                wyp = int(wyp)
                time.sleep(1)
                if wyp<=saldo:
                    saldo -= wyp
                    print("Saldo po wypłacie wynosi: ", saldo)
                    time.sleep(2)
                else:
                    print("ZA MAŁO ŚRODKÓW!")
                    time.sleep(2)
            elif o==3:
                print("Saldo wynosi: ",saldo)
                time.sleep(2)
            print("1. Wpłata gotówki\n2. Wypłata gotówki\n3. Stan konta\n4. Wyjdź")
            o = input("Wybierz operację: ")
            o = int(o)
        print("ODBIERZ KARTĘ")
        time.sleep(2)
        print("DZIĘKUJEMY ZA SKORZYSTANIE Z NASZEGO BANKOMATU\n\t\t\t\tDO ZOBACZENIA!")
        time.sleep(5)
        break
    elif l==2:
        p = input("Enter the pin: ")
        p = int(p)
        while p != p1:
            print("Invalid pin")
            p = input("Enter the pin: ")
            p = int(p)
        print("1. Cash deposit\n2. Cash withdraw\n3. Account balance\n4. Exit")
        o = input("Select an operation: ")
        o = int(o)
        while o != 4:
            if o < 1 or o > 4:
                print("INVALID OPERATION NUMBER!")
            elif o == 1:
                wp = input("Enter your deposit amount: ")
                wp = int(wp)
                saldo += wp
                print("The balance after the deposit is: ", saldo)
            elif o == 2:
                wyp = input("Enter the withdrawal amount: ")
                wyp = int(wyp)
                if wyp <= saldo:
                    saldo -= wyp
                    print("The balance after the withdrawal is: ", saldo)
                else:
                    print("TOO LESS FUNDS ON THE ACCOUNT!")
            elif o == 3:
                print("The balance is: ", saldo)
            print("1. Cash deposit\n2. Cash withdraw\n3. Account balance\n4. Exit")
            o = input("Select an operation: ")
            o = int(o)
        print("RECEIVE CARD")
        time.sleep(2)
        print("THANK YOU FOR USING OUR ATM\n\t\tGOODBYE!")
        time.sleep(5)
        break
    elif l==3:
        p = input("Podaj pin: ")
        p = int(p)
        while p != p1:
            print("Zły pin")
            p = input("Podaj pin: ")
            p = int(p)
        print("1. Depósito en efectivo\n2. Retiro de efectivo\n3. Saldo de la cuenta\n4. Salida")
        o = input("Seleccione una operación: ")
        o = int(o)
        while o != 4:
            if o < 1 or o > 4:
                print("NÚMERO DE OPERACIÓN NO VÁLIDO!")
            elif o == 1:
                wp = input("Ingrese el monto de su depósito: ")
                wp = int(wp)
                saldo += wp
                print("El saldo después del depósito es: ", saldo)
            elif o == 2:
                wyp = input("Ingrese el monto del pago: ")
                wyp = int(wyp)
                if wyp <= saldo:
                    saldo -= wyp
                    print("El saldo después del pago es: ", saldo)
                else:
                    print("DEMASIADO MENOS FONDOS EN LA CUENTA!")
            elif o == 3:
                print("El saldo es: ", saldo)
            print("1. Depósito en efectivo\n2. Retiro de efectivo\n3. Saldo de la cuenta\n4. Salida")
            o = input("Seleccione una operación: ")
            o = int(o)
        print("RECIBIR TARJETA")
        time.sleep(2)
        print("GRACIAS POR USAR NUESTRO CAJERO AUTOMÁTICO\n\t\t\tNOS VEMOS!")
        time.sleep(5)
        break
    else:
        print("WRONG NUMBER\nTRY AGAIN")
        time.sleep(1)