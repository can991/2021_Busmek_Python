#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Format komutu String bir ifadenin içine değişken eklememize yardımcı olur

isim = "python"
print("{} derslerini çok severim".format(isim))


# In[2]:


#Birden fazla değeri format komutu ile çağırıp çalıştırma

a = 13
b = 14 
c = a*b

print("{} çarpı {} , {} eder.".format(a,b,c))


# In[3]:


#klavyeden sayı girip, sayının tek mi çift olduğunu yazdırma

sayi = int(input("Bir sayı giriniz:\t"))
if (sayi%2==0):
    print("{} sayisi çifttir".format(sayi))
else:
    print("{} sayisi tektir".format(sayi))  


# In[4]:


#Klavyeden vize ve final notlarını girip ortalamasını yazdırma

vize = int(input("Vize notunu giriniz:\t"))
final = int(input("Final notunu giriniz:\t"))

ort = (vize+final)/2


# In[15]:


#Format komutu içinde birden fazla değişkeni kullanma örneği

vize = int(input("Vize notunu giriniz:\t"))
final = int(input("Final notunu giriniz:\t"))

ort = (vize+final)/2

if (ort > 49):
    print("Geçti")
else:
    print("Kaldı")
    
print("ortalama: ",round(ort,3))

print("öğrencinin vize notu {} ve final notu {} ve ortalaması {}".format(vize,final,ort))


# In[17]:


#klavyeden vize ve final notunu girip ve,
#format komutu kullanarak notları ve ortalamayı yazdırma ve
# ortalamaya göre geçip geçmediğini yazdırma

vize = int(input("Vize notunu giriniz:\t"))
final = int(input("Final notunu giriniz:\t"))

ort = (vize+final)/2

if (ort > 49):
    print("öğrencinin vize notu {} ve final notu {} ve ortalaması {}".format(vize,final,ort),"GEÇTİNİZ")
else:
    print("öğrencinin vize notu {} ve final notu {} ve ortalaması {}".format(vize,final,ort),"KALDINIZ")  


# In[1]:


#klavyeden vize ve final notunu girip ve,
#format komutu kullanarak notları ve ortalamayı yazdırma ve
# ortalamaya göre harf notunu yazdırma

isim = input("öğrencinin ismi\t")
vize = int(input("Vize notunu giriniz:\t"))
final = int(input("Final notunu giriniz:\t"))


ort = (vize+final)/2

if ort > 85:
    print("öğrencinin ismi {} \nOrtalaması {}".format(isim,ort),"\nGEÇTİ \nHARF NOTU: AA")
elif ort > 70:
    print("öğrencinin ismi {} \nOrtalaması {}".format(isim,ort),"\nGEÇTİ \nHARF NOTU: BB")
elif ort > 55:
    print("öğrencinin ismi {} \nOrtalaması {}".format(isim,ort),"\nGEÇTİ \nHARF NOTU: CC")
else:
    print("öğrencinin ismi {} \nOrtalaması {}".format(isim,ort),"\nKALDI \nHARF NOTU: FF") 


# In[24]:


#liste oluşturup, liste içindeki elemanları yazdırma

sayilar = [1,2,3,4,5]
for x in sayilar:
    print(x,"python")


# In[9]:


#for döngüsü ile istenilen aralıktaki sayıları range komutu ile yazdırma

for x in range(1,11,5):
    print(x)


# In[26]:


#liste oluşturup bu listeye koşul ekleyip istenilen değeleri yazdırma

sayi=[1,2,3,4,5,6,7]

for x in sayi:
    if(x>3):
        print(x)       


# In[72]:


#liste oluşturup bu listeye koşul ekleyip istenilen değeleri yazdırma
sayi=[1,2,3,4,5,6,7,8]

for x in sayi:
    if(x>3):
        if(x%2==0):
            print(x)        


# In[68]:


#klavyyeden saati ve dakikayı girme
#girilen değeri dakika ve saniyeye çevirme
#format komutunu kullanma

saat = int(input("Saat kaç:\t"))
dak = int(input("Kaç geçiyor:\t"))

dakika = (saat*60)+dak
saniye = (saat*3600)+(dak*60)

print("{} saat ve {} dakika --> {} dakika ve {} saniye ".format(saat,dak,dakika,saniye))


# In[70]:


#klavyeden sayılar girme ve range oluşturma
#çift sayıları bulma ve toplamını yazdırma

toplam = 0
sayi1 = int(input("Birinci Sayiyi Giriniz:\t"))
sayi2 = int(input("ikinci Sayiyi Giriniz:\t"))
for x in range(sayi1,sayi2):
    if x%2==0:
        print(x)
        toplam=toplam+x
print("çift sayiların toplamı",toplam)  


# In[48]:


#klavyeden sayılar girme ve range oluşturma
#Belirlenen koşuldan büyük olanları bulma ve 
#koşula uyan sayıların toplamını yazdırma

sayi1 = int(input("Birinci Sayi Giriniz:\t"))
sayi2 = int(input("İkinci Sayi Giriniz:\t"))

toplam = 0                              

for x in range(sayi1,sayi2): 
    if (x>5):
        toplam = toplam+x
        print(x)
print("Toplam",toplam)


# In[60]:


#break ve continue komutunu kullanarak for döngüsünde işlem yapma
for x in range(0,20):
    if (x>12):
        break
        
    if (x%2==1):
        continue
        
        
    print(x)
 
    
    



# In[64]:


#for döngüsünde aralık oluşturuğ koşula uyan sayıları ve toplamını yazdırma

toplam = 0
for x in range(0,20):
    if (x>12):
        toplam= toplam+x
        print(x)      
print("toplam",toplam)

