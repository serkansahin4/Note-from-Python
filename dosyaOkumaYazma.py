# -*- coding: utf-8 -*-

#
#________________________________________________________________________________________
# open() fonksiyonu dosyalarla alakalı işlemleri yapan bir fonksiyondur
# ("Dosya adı . türü", yapılacak işlem)
# yapılacak işlem "w" burdaki w aslında "write" yani yazdır anlamında
# write komutunun yaptığı işlem, dosya yoksa dosyayı oluştur ve dosya ile işlem yaparken
# içerisine yazılabilir olması özelliğini belirtir.

# bütün komutlar dosya yoksa otomatik oluşturmaya yarar
# w komutu, belirtilen adda dosya yoksa oluşturur ve dosyanın yazılabilirliğini aktif eder (write)
# w komutu, dosyada üzrine yazar yani dosyayı sıfırlar.
# a komutu, dosyanın sadece yazılabilirliğini aktif etme komutudur. (append)
# x komutu, belirtilen adda dosya yoksa oluşturur, varsa hata verir. (create)
# r komutu, dosyayı oku. (read) //// çoğunlukla okuma işlemini kullanıyoruz.

f= open("okunacask.txt","w") # ,"w" yada herhangi bir komut vermeseydik default olarak ,"r" komutu çalışıyor olurdu.

# 3 tane ayrı ayrı kullanım şekli var. birini kullanınca diğerine gerek kalmaz bu kullanım şekillerinin.
print(f.read())   # read() fonksiyonu dosyanın tamamını oku demek


print(f.readline()) # readline() fonksiyonunda kaçtane readline() fonksiyonu yazarsak dosyadaki o kadar satırı okur
print(f.readline()) # readline() 


for x in f:  # not defterindeki her satırı x ile indexler.  yine tamamını okumuş olur.
    print(x)

f.close() # dosyayla işimiz bittiğinde dosyayı kapatmamız gerekiyor.

#%%
f= open("okunacask.txt","w") # ,"w" yada herhangi bir komut vermeseydik default olarak ,"r" komutu çalışıyor olurdu.
f.write("serkan") # "w" komutu kullandığımız için var olan dosyanın içeriğini silip sadece "serkan" yazdı içine


#%%
f= open("okunacask.txt","a") # "a" komutu var olan dosyanın sonuna ekleme yapıyor.
f.write("\n") # boşluk bırak 
f.write("serkan") # 

#%%
f=open("okunacask.txt","x") # belirtilen adda dosya yoksa oluşturur, varsa hata verir. (create)

#%%
# dosya silmek için ise os adında bir kütüphaneden yararlanılır remove() fonksiyonunun içerisine dosya adı yazılır ve o dosya silinir.
import os
os.remove("okunacask.txt")

# Bilgisayardaki bir dosyayı bulmak
if os.path.exists("Ogrenciler.txt"): #
    print("Böyle bir dosya var")
    
# Bilgisayardaki bir klasörü silmek
os.rmdir("Ogrenciler")


#%%
# ÖRNEĞİM ÖRNEĞİM ÖRNEĞİM ÖRNEĞİM ÖRNEĞİM ÖRNEĞİM ÖRNEĞİM ÖRNEĞİM
# -*- coding: utf-8 -*-

listem=[["Serkan","Şahin",22],["Hakan","Şahin",25]]

fileForAppend=open("okunacask.txt","a")
for x in range(len(listem)):
    for y in range(len(listem[0])):
        fileForAppend.write(str(listem[x][y]))
        fileForAppend.write(" ")
    fileForAppend.write("\n")
fileForAppend.close()