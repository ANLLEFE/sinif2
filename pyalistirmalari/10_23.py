#tuple dedıgımız sey dırekt degıstırılemez lısteler dır
#parantez ıcınde tanımlanır
t = (1, 2, "Babayla zor yarısırlar",  3, 4, 5)
print(t)
t.index(1)#ındex fonksıyonu ıle bır eleman ıncısını ogrenebılırız
print(t[2])
###################################t
a_tuple = (1, 2, 3, 4, 5 , "BABAYLA ZOR YARISIRLAR")
print(a_tuple[1:4])  # Dilimleme işlemi 1'den 4'e kadar (4 dahil değil)
print(a_tuple[-3:])   # Son üç elemanı alır
print(a_tuple[:3])    # İlk üç elemanı alır
print(a_tuple[5][5])     # 5. elemanın 5.karakterını alır burası cokomellı 
#####################################
print(a_tuple + t) # İki tuple'ı birleştirir
#####################################
isimler_tuple = ("Ali", "Veli", "Ayşe") 
soyadlar_tuple = ("Yılmaz", "Kara", "Demir")
tam_isimler = isimler_tuple + soyadlar_tuple
print(tam_isimler)
#####################################
print(isimler_tuple + soyadlar_tuple)
#####################################
##################################
#tuple ııcndekı bılgılerı carparsak tekrarlmaıs oluruz 
print(t * 3 )#t tuple ını 3 kere tekrarlatır BABAYLA HEP ZOR YARISIRLAR 
##################################
a = 1, 2 ,(3,4)
b , c , d = a #tuple unpacking b=1 c=2 d=(3,4)
print(d[-10:1])
#sınavda boyle bır soru gelecek  
a = ( 1,2 ,(3,4))
b= a,5,6
print(b)
##################################
a = 1,2,3,4 
x, *xs = a
y = xs[-1]
print(y)