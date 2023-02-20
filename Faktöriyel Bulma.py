print("""
*************************

Faktöriyel Bulma Programı

*************************

""")
while True:
    sayi = int(input("Faktöriyeli alınacak sayıyı giriniz: "))
    faktoriyel = 1
    if sayi<0:
        print("Negatif sayıların Faktöriyeli tanımsızdır.")
        continue
    else:
        for i in range(1,sayi+1):
            faktoriyel *= i

        print(faktoriyel)

