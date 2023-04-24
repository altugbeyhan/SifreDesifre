import cipher
islem = True
while islem:
    kontrol = input("Şifreleme işlemi için 1, deşifreleme işlemi için 2 yazınız: ")
    if kontrol == "1":
        duzmetin = input("Şifrelenecek metni giriniz: ")
        x = cipher.Cipher()
        print("Şifreli metin: ",x.encrypt(duzmetin),"\n")
    elif kontrol == "2":
        sifrelimetin = input("Deşifrelenecek metni giriniz: ")
        x = cipher.Cipher()
        print("Deşifre edilmiş metin: ",x.decrypt(sifrelimetin),"\n")
    else:
        print("Hatalı giriş yaptınız, çıkış yapıldı.")
        islem = False