# NOT: İsimler rastgele yazılmıştır!

liste = ["Ahmet Deli","Veli Topal","Zeki Nur","Kasım Sadık"]

def Add_Eleman():
    add = input("Elemanın adı: ")
    soyadd = input("Elemanın soyadı: ")
    tamad = add + " " +soyadd
    liste.append(tamad)
def Show_Eleman():
    mod_add = input("Moderatörün adı: ")
    mod_soyadd = input("Moderatörün soyadı: ")
    mod_tamad = mod_add + " " + mod_soyadd
    
    indexno = 0
    indexno2 = 0
    for eleman in liste:
        ad, soyad = eleman.split()[0], eleman.split()[1]
        if (eleman == mod_tamad):
            indexno2 += 1
            print("{}. moderatörün adı {} soyadı {}".format(indexno2, ad, soyad))
        else:
            indexno += 1
            print("{}. elemanın adı {} soyadı {}".format(indexno, ad, soyad))
        
Add_Eleman()
Show_Eleman()
