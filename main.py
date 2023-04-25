import cipher
islem = True
while islem:
    metin = input("Metni giriniz (çıkış yapmak için 0000): ")
    if metin == "0000":
        print("Çıkış yapıldı.")
        islem = False
    else:
        kontrol = input("Şifreleme işlemi için 1, deşifreleme işlemi için 2 giriniz: ")
        x = cipher.Cipher()
        if kontrol == "1":
            print("Şifreli metin: ",x.encrypt(metin),"\n")
        elif kontrol == "2":
            print("Deşifre edilmiş metin: ",x.decrypt(metin),"\n")
        else:
            print("Hatalı işlem girişi.\n")
