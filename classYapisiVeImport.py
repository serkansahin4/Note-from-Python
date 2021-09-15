# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 00:55:48 2021

@author: fffdf
"""
#%%
#-----------------------------------------------------------------------------------------------
# class lar 


class Matematik: #self kullanmamızın sebebi 
  def __init__(self,a,b): #constructor tanımladık çünkü dışarıdan sadece 2 tane belli değer alacağız.
      self.a=a            #self kullanmamızın sebebi fonksiyonlarımızda değişkenleri sürekli istememek için.
      self.b=b            #normalde metotların içerisinde aynı sınıf içindeki diğer metotları çağıramıyoruz
  def topla(self):        # ama self kullandığımızda çağırabiliyoruz.
    return self.a+self.b
    

  def carp(self):
    return self.a*self.b

  def bol(self,c):
    return self.a/self.b+c

  def cikar(self):
    return self.a-self.b
matematik=Matematik(5,3)

print(matematik.topla())
print(matematik.bol(3))


#%%
# Hem miras veren hemde miras alan sınıfın içerisinde constructor var her ikisindede, bu yüzden miras veren sınıfın
# içindeki constructor ı miras alan sınıfı çağırdığımızda görmüyordu. Problem super() yani base classa dışarıdan aldığımız
# verileri super() komutu ile göndererek çözüldü.
class Person:
    def __init__(self, ad, soyad):
        self.ad = ad
        self.soyad = soyad

class Customer(Person):
    def __init__(self, ad, soyad,yas):
        super().__init__(ad, soyad) 
        self.yas=yas


ogr = Customer("serkan","şahin",15)


#%% 
# Kütüphane import etme
# Moduller dediğimiz aynı klasördeki python dosyası
# as dediğimizde import edilen Moduller dosyasının adının kısaltılmış halini belirtiyoruz.
# kütüphaneyi dahil ettiğimizde kullanım şekli = mm.MODULDEKİHERHANGİBİRNESNE()
# as kullanmadan önce kullanım şekli =  Moduller.MODULDEKİHERHANGİBİRNESNE()

import Moduller as mm
from Moduller import Matematik # Moduller modülünden sadece belirtilen sınıf veya metodu çekme

print("1: Topla")
print("2: Çıkar")
print("3: Böl")
print("4: Çarp")
a=str(input("Bir Operasyon Seçiniz ? "))

sayi1=int(input("1. Sayı = "))
sayi2=int(input("2. Sayı = "))
var=mm.Matematik(sayi1,sayi2)

if a=="1":
    print(var.topla())
if a=="2":
    print(var.cikar())
if a=="3":
    print(var.bol()())
if a=="4":
    print(var.carp()())