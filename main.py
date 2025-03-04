def toplama(sayi1, sayi2):
    return sayi1 + sayi2


def cikarma(sayi1, sayi2):
    return sayi1 - sayi2


def carpma(sayi1, sayi2):
    return sayi1 * sayi2


def bolme(sayi1, sayi2):
    if sayi2 == 0:
        return "Hata: Bir sayıyı sıfıra bölemezsiniz!"
    return sayi1 / sayi2


print("Hesap Makinesi 1.0")
print("Toplama : +, Çıkarma : -, Çarpma : x, Bölme : /, Çıkış : q")

while True:
    secim = input("İşleminiz: ")

    if secim == "q":
        print("Çıkılıyor...")
        break

    if secim in ["+", "-", "x", "/"]:
        sayi1 = float(input("Birinci sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))

        if secim == "+":
            print("Sonuç:", toplama(sayi1, sayi2))
        elif secim == "-":
            print("Sonuç:", cikarma(sayi1, sayi2))
        elif secim == "x":
            print("Sonuç:", carpma(sayi1, sayi2))
        elif secim == "/":
            print("Sonuç:", bolme(sayi1, sayi2))
    else:
        print("Yanlış seçim, lütfen tekrar deneyin.")
