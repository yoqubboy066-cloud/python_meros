 # class Phone:
#     def  __init__(self,yili,madel,rangi,xotirasi,narxi):
#         self.yili=yili
#         self.madel=madel
#         self.rangi=rangi
#         self.xotirasi=xotirasi
#         self.narxi=narxi



#     def get_info(self):
#         return f"Telefon madeli : {self.madel}\nTelefon rangi : {self.rangi}\nTelefon xotirasi : {self.xotirasi}\nTelefon narxi : {self.narxi}\ntelefon yili : {self.yili}"
#     # def get_year(self,joriy_yili):
    # def chek_color(self,color):
        # if self.yili>=5:
        #     a=self.narxi-20000
        #     if 15>=color>=5:
        #         y=a-1500
        #         return f" telefon narxi :{y}"
        #     elif color >=35:
        #         a-1500
        #         return f"telefon narxi :{a}"
        #     else:
        #         a=self.narxi-10000
        #         if color==0:
        #             return f"telefon narxi :{a}"
#     def get_price(self,current_year,percentage_of_color):
#         count_year=current_year-self.yili
#         if count_year>=5:
#             self.price-=10000
#         else:
#             self.price-=5000

#         if percentage_of_color!=0:
#             self.price=self.price-self.price*percentage_of_color*2/100
#         else:
#             self.price

#         return f"{self.name} ning yili "   

              
        

# phone1= Phone(2009,"samsungA32","Qora",64,280000000)
# print(phone1.get_info())

# class Mahsulot:
#     def __init__(self,mahsulot_nomi,mahsulot_narxi,mahsulot_turi):
#         self.name=mahsulot_nomi
#         self.price=mahsulot_narxi
#         self.turi=mahsulot_turi
    
#     def get_info(self):
#         return f"mahsulot nomi : {self.name}\nmaxsulot narxi : {self.price}\nmaxsulot turi : {self.turi}"
    
# class sut_maxsulotlari(Mahsulot):
#     def __init__(self, mahsulot_nomi, mahsulot_narxi, mahsulot_turi,litr):
#         super().__init__(mahsulot_nomi, mahsulot_narxi, mahsulot_turi)
#         self.litr=litr
    
#     def get_info_sut(self):
#         return f"{self.get_info()}mahsulotida dokonda {self.litr} litr bor"
    

# class shakar(Mahsulot):
#     def __init__(self, mahsulot_nomi, mahsulot_narxi, mahsulot_turi,kg):
#         super().__init__(mahsulot_nomi, mahsulot_narxi, mahsulot_turi)
#         self.kg=kg

#     def get_data(self):
#         return f"{self.get_info()}{self.kg} kilogram bor"
    


# halimaxon=sut_maxsulotlari("sut",10000,'sut mahsulotlari',50)
# ozoda=shakar('shakar',2000,'kandolatchilik mahsulotlari',100)

# print(halimaxon.get_info_sut())
# print(ozoda.get_data())

# 6
# class ustoz:
#     def __init__(self,ism,familiya,yosh,fan):
#         self.ism=ism
#         self.familiya=familiya
#         self.yosh=yosh
#         self.fan=fan

#     def get_info(self):
#         return f"ustoz ismi : {self.ism}\nustoz familiyasi : {self.familiya}\nustoz yoshi : {self.yosh}\nustoz fani : {self.fan}"
# class IT (ustoz):
#     def __init__(self, ism, familiya, yosh, fan):
#         super().__init__(ism, familiya, yosh, fan)

# IT_ustoz=IT("yoqubboy","bagandikov",9999,"IT mutaxasisligi")
# print(IT_ustoz.get_info())

# 5
# class Talaba:
#     def __init__(self,ism,yoshi,darajasi):
#         self.ism=ism
#         self.yosh=yoshi
#         self.daraja=darajasi

#     def get_info(self):
#         return f"talaba ismi : {self.ism}\ntalaba yoshi : {self.yosh}\ntalaba darajasi : {self.daraja}"
# class Bakalavr (Talaba):
#     def __init__(self, ism, yoshi, darajasi):
#         super().__init__(ism, yoshi, darajasi)  
# talaba1=Talaba("yoqubboy",20,"bakalavr")
# print(talaba1.get_info())


# class Magistr (Talaba):
#     def __init__(self, ism, yoshi, darajasi):
#         super().__init__(ism, yoshi, darajasi)
# talaba2=Talaba("vali",20,"magistr")
# print(talaba2.get_info())


