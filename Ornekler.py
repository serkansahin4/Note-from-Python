# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 20:07:38 2021

@author: fffdf
"""

#__________________________________________________________________
#substring fonksiyonu ( Metin kesmeye yarıyor )

metin="Merhaba Dünya"
print(metin[1:2]) # Burada 1 kaçıncı karakterden başlayacağı, 2 ise kaçıncı karaktere kadar gideceği
print(metin[1:]) # Burada 1. karakterden sonrasını al demek
print(metin[:1]) # Burada 1. karakterden öncesini al demek


#__________________________________________________________________
# len fonksiyonu

metin="Merhaba Dünya"
print(len(metin)) # metnin uzunluğunu verir

#__________________________________________________________________
# lower() - upper() Fonksiyonu

metin="Merhaba Dünya"
print(metin.lower()) # Metni Küçültür
print(metin.upper()) # Metni Büyültür

#__________________________________________________________________
# replace("x","y") fonksiyonu 

metin="Merhaba Dünya"
print(metin.replace("a","b")) # metindeki a harflerini b harfine dönüştürür

#__________________________________________________________________
# split() ve strip() Fonksiyonları

metin="Merhaba   Dünya "
print(metin.split(';')) #metni noktalı virgüle göre ayır demek
print(metin.split(';')[0]) #metni noktalı virgüle göre ayır 1.elemanı yazdır demek
print(metin.strip())# metindeki boşlukları siler default olarak
print(metin.sort()) # kelimeleri a dan z ye sıralar ama önce split() yaparak kelime kelime ayrıştırmak gerekiyor.




#__________________________________________________________________
# Önemli Bilgi REFERANS TİP

kelime=["selamke"," devamke"]
kelime2=kelime # Referans tiplerde ram üzerindeki numaraya atama yapılır
kelime2.pop(0) # Bu yüzden kelime yi kelime2 ye atadığımızda kelime2 den bir veri sildiğimizde
print(kelime)  # kelimedeki veriyi silmiş oluyoruz.

               # Bu yüzden copy() diye bir fonksiyon ile kelime listesini kopyalıyoruz.

kelime=["selamke"," devamke"]
kelime2=kelime.copy() # kelime listesinin kopyası kelime2 ye atandığı için
kelime2.pop(0)        # ram üzerinde kelime 2 ye kelimenin indexi değil farklı bir index ataması yapılıyor.
print(kelime)





#__________________________________________________________________
# list(()) ler []

liste= list(("selam",2,"selsm"))
liste.append("sak") # Listeye veri ekleme
liste.remove("selam") # Listeden ada göre veri silme
liste.pop(1) # Listeden indexe göre veri silme
liste.insert(0,"serkan") # Listeye index numarasını belirterek veri ekleyip veri kaydırma
liste.reverse() # listeyi tersine çevirme

liste2=list(("murat",5,"selamı"))
liste.extend(liste2)   # liste adlı list imize liste2 deki verileri ekler extend()
#liste.sort() # Listeyi küçükten büyüğe sıralamaya yarar
#liste.sort().reverse() # Listeyi a dan z ye sıralar ve listeyi tersine çevirerek büyükten küçüğe sıralamış olur.
print(liste)

#__________________________________________________________________
# Tuple() lar İçerisindeki verilerin değişmediği bi liste türü ve sistem hızı açısından avantaj sağlar nadir kullanılır
                          # Tuple ve liste arasındaki fark tupellar () parantez içerisinde veri girişi alır listeler ise [] köşeli parantez içerisinde.
tuples=('selam','cow',5)

print(tuples)
                          #Tuple kullanılırken oluşturulan tuple içerisinde bi tane veri varsa o verinin type sını algılamaz. bu yüzden
                          # ("serkan",) sonuna virgül bırakılır.

#__________________________________________________________________
# set{} unique elemanlar içerir. İçerisindeki verilere index erişimi sağlayamayız kafasına göre sıralama yeteneği vardır.

setter = {"serkan",2,"mah"}

for x in setter:
    print(x)
    
if "serkan" in setter:  # setterin içinde "serkan" varmı? "in" kullandığımızda true yada false döndürür. 
    print("Listede Var")

setter.add("serjkan") # sete veri ekleme
setter.update(["serkan",3]) # sete toplu veri ekleme
print(setter)

setter.remove("serkan") # setterden veri silme
setter.discard("serkan")#setterda olmayan veriyi silerken hata verir. bu yüzden remove() yerine discard() fonksiyonu kullanılır.
setter.clear() # setin içindekileri komple siler.
del setter # setteri komple hafızadan siler.

                    # iki tane set listesini birleştirmeye çalıştığımızda birbirine benzer dataları tek dataya indirmek için union yada | pipe işareti kullanılır
setA = {1,2,3,4,5}
setB = {3,4,5,6,7}
print(setA|setB)    # iki set teki ortak elemanları tek elemanmış gibi gösterir unionda farklı bir kullanım örneğidir aynı işlevi görür. 
print(setA.union(setB))

                    # iki tane setin sadece ortak noktasını almak için intersection() yada & işareti kullanılır
print(setA&setB)
print(setA.intersection(setB))

                    
print(setA-setB)             # iki tane setin birbirinden farkını almak için difference() yada - işareti kullanılır.
print(setA.difference(setB)) # iki tane setin birbirinden farkını almak için


print(setA^setB) # iki tane setin ortak noktası dışındakileri(farklarını) almak için symmetric_difference() yada ^ işareti kullanılır.
print(setA.symmetric_difference(setB)) # 

#__________________________________________________________________
# Metotlar def xxx()    ve lambda fonksiyonu

def metotadi():
    print("sen kimsin ula")

def metotadi(a,b):
    print(a+b)
    
def metotadi(a,b):
    return a+b
#%%
             # lambda fonksiyonu daha kısa bir metot tarzıdır ama fonksiyondur. metot işlevi görür.
hesapla=lambda a,b: a*b # a,b dediğimiz yer def metodundaki gibi parametre aldığı yer ":" dan sonrasıda return edilen blok.
print("kullanımı = "+str(hesapla(5,3)))

#%% Faktöriyel hesaplama
sayigir=int(input("Sayı Giriniz = "))
toplam=1

for x in range(1,sayigir+1,1):
  toplam=toplam*x
print(toplam)


#%% matris hesaplama

matris1=[[1,3,5],[2,4,1],[1,5,7]]
matris2=[[3,3,4],[2,4,1],[3,5,4]]
matris3=[[0,0,0],[0,0,0],[0,0,0]]

for x in range(3):
  for y in range(3):
    matris3[x][y]=matris1[x][y]+matris2[x][y]
print(matris3)