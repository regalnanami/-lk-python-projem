import random
secenek = ["taş" , "kağıt" , "makas"]

bilgisayar_secimi = random.choice(secenek)
kullanici_secimi = input("hangi hamleyi yapacaksınız?: ( taş , kağıt , makas)").lower()


print(f"bilgisayar_secimi : {bilgisayar_secimi}")

if kullanici_secimi == bilgisayar_secimi:
    print("berabere!")
elif kullanici_secimi == "taş" and bilgisayar_secimi == "makas" :
    print("kullanıcı kazanmıştır!")
elif kullanici_secimi == "makas" and bilgisayar_secimi == "kağıt" :
    print("kullanıcı kazanmıştır!")
elif kullanici_secimi == "kağıt" and bilgisayar_secimi == "taş" :
    print("kullanıcı kazanmıştır!")
else:
    print("kaybettin!")

print("oyun bitti")