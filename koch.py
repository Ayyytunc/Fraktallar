
# coding: utf-8

# # Koch Fraktalı
# Koch kar tanesi fraktalı bir üçgenin her kenarının üçe bölünmesi, ardından orta bölüme bir üçgen çizilmesi aşamalarıyla devam eden bir fractal çeşididir. İsviçreli bilim adamı Niels Fabian Helge von Koch tarafından bulunmuş ve bilim adamının soyadından gelen Koch fraktalı ismini almıştır. Tanımlanan ilk fraktallardan bir tanesidir. Fraktal olarak Kabul edilmesinin sebebi ise bakılan her ölçekte neredeyse aynı görünmesidir.
# Kodumuzun çalışma mantığı şu ki; ilk satırda import komutu ile kütüphanemizi kodda kullanılabilir hale getiriyoruz yani onu aktarıyoruz. Ondan sonra Turtle() fonksiyonu ile bir kaplumbağa oluşturup onu bir değişkene atıyoruz. Aynı şekilde Screen() ile penceremizi yani turtle'ımızın çizim yapacağı alanı bir değişkene atıyoruz. Ardından turtle'ımızın çizim hızını maksimuma getirip fonksiyomuzu oluşturuyoruz. Son olarak fonksiyonumuzu 4 tekrar ve 150 boyutta çizim yapacak şekilde kullanıyoruz ve penceremizin biz onu kapatana kadar açık durmasını sağlayarak kodumuzu bitiriyoruz.

# In[ ]:

import turtle             #import ile kutuphanemizi koda aktardik.

pen = turtle.Turtle()     #Burada turtle'imizi olusturup ona bir isim verdik.
wn = turtle.Screen()      #Ayni sekilde penceremizi bir degiskene atadik.

pen.speed(0)              #Burada turtle'imizin hizini maksimuma getirdik.

def frag(n,sz):           #Burasi kodun en onemli kismi. Burada fonksiyonumuzu tanimladik.
    if(n==1):
        pen.forward(sz)
        pen.left(60)
        pen.forward(sz)
        pen.right(120)
        pen.forward(sz)
        pen.left(60)
        pen.forward(sz)
        return
    frag(n-1,sz/3)
    pen.left(60)
    frag(n-1,sz/3)
    pen.right(120)
    frag(n-1,sz/3)
    pen.left(60)
    frag(n-1,sz/3)
    
frag(4,150)              #Burada da fonksiyonumuzu 4 tekrar ve 150 boyutunda cizim yapacak sekilde kullandik.
wn.mainloop()

