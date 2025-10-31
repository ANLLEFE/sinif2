#strings
#stringler tek tirnak , cift tirnak ve uc tirnakla olusturulabilir.
'Anil Efe Cakmak'
"Anil Efe Cakmak"
a = "aliasd"
# print(a[1:5:2])#ilk deger baslagin degeri ikinci deger bitis noktasi sondaki ise atlama degeri 
# print(a[::-1])#bu durumda ise tersden yaziyor 
b = "Merhaba"
# print(len(b))# stringdeki index sayisini verir


c = "Mustafa "
c = c + " Anil Efe"
# print(c)
#############################
#Veri tipi donusumleri 
# #tam sayi > ondalikli sayi 
# a = 43
# print(float(a))
# #ondalikli sayi > tam sayi 
# b = 12.32

# print(int(b))

# #sayilari stringlere donusturme ve ya tam tersi 
# print(str(123))
# a = str(123)
# print(len(a))
# b = str(123.4)#burada nokta dahi karakter sayilir. 
# print(len(b))

a = "123123214asdadsasda"
#############
#Print formatlama 
print("Merhaba\nNasilsin\nIyi misin ")#\n alt satira gecirir. 
print("\t Merhaba\t Naislsin\t Iyi misin ")#\t tab tusuna bastiignda ki boslugu yaratir 
print(type(34))#type kodu ile datanin turunu gosteriyor int mi string mi vb.
print(type("anil"))
print(type(23.23))
print(34,23,23,54,65,sep = "/")# sep kodu ile her bir degerin ardina / koyar 
print(*"SELAM" )# * isareti her bir karakterin arasina bir bosluk birakir 
print(*"SELAM" , sep = "\n")
print("{} {} {}".format(23,"Anil",52))
a = 3
b = 5 
print("'{} + {} = {}' 'a + b nin toplami '".format(a, b , a+b))
print("{2} {1} {0}".format(41,"Anil",53))
print("{:.2f} {:.2f} {:.2f}".format(1.2345,1.2543,2.3453))