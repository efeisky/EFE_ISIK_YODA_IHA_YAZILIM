import random

class Person:
    def __init__(self, name, age, tckn):
        self.name = name
        self.age = age
        self.__tckn = tckn

        
    def goster_kisi(self):
        print(f"{self.name} - {self.age} - {self.__tckn}")

class BankAccount:
    def __init__(self, person: Person, account_no, cash):
        self.person = person
        self.account_no = account_no
        self.cash = cash

    def yatir_para(self, yatirilacakMiktar):
        self.cash += yatirilacakMiktar

    
    def cek_para(self, cekilecekMiktar):
        if self.cash >= cekilecekMiktar:
            self.cash -= cekilecekMiktar
        else:
            print("Yeterli bakiye yok, çekim iptal")
        
    def goster_para(self):
        print(f"{self.account_no} - {self.cash:.3f} TL")

exit = 0

person = None
account = None

while exit < 1:
    print("Banka sistemine hoş geldiniz.")
    print("""
    1. Hesap Aç
    2. Para Yatır
    3. Para Çek
    4. Bakiye Göster
    5. Kişi Bilgi Göster
    6. Çıkış
    """)
    process = int(input("Yapmak istediğiniz işlemi seçin (1-6): "))

    if process == 1:
        print("Ad, Yaş ve TCKN gir")
        name = input("AD: ").strip()
        if not name:
            print("HATA: Ad boş olamaz")
            continue
        age = input("YAS: ").strip()
        if not age.isdigit() or int(age) <= 0:
            print("HATA: Yaş pozitif bir tam sayı olmalı")
            continue
        tckn = input("TCKN: ").strip()
        if not tckn.isdigit() or len(tckn) != 11:
            print("HATA: TCKN 11 haneli olmalı")
            continue
        person = Person(name, int(age), tckn)
        account = BankAccount(person, random.randint(0, 1000), 0)

        print("Hesap başarıyla oluşturuldu")

    elif process == 2:
        if account == None:
            print("HATA: Önce hesap oluşturmalısınız")
            continue
        print("Yatırılacak Para")
        miktar = int(input("Miktar: "))
        account.yatir_para(miktar)

    elif process == 3:
        if account == None:
            print("HATA: Önce hesap oluşturmalısınız")
            continue

        print("Çekilecek Para")
        miktar = int(input("Miktar: "))
        account.cek_para(miktar)

    elif process == 4:
        if account == None:
            print("HATA: Önce hesap oluşturmalısınız")
            continue

        print("Bakiye Göster")
        account.goster_para()

    elif process == 5:
        if person == None:
            print("HATA: Önce kişi oluşturmalısınız")
            continue

        print("Kişi Bilgi Göster")
        person.goster_kisi()

    elif process == 6:
        print("Çıkış alındı. Hoşça kalın")
        exit = 1
        break
    else:
        print("HATA: Geçersiz işlem numarası")