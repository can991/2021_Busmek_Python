#!/usr/bin/env python
# coding: utf-8

# In[10]:


#klavyeden girilen değerler ile matematiksel işlemler yapma

a = int(input("Kısa kenar uzunluğunu giriniz:\t"))
b = int(input("Uzun kenar uzunluğunu giriniz:\t"))

c = (a*b)
d = (2*(a+b))

print("Dikdörgenin Alanı\t", c,"mm2")
print("Dikdörgenin Çevresi\t",d,"mm")


# In[11]:


#Range komutu ve koşul koyarak istenen değerleri yazdırma ve uygun değerlerin toplamını yazdırma

toplam = 0
for x in range(1,50):
    if x%7==0:
        print(x)
        toplam=toplam+x
print("7'ye bölünebilen sayıların toplamı\t",toplam)


# In[12]:


#Klaveyeden sayı girme, bu sayılar ile range belirleme
#koşul koyarak istenen değerleri yazdırma ve uygun değerlerin toplamını yazdırma

a = int(input("Klavyeden bir sayı giriniz\t"))
b = int(input("Klavyeden ikinci sayıyı giriniz\t"))

toplam= 0
for x in range(a,b):
    if x%2==0:
        print(x)
        toplam=toplam+x
print("Çiftsayıların Toplamı\t",toplam)


# In[19]:


#while döngüsü örneği

x=0

while x<6:
    x=x+1
    print(x)


# In[27]:


#listeye append komutu ile klavyeden girelen değeri listeye ekleme

liste = ["C","C++","C#"]
liste.append(input("Bir programlama dili ekleyiniz:\t"))
print(liste)


# In[28]:


#listeden remove komutu ve klavyeden değer girerek eleman çıkarma

liste = ["C","C++","C#"]
liste.remove(input("Bir programlama dili cıkarınız:\t"))
print(liste)


# In[9]:


#liste oluşturma ve klavyeden yeni liste elemanı ekleme
#baş harfa göre sort etme ve listeyi tekrar yazdırma

liste = ["c","C++","C#"]
liste.append(input("Bir programlama dili ekleyiniz:\t"))
liste.sort()
print(liste)


# In[9]:


#append ve input komutu ile listeye klavyeden eleman ekleme

liste = [1,9,8]
liste.append(int(input("Bir sayi giriniz:\t")))
print(liste)


# In[5]:


#upper komutu ile harflerin tamamını büyütme

liste = "Ali"
liste.upper()


# In[18]:


#liste oluşturma , listeye klavyeden sayı ekleme ve
#listedeki sayıları küçükten büyüğe sıralama

liste = [1,9,8]
liste.append(int(input("Bir sayi giriniz:\t")))
liste.sort(reverse=True)
print(liste)


# In[5]:


#Liste içine 5 adet sayı girişi yap
#Listeyi yazdır
#Sonra listedeki çift sayıları liste şeklinde ekrana yazdır

liste = []
while len(liste)<5:
    liste.append(int(input("Bir sayı giriniz\t")))

for x in liste:
    if x%2!=0:
        liste.remove(x)
print("çift sayılar listesi",liste)   


# In[4]:


#def komutu ile klavyeden girilen sayı ile işlem yapma

sayi = int(input("Bir sayı giriniz\t"))
def kare():
    kar=sayi*sayi
    print("Girilen sayinin karesi",kar)  
kare()
  


# In[9]:


#Klaveyden sayi ve işlem tipi girip sayilara girilen koşula göre işlem yaptırma

def dortislem():
    sayi1 = int(input("Bir sayı giriniz\t"))
    sayi2 = int(input("Bir sayı giriniz\t"))

    islem = input("4 işlem'den birini seçiniz :\t (+ - * /)")

    if (islem =="+"):
        print("Toplama\t",sayi1+sayi2)
                
    elif (islem =="-"):
        print("Cıkarma\t",sayi1-sayi2)
        
    elif (islem =="*"):
        print("Carpma\t",sayi1*sayi2)
               
    elif (islem =="/"):
        print("Bölme\t",sayi1/sayi2)
                
    else:
        print("Hatalı Karakter Girdiniz")
dortislem()


# In[ ]:




