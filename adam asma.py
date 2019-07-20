#adam asma resimleri ayarlama kodlada yazilabilirdi kolaya kacildi (:
resim_0 = [[ "___________ "],
         [ "|","   ","|"],
         [ "|","   ","|"],
         [ "|","   ","O"],
         [ "|","  /","|","\\"],
         [ "|","   ","|",],
         [ "|","  /","  \\"],
         ['_____']]

resim_6=[[ "___________ "],
         [ "|","   ","|"],
         [ "|","   ","|"],
         [ "|","   ",],
         [ "|","   ",],
         [ "|","   ",],
         [ "|","   ",],
         ['_____']]
resim_5=[[ "___________ "],
         [ "|","   ","|"],
         [ "|","   ","|"],
         [ "|","   ","O"],
         [ "|","   ",],
         [ "|","   ",],
         [ "|","   ",],
         ['_____']]
resim_4=[[ "___________ "],
         [ "|","   ","|"],
         [ "|","   ","|"],
         [ "|","   ","O"],
         [ "|","   ","|"],
         [ "|","   ","|"],
         [ "|","   ",],
         ['_____']]
resim_3=[[ "___________ "],
         [ "|","   ","|"],
         [ "|","   ","|"],
         [ "|","   ","O"],
         [ "|","  /","|"],
         [ "|","   ","|"],
         [ "|","   ",],
         ['_____']]
resim_2=[[ "___________ "],
         [ "|","   ","|"],
         [ "|","   ","|"],
         [ "|","   ","O"],
         [ "|","  /","|","\\"],
         [ "|","   ","|"],
         [ "|","   ",],
         ['_____']]
resim_1=[[ "___________ "],
         [ "|","   ","|"],
         [ "|","   ","|"],
         [ "|","   ","O"],
         [ "|","  /","|","\\"],
         [ "|","   ","|"],
         [ "|","  /",],
         ['_____']]



#giris ekrani
print(
        """
__________________________________________________________________
ADAM ASMACA OYUNUNA HOSGELDINIZ
DOGRU TAHMIN ICIN 6 ADET HAKKINIZ BULUNMAKTADIR.
HARFLERI GIRINCE DOGRU HARFLER OTOMATIK YERINI BULUR.SIZE SADECE
TAHMIN ETMEK KALIR.
  ---------------IYI EGLENCELER-----------
             _________
             |      |
             |      |
             |     ***
             |    *   *
             |     ***
             |     /|\\
             |    / | \\         
             |   /  |  \\
             |     / \\
             |    /   \\
             |   /     \\   - - - - - -
oyununuz basliyor.................           
____________________________________________________________________       
                               """,'\n')
#Kelimeleri elle girmektense kayitli olanlarda secelim dedim

sec=['ZONGULDAK','ARI','KANEPE','PORTAKAL','KEHRIBAR',
     'LACIVERT','BEGONYA','ZIL','OYUNCAK','PENALTI']
# oyunun kelimesini hazirlama
while True:
    oyun=input("Kelime secmek icin                                  CIKIS=Q"
              "\nLutfen 0-9 arasi sayi giriniz:")
    if oyun=='Q' or oyun=='q' :
        break
    
    elif oyun.isdigit() and int(oyun) >10 :
        print('------lutfen 0-9 arsinda rakam giriniz-------\n')
        continue
    elif oyun.isdigit() :
        
        liste=sec[int(oyun)]
    
        liste=liste.upper()
        ekran=list(liste)
        adam=list(len(ekran)*'-')
    else:
        print('---------Lutfen sayi giriniz-----------\n')
        continue
    sayac=6
    i=0
   #oyuna baslama  
    while True:
        
        #6 hakki kullanmayi ayarlama ve ekran ciktisi
        
        if sayac==6:
            for e in resim_6:
                print(" "*20, *e,end="\n")
                    
            print('\n',' '*40,*adam)
            print("\n                              ",sayac,"HAKKINIZ KALDI")
        elif sayac==5:
            for e in resim_5:
                 print(" "*20, *e,end="\n")
                   
            print('\n',' '*40,*adam)
            print("                              ",sayac,"HAKKINIZ KALDI")    
       
        elif sayac==4:
            for e in resim_4:
                print(" "*20, *e,end="\n")
                   
            print('\n',' '*40,*adam)
            print("                              ",sayac,"HAKKINIZ KALDI")
        elif sayac==3:
            for e in resim_3:
                print(" "*20, *e,end="\n")
                   
            print('\n',' '*40,*adam)
            print("                              ",sayac,"HAKKINIZ KALDI")
        elif sayac==2:
            for e in resim_2:
                print(" "*20, *e,end="\n")
                   
            print('\n',' '*40,*adam)
            print("                              ",sayac,"HAKKINIZ KALDI")
        elif sayac==1:
            for e in resim_1:
                print(" "*20, *e,end="\n")
                   
            print('\n',' '*40,*adam)
            print("                              ",sayac,"HAKKINIZ KALDI")
        elif sayac==0:
            
            for e in resim_0:
            
                print(" "*20,*e, end="\n")
        
                
            print("\n                 UZGUNUM HAKKINIZ KALMADI")
       
            print('-------oyunu kaybettiniz ------')
            print("Dogru cevap :",*ekran)
            sayac=6
            i=0
            adam=list(len(ekran)*'-')
            print('\n>>>>>>>>>>>>Simdi yeniden baslatiliyor...     ')
            break
       

       #tahmin inputlari
        
        tahmin=input("cikis:Q"
                     "\nLutfen Harf Giriniz:")
        tahmin=tahmin.upper()
       
        if tahmin=='Q':
            print('......GAME OVER......')
            quit()
        elif tahmin.isalpha()==False:
            print('------Lutfen harf giriniz------')
            continue
        elif len(tahmin)>=2:
            print('------Yalnizca harf giriniz------')
            continue
        else:
            
            i=0
            for goster in ekran:
                i+=1
                    
                if tahmin in goster :
                    
                    
                    adam[i-1]=goster
                    
    # oyunun bitis ve basa donmesi
        if ekran[:]==adam[:]:
            print(*ekran,"\n>>>>>>>>>>>>>>>TEBRIKLER KAZANDINIZ>>>>>>>>>>>>>>>.")
            sayac=6
            i=0
            adam=list(len(ekran)*'-')
            print('\nsimdi yeniden baslatiliyor...     ','\n'*4)
            break
                
        # 6 hak kontrolu    
        elif tahmin not in  ekran:
            sayac-=1
            
            continue
       
    
    
        
    
