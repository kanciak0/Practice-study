import os
Pricesandnames={}
def SecretAuction():
    finished= False
    while not finished:
        x = input("Podaj nazwe")
        y = int(input("Podaj liczbe"))
        Pricesandnames[x]=y
        print("Czy chcesz kogos jeszcze dodac? Wpisz tak/nie")
        os.system('cls')
        dodatkowy=input()
        if dodatkowy=="tak":
            continue
        if dodatkowy=="nie":
            max_val=list(Pricesandnames.values())
            max_key=list(Pricesandnames.keys())
            print(max_key[max_val.index(max(max_val))],max(max_val))
            finished=True

SecretAuction()