# 7
# class Texnika:
#     def __init__(self,nomi):
#         self.nomi=nomi

#     def get_info(self):
#         return f"texnika nomi : {self.nomi}"
        
# class Kompyuter (Texnika):
#     def __init__(self, nomi,turi,tasfir_formati):
#         super().__init__(nomi,turi,tasfir_formati)
#         self.tasfir_formati=tasfir_formati
    
#     def get_info2(self):
#         return f"Texnika nomi : {self.nomi}\nTexnika tasfir formati : {self.tasfir_formati}"
# Kompyuter1=Kompyuter("kompuyuter","asus","4k")
# print(Kompyuter1.get_info())

# 8
# class Kompyuter:
#     def __init__(self,nomi,rangi):
#         self.nomi=nomi
#         self.rang=rangi
    
#     def get_info(self):
#         return f"Kompyuter nomi : {self.nomi}\nKompyuter rangi : {self.rang}"
# class noutbok(Kompyuter):
#     def __init__(self, nomi, rangi,sensiri):
#         super().__init__(nomi, rangi, sensiri)
# noutbok1=noutbok("hp","qora","sensri bor")
# print(noutbok1.get_info())

# 9
# class Shaxs:
#     def __init__(self,kasb,yoshi,darajasi):
#         self.yosh=yoshi
#         self.daraja=darajasi
#         self.kasb=kasb

#     def get_info(self):
#         return f"Shaxs kasbi : {self.kasb}\nShaxs yoshi : {self.yosh}\nShaxs darjasi : {self.daraja}"
    
# class Oqituvchi(Shaxs):
#     def __init__(self, kasb, yoshi, darajasi):
#         super().__init__(kasb, yoshi, darajasi)
# shaxs=Shaxs("O‘qituvchi ",34,"magistr")
# print(shaxs.get_info())

# 10
# class Mashina:
#     def __init__(self,turi,vazni,rang):
#         self.tur=turi
#         self.vazn=vazni
#         self.rang=rang
         
#     def get_info(self):
#         return f"Mashina turi : {self.tur}\nMashina vazni : {self.vazn} tona\nMashina rangi : {self.rang}"
    
# class YukMashina(Mashina):
#     def __init__(self, turi, vazni, rang,narxi):
#         super().__init__(turi, vazni, rang)
#         self.narx=narxi
#     def get_info2(self):
#         return f"YukMashina turi : {self.tur}\nYukMashina vazni : {self.vazn} tona \nYukmashina rangi : {self.rang}\nYukMashina narxi : {self.narx}"
    
# mashina=Mashina("yengil mashina",1.5,"qora")
# print(mashina.get_info())
# yukmashina=YukMashina("ogir vazinli",3.5,"Oq","170000$")
# print(yukmashina.get_info2())
# 11
# class  Uchuvchi:
#     def __init__(self,ismi,familiyasi,yoshi):
#         self.ism=ismi
#         self.familiya=familiyasi
#         self.yosh=yoshi
#     def get_info(self):
#         return f"Uchuvchi ismi : {self.ism}\nUchuvchi familiyasi : {self.familiya}\nUchuvchi yoshi : {self.yosh}"
# class HarbiyUchuvchi(Uchuvchi):
#     def __init__(self, ismi, familiyasi, yoshi,samolyot_modeli):
#         super().__init__(ismi, familiyasi, yoshi)
#         self.modeli=samolyot_modeli
#     def get_info2(self):
#         return f"Samolyot modeli : {self.modeli}\n{self.get_info()}" 
# samolyot=HarbiyUchuvchi("yoqubboy","bagandikov",20,"F-22 Raptor")
# print(samolyot.get_info2())

# 12
# class Kitob:
#     def __init__(self,nomi,muallifi,yili):
#         self.nomi=nomi
#         self.muallifi=muallifi
#         self.yili=yili
#     def get_info(self):
#         return f"Kitob nomi : {self.nomi}\nKitob muallifi : {self.muallifi}\nKitob yili : {self.yili}"
# class Darslik(Kitob):
#     def __init__(self, nomi, muallifi, yili,sahifa_soni):
#         super().__init__(nomi, muallifi, yili)
#         self.sahifa_soni=sahifa_soni
#     def get_ifno(self):
#         return f"Darslik nomi : {self.nomi}\nDarslik muallifi ; {self.muallifi}\nDarslik yili : {self.yili}\nDarslik sahifasi : {self.sahifa_soni}"
    
