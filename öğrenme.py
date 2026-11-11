isim = input("isminizi giriniz: ")
soyisim = input("soyisminizi giriniz: ")
yas = int(input("yaşınızı giriniz: "))
posta =  input("posta giriniz: ")
print(isim.title()[0:3] + "** " + soyisim.title()[0:2] + "*** " + "Yaşınızı doğrulamak için e-posa gönderilmiştir")
onay = input("yaşınızı doğruladınızmı?  (evet: e , hayır: h)")
if yas >= 18 and onay == "e":
    print("Girişiniz yapılmaktadır lütfen bekleyiniz...")
elif yas < 18 and onay == "e":
    print("18 Yaş altının ebebeyn üzerinden giriş yapması gerekmektedir")

if onay == "h":
    print("İşeminiz yapılamıyor lütfen e-postayı onaylayın")

if yas < 18 and onay == "h":
    print("uygun şartları sağlamıyorsunuz")
