import random
#ilk önce müşterileri ve siparişleri belirliyorum

musteriler = ["Andrew", "Rose", "Martha", "Bruce"]
secenekler = ["Klasik Burger" , "Cheeseburger" , "Tavuklu Burger"]

#müşteriler ve seçenekler yani burger rasgele seçiliyor
musteri = random.choice (musteriler)
secenek = random.choice (secenekler)

#altta ekrana çıkıcak rolerplay mesajları bulunmakta rasgele biri geliyor ve rasgele sipariş veriyor
print("hamburgerciye hooooş geldiniz!")

print(f"dükkana  {musteri}  geldi!")
print(f"merhaba {musteri}! ne sipariş edersiniz?")
print(f"{musteri}: Merhaba ben {secenek} istiyorum")

#burger için malzemeler veriliyor
print("--- MALZEME LİSTESİ ---")
print("1: Ekmek | 2: Dana Köfte | 3: Peynir | 4: Tavuk Köftesi")


secim = input("Lütfen malzemeleri aralarına virgül koyarak girin (Örn: 1,2,3): ")


hazirlanan_burger = secim.split(",")

print(f"Hazırladığın malzeme listesi: {hazirlanan_burger}")

#burgerlerin kodları klasik için 1 ve 2 yi cheeseburger ise 1 2 ve 3 tavuklu burger  ise 1 ve 4 tuşlanır
if hazirlanan_burger == ["1", "2"]:
    hazirlanan_isim = "Klasik Burger"

elif hazirlanan_burger == ["1", "2", "3"]:
    hazirlanan_isim = "Cheeseburger"

elif hazirlanan_burger == ["1", "4"]:
    hazirlanan_isim = "Tavuklu Burger"
else:
    hazirlanan_isim = "Bilinmeyen Tarif"
#burada doğru yapıldıysa eline sağlık doğrudeğilse para iadesi ister
if hazirlanan_isim == secenek:
    print(f"{musteri}: 'Harika! Tam istediğim gibi bir {secenek} olmuş, eline sağlık!'")
else:
    print(f"{musteri}: 'Ben {secenek} istemiştim ama sen bana {hazirlanan_isim} verdin para iadesi istiyorum!'")