# kitob=Kitob("o'tgan kunlar","yoqubboy",1999)
# print(kitob.get_info())
# kitob1=Darslik("informatika","yoqubboy",1999,500)
# print(kitob1.get_info())

# 13
# class Hayvon:
#     def Ovoz(self):
#         return "hayvon turli hil ovoz chiqaradi"
    
# class Mushuk(Hayvon):
#     def Ovoz(self,Mushuk):
#         return super().Ovoz(Mushuk)
    
# class It(Hayvon):
#     def Ovoz(self,It):
#         return super().Ovoz(It)
    
# mushuk=Mushuk()
# it=It()
# print(mushuk.Ovoz("miyov-miyov"),it.Ovoz("vov-vov"))
# 14
# class Qurilma:
#     def __init__(self,turi,narxi,nomi):
#         self.turi=turi
#         self.nom=nomi
#         self.narx=narxi


#     def get_info(self):
#         return f"Qurilma nomi : {self.nom}\nQurilma turi : {self.turi}\nQurilma narxi : {self.narx}"

# class Telefon(Qurilma):
#     def __init__(self,nomi,narxi,turi, xotirasi,quvatilash_soati):
#         super().__init__(turi,nomi,narxi)
#         self.quvat=quvatilash_soati
#         self.xotira=xotirasi

#     def get_info2(self):
#         return f"Telefon turi : {self.turi}\nTelefon nomi : {self.nom}\nTelefon narxi : {self.narx}\nTelefon xotirasi : {self.xotira} GB\nTelefon quvatlash soati : {self.quvat} soat"
    
# class Noutbuk(Qurilma):
#     def __init__(self, turi, narxi, nomi,xotirasi,tasfir_formati):
#         super().__init__(turi, narxi, nomi)
#         self.xotira=xotirasi
#         self.tasfir=tasfir_formati

#     def get_info3(self):
#         return f"Noutbuk nomi : {self.nom}\nNoutbuk narxi : {self.narx}\nNoutbuk turi : {self.turi}\nNoutbuk xotirasi : {self.xotira}\nNoutbuk tasfir_formati : {self.tasfir}"
    
# qurilma=Qurilma("artel","500$","kir yuvish mashinasi")
# telefon=Telefon("samsungA36","250$","samsung",126,1.3)
# noutbuk=Noutbuk("asus","600$","ASUS ROG","1Tr","4k")
# print(qurilma.get_info(),telefon.get_info2(),noutbuk.get_info3())

# 15
# class Kompanya:
#     def __init__(self,oylik_daromad,ishlash_sohasi):
#         self.oylik=oylik_daromad
#         self.soha=ishlash_sohasi

#     def get_info(self):
#         return f"Kompanyaning oylik daromadi : {self.oylik}\nKompanyaning ishlash sohasi : {self.soha}\n"
    
# class Ishchi(Kompanya):
#     def __init__(self, oylik_daromad, ishlash_sohasi,ish_vaqti):
#         super().__init__(oylik_daromad, ishlash_sohasi)
#         self.ish_vaqti=ish_vaqti

#     def get_info2(self):
#         return f"Ishchining oylik daromadi : {self.oylik}\nIshchining ishlash sohasi : {self.soha}\nIshchining ish vaqti : {self.ish_vaqti}"
    
# kompanya=Kompanya("1000000$","ishlab chiqarish")
# ishchi=Ishchi("100$","ishlab ciqarish","tongi 8 dan kechgi 6 gacha")
# print(kompanya.get_info(),ishchi.get_info2())


# 16 
# class Avto:
#     def __init__(self,avtomobil_turi,tezlik,vazn):
#         self.avto_turi=avtomobil_turi
#         self.tezlik=tezlik
#         self.vazn=vazn
#     def get_info(self):
#         return f"Avtomobil turi : {self.avto_turi}\nAvtomobil tazliki : {self.tezlik}\nAvtomobil vazni : {self.vazn}"
# class Nexi(Avto):
#     def __init__(self, tormiz_tizimi, tezlik, vazn,):
#         super().__init__(tormiz_tizimi, tezlik, vazn) 
#         self.tormz=tormiz_tizimi

#     def get_info2(self):
#         return f"Nexi tormz tizimi : {self.tormz}\nNexi tezliki : {self.tezlik}\nNexi vazni : {self.vazn}"

# avto=Avto("malibu",150,"1.1tona")
# nexi=Nexi("yo'q",110,"1 tona")    
# print(avto.get_info())
# print(nexi.get_info2()) 


