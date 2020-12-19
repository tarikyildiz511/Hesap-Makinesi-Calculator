__author__ = "Tarık Capar"

giriş = """
(1) topla
(2) çıkar
(3) çarp
(4) böl
"""
print(giriş)

while True:
    soru = input("yapmak istediğiniz işlemi seçin (çıkmak için e):")
    if soru =="e":
        print("çıkış yapılıyor")
        break
    elif soru == "1":
        sayi1=int(input("toplama işlemi için birinci sayıyı giriniz"))
        sayi2=int(input("toplama işlemi için ikinci sayıyı giriniz"))
        print(sayi1, "+", sayi2, "=", sayi1 + sayi2)
    elif soru == "2":
        sayi1=int(input("çıkarma işlemi için birinci sayıyı giriniz"))
        sayi2=int(input("çıkarma işlemi için ikinci sayıyı giriniz"))
        print(sayi1,"-", sayi2, "=", sayi1 - sayi2 )
    
    elif soru == "3":
        sayi1=int(input("çarpma işlemi için birinci sayıyı giriniz"))
        sayi2=int(input("çarpma işlemi için ikinci sayıyı giriniz"))
        print(sayi1, "*", sayi2, sayi1*sayi2)
    elif soru == "4":
        sayi1=int(input("bölme işlemi için birinci sayıyı giriniz"))
        sayi2=int(input("bölme işlemi için ikinci sayıyı giriniz"))
        print(sayi1, "/", sayi2, sayi1/sayi2)
        