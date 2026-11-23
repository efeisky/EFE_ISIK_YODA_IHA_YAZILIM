text = input("İstediğiniz metni giriniz: ")#Kullanıcıdan metin alınır.

text = text.lower()#Aynı kelimelerin tekrarını önlemek için tüm kelimeler küçük harf olarak ayarlanır.

kelimeler_ham = text.split(" ")#Boşluklardan bölünerek kelime listesi alınır.

kelimeler_duzeltilmis = []#Düzeltilmiş kelimelerin olacağı liste.
silinecek_isaretler = ".,!?;"#RegEx gibi kelime metinlerinden silinecek karakterler.
for kelime in kelimeler_ham:
    duzgun_kelime = kelime
    for isaret in silinecek_isaretler: 
        duzgun_kelime = duzgun_kelime.replace(isaret, "")#Kelimeden silinecek kelimeleri çıkar.
    if duzgun_kelime != "":
        kelimeler_duzeltilmis.append(duzgun_kelime)#Duzgun kelimeyi listeye ekle.

kelime_sayi = len(kelimeler_duzeltilmis)#Toplam kelime sayısı hesabı
karakter_sayi = len(text)#Toplam karakter sayısı hesabı

print(f"\nToplam kelime sayısı: {kelime_sayi}")
print(f"Toplam karakter sayısı: {karakter_sayi}\n")


if len(kelimeler_duzeltilmis) > 0:#Duzgun kelime listesinde eleman varsa,
    en_uzun_kelime = max(kelimeler_duzeltilmis, key=len)#Len türünden duzgun kelime listesindeki en büyük kelimeyi bul
    print(f"En uzun kelime: {en_uzun_kelime}, {len(en_uzun_kelime)} karakter\n")#En büyük kelime ve uzunluğunu yazdır
else:
    print("Herhangi bir kelime yok.\n")

kelime_tekrar = dict()#Kelime tekrarı sözlüğü hazırlama 
for kelime in kelimeler_duzeltilmis:
    kelime_tekrar[kelime] = kelime_tekrar.get(kelime, 0) + 1 #Listede varsa +1 yoksa kelimeyi ekleyen kod

print("Kelime tekrar sayıları:")
for kelime, adet in kelime_tekrar.items():
    print(f"    {kelime}: {adet}") #Dictteki kelimeleri for ile alan ve yazdıran satır