# 17
# class Transport:
#     def __init__(self,vazn,tezlik):
#         self.vazn=vazn
#         self.tezlik=tezlik

#     def get_info(self):
#         return f"Transport vazni : {self.vazn}\nTransport tezliki : {self.tezlik}"
    
# class Avtobus(Transport):
#     def __init__(self, vazn, tezlik,orindiq_soni):
#         super().__init__(vazn, tezlik)
#         self.orindiq=orindiq_soni

#     def get_info2(self):
#         return f"Avtobus vazni : {self.vazn}\nAvtobus : {self.tezlik}\nAvtobusdagi orindiqlar soni : {self.orindiq}"

# class Poyezd(Transport):
#     def __init__(self, vazn, tezlik,vagonlar_soni):
#         super().__init__(vazn, tezlik)
#         self.vagon=vagonlar_soni
    
#     def get_info3(self):
#         return f"Poyezd tezliki : {self.tezlik}\nPoyezd vagonlar soni : {self.vagon} ta\nPoyezd vani : {self.vazn}"
    
# transport=Transport("1.5 tona",150)
# avtobus=Avtobus("1.2 tona",130,16)
# poyezd=Poyezd(3.3,700,5)

# 18
# class Shaxs:
#     def __init__(self,ismi,familyasi,yoshi):
#         self.ism=ismi
#         self.familya=familyasi
#         self.yosh=yoshi

#     def get_info(self):
#         return f"Shaxs ismi : {self.ism}\nShaxs familyasi : {self.familya}\nShaxs yoshi : {self.yosh}"
    
# class Talaba(Shaxs):
#     def __init__(self, ismi, familyasi, yoshi,nechanchi_kurs):
#         super().__init__(ismi, familyasi, yoshi)
#         self.kurs=nechanchi_kurs

#     def get_info2(self):
#         return f"Talaba ismi : {self.ism}\nTalaba familyasi : {self.familya}\nTalaba yoshi : {self.yosh}\nTalaba nechanchi kursda o'qiydi : {self.kurs}  kursda da o'qiydi"

# class Oqituvchi(Shaxs):
#     def __init__(self, ismi, familyasi, yoshi,fani):
#         super().__init__(ismi, familyasi, yoshi)
#         self.fan=fani

#     def get_info3(self):
#         return f"O'qituvchi : {self.ism}\nO'qituvchi familyasi : {self.familya}\nO'qituvchi yoshi : {self.yosh}\nO'qituvchi fani : {self.fan}"
    
# shaxs=Shaxs("yoqubboy","bagandikov",20)
# talaba=Talaba("yoqubboy","bagandikov",20,2)   
# oqituvchi=Oqituvchi("yoqubboy","bagandikov",25,"informatika") 
# print(shaxs.get_info())
# print(talaba.get_info2())
# print(oqituvchi.get_info3())

# 19
# class Maxsulot:
#     def __init__(self,maxsulot_nomi,maxsulot_narxi):
#         self.nom=maxsulot_nomi
#         self.narx=maxsulot_narxi

#     def get_info(self):
#         return f"Maxsulot nomi : {self.nom}\nMaxsulot narxi : {self.narx}"

# class Meva(Maxsulot):
#     def __init__(self, maxsulot_nomi, maxsulot_narxi,maxsulot_sifat):
#         super().__init__(maxsulot_nomi, maxsulot_narxi)
#         self.sifat=maxsulot_sifat

#     def get_info2(self):
#         return f"Meva nomi : {self.nom}\nMeva narxi : {self.narx}\nMeva sifati : {self.sifat}"
    
# maxsulot=Maxsulot("kompuyuter",5000000000)
# meva=Meva("olma",99999,"yesang olasan degan sifat")
# print(maxsulot.get_info())
# print(meva.get_info2())
# 20
# class Bino:
#     def __init__(self,qavat,hona_soni):
#         self.qavat=qavat
#         self.hona=hona_soni

#     def get_info(self):
#         return f"Bino qavati : {self.qavat}\nBino dagi honalar soni soni : {self.hona}"

# class Uy(Bino):
#     def __init__(self, qavat, hona_soni):
#         super().__init__(qavat, hona_soni)

#     def get_info2(self):
#         return f"Uy qavat : {self.qavat}\nUy honalar soni : {self.hona}"
    
# bino=Bino(6,4)
# uy=Uy(2,8)
# print(bino.get_info())
# print(uy.get_info2())
