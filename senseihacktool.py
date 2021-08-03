# @senseioffical tarafindan yapılmıştır. 
# 4 farklı hack alanında işinize yarayacak araçları kurmak için kullanabilirsiniz.
# hizmet amaçlı hazırlanmıştır. yapılan hiçbir faaliyetten sorumlu değilim.

import os 
import sys
import time 
os.system ("apt update && apt upgrade")
os.system ("clear")

print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
while True:
  print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•             ~SENSEİ OFFİCAL HACK TOOL~          •
•                                                 •
•        [0] Köməkçi paketləri quraşdırmaq üçün   •
•        [1] Məlumat toplama vasitələri           •
•        [2] DDOS Hücum Alətləri                  •
•        [3] Şifrə Qırma Alətləri                 •     
•        [4] Təhlükəsizlik Analizi Alətləri       •
•                                                 •
•        [x] Çıxmaq Üçün                          •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  """)
  
  karar = input ("Nə etmək istəyirsən: ")
  if karar=="x":
    print ("Yenə Gözləyirik...")
    break

  elif karar=="0":
    os.system ("clear")
    print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
    print ("Köməkçi paketlərin quraşdırılır...")
    os.system ("pkg install python -y")
    os.system ("pkg install python2 -y")
    os.system ("pkg install python3 -y")
    os.system ("pkg install curl -y")
    os.system ("pkg install php -y")
    os.system ("pkg install nano -y")
    os.system ("pkg install vim -y")
    os.system ("pkg install cat -y")
    os.system ("pkg install colorama -y")
    os.system ("pkg install figlet -y")
    os.system ("pkg install toilet -y")
    os.system ("pkg install ruby -y")
    os.system ("pkg install perl -y")
    os.system ("pkg install pip")
    os.system ("pkg install pip2")
    os.system ("pkg install pip3")
    os.system ("pkg install tsu")
    print ("Köməkçi paketlər quraşdırılıb.")
    
  elif karar=="1":
    os.system ("clear")
    print ("""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    •                                                •
    •              ~MƏLUMAT TOPLAMA VASİTƏLƏRİ~      •
    •                                                •
    •    [1] Telefon nömrəsindən məlumat toplamaq    •
    •    [2] TR Kimlik Nömrəsi Son 2 Rəqəm Tapmaq    •
    •    [3] IP ünvanından Məkan tapın               •
    •    [4] Veb saytlardan məlumat toplamaq         •
    •    [5] İnstagram hesablardan məlumat toplamaq  •
    •    [6] Adına görə Sosial Media Hesabı Sorğusu  •
    •    [7] Facebook Hesablarından Məlumat Toplamaq •
    •    [8] Mac ünvanları haqqında məlumat toplamaq •
    •    [9] E -poçtdan Məlumat Toplanması           •
    •    [10] Phishing Aləti                         •
    •                                                •
    •    [x] Çıxmaq Üçün                             •
    •                                                •
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)
    karar1 = input ("Nə etmək istəyirsən: ")
    if karar1=="x":
      print ("Yenə Gözləyirik...")
      break  
      
    elif karar1=="1":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("PhoneInfoga Quraşdırılır...")
      os.system ("apt update")
      os.system ("git clone https://github.com/ExpertAnonymous/PhoneInfoga.git")
      print ("PhoneInfoga Quruldu.")
      
    elif karar1=="2":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""") 
      tcnumara = input("TR Kimlik nömrəsinin ilk 9 rəqəmini daxil edin: ")
      def tcno(tcno):
        if len(tcno) == 9:
            a = 7*(int(tcno[0])+int(tcno[2])+int(tcno[4])+int(tcno[6])+int(tcno[8]))
            b = int(tcno[1])+int(tcno[3])+int(tcno[5])+int(tcno[7])
            haneOn = (a-b)%10
            onHaneli=str(tcno)+str(haneOn)
            toplamOn = 0
            for i in range(10):
              toplamOn=toplamOn+int(onHaneli[i])
            haneOnBir = toplamOn%10
            return tcno+str(haneOn)+str(haneOnBir)
      print ("TC Kimlik No'nun Tamı :",tcno(tcnumara))
      
    elif karar1=="3":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("IPGeolocation Qurulur...")
      os.system ("apt update")
      os.system ("git clone https://github.com/maldevel/IPGeoLocation.git")
      print ("IPGeolocation Quruldu.")
      
    elif karar1=="4":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("RED_HAWK Qurulur...")
      os.system ("apt update")
      os.system ("git clone https://github.com/Tuhinshubhra/RED_HAWK.git")
      print ("RED_HAWK Quruldu.")
      
    elif karar1=="5":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("osi.ig Qurulur...")
      os.system ("apt update")
      os.system ("git clone https://github.com/th3unkn0n/osi.ig.git")
      print ("osi.ig Quruldu.")
      
      
    elif karar1=="6":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("userrecon Qurulur...")
      os.system ("apt update")
      os.system ("git clone https://github.com/issamelferkh/userrecon.git")
      print ("userrecon Quruldu.")
      
    elif karar1=="7":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""") 
      print ("OSIF Qurulur...")
      os.system ("apt update")
      os.system ("git clone https://github.com/ciku370/OSIF.git")
      print ("OSIF Quruldu.")
      
    elif karar1=="8":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("mac-lookup Qurulur...")
      os.system ("apt update")
      os.system ("git clone https://github.com/ivan-loh/mac-lookup.git")
      print ("mac-lookup Quruldu.")
      
    elif karar1=="9":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("Infoga Qurulur...")
      os.system ("apt update")
      os.system ("git clone https://github.com/m4ll0k/Infoga.git")
      print ("Infoga Quruldu.")
    
    elif karar1=="10":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("ShellPhish Qurulur...")
      os.system ("apt update")
      os.system ("git clone https://github.com/AbirHasan2005/ShellPhish.git")
      print ("ShellPhish Quruldu.")
      
  elif karar=="2":
    os.system ("clear")
    print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•             ~DDOS HÜCUM VASİTƏLƏRİ~             •
•                                                 •
•        [1] Hammer DDOS Aləti                    •
•        [2] Hulk DDOS Aləti                      •
•        [3] XERXES DDOS Aləti                    •
•        [4] SMS Bomb Aləti                       •
•        [5] Anonim SMS Aləti                     •
•                                                 •
•        [x] Çıxmaq Üçün                          •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
    karar2 = input ("Nə etmək istəyirsən: ")
    if karar2=="x":
      print ("Yenə Gözləyirik...")
      sys.exit()
      
    elif karar2=="1":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""") 
      print ("Hammer Qurulur...")
      os.system ("apt update")
      os.system ("git clone https://github.com/cyweb/hammer.git")   
      print ("Hammer Quruldu.")
      
    elif karar2=="2":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("Hulk Qurulur...")
      os.system ("apt update")
      os.system ("git clone https://github.com/grafov/hulk.git")
      print ("Hulk Quruldu.")
     
    elif karar2=="3":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("XERXES Qurulur...")
      os.system ("apt update")
      os.system ("git clone https://github.com/CyberXCodder/XerXes.git")
      print ("XERXES Quruldu.")
      
    elif karar2=="4":
      os.system ("clear")   
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("Impulse Qurulur...")
      os.system ("apt update")
      os.system ("git clone https://github.com/LimerBoy/Impulse.git")
      print ("Impulse Quruldu.")
    
    elif karar2=="5":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("yubasms Qurulur...")
      os.system ("apt update")
      os.system ("git clone https://github.com/yuba-0/yubasms.git")
      print ("yubasms Quruldu.")
      
  elif karar=="3":
    os.system ("clear")
    print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~ŞİFRƏ QIRMA ALƏTLƏRİ~               •
•                                                 •
•       [1] Hydra Brute Force                     •
•       [2] İnstagram Brute Force                 • 
•       [3] E-mail Brute Force                    •
•       [4] Hash Şifre Qırıcı                     •
•       [5] Wordlist Oluşturucu                   •
•       [6] Instagram Brute Force 2               •
•       [7] HashCat Hash Şifre QKırıcı            •
•       [8] Katak Toolkit                         •
•       [9] Facebook Brute Force                  •
•       [10] Wi-fi Təhlükəsizlik Nəzarəti         •
•                                                 •
•       [x] Çıxmaq Üçün                           •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

""")
    karar3=input ("Nə etmək istəyirsən: ")
    
    if karar3=="x":
      print ("Yenə Gözləyirik...")
      sys.exit()
    elif karar3=="1":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("Hydra Qurulur...")
      os.system ("apt update")
      os.system ("pkg install tsu")
      os.system ("git clone https://github.com/vanhauser-thc/thc-hydra.git")
      print ("Hydra Quruldu.")
      
    elif karar3=="2":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("Instagram Qurulur...")
      os.system ("apt update")
      os.system ("git clone https://github.com/Bitwise-01/Instagram-.git")
      print ("Instagram Quruldu.")
      
    elif karar3=="3":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("Brute-Force-gmail Qurulur...")
      os.system ("apt update")
      os.system ("git clone https://github.com/0xfff0800/Brute-force-gmail.git")
      print ("Brute-Force-gmail Quruldu.")
    
    elif karar3=="4":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("hasher Qurulur...")
      os.system ("apt update")
      os.system ("apt install python2 git")
      os.system ("git clone https://github.com/CiKu370/hasher.git")
      print ("Hasher Quruldu.")
      
    elif karar3=="5":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("cheekyPassListCreator Qurulur...")
      os.system ("git clone https://github.com/mXBozkurt/cheekyPassListCreator.git")
      print ("cheekyPassListCreator Quruldu.")
      
    elif karar3=="6":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("İnstaHack Qurulur...")
      os.system ("apt update")
      os.system ("git clone https://github.com/evildevill/instahack.git")
      print ("İnstaHack Quruldu.")
      
    elif karar3=="7":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("HashCat Qurulur...")
      os.system ("apt update")
      os.system ("git clone https://github.com/hashcat/hashcat.git")
      print ("HashCat Quruldu.")
      
    elif karar3=="8":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("Katak Qurulur...")
      os.system ("apt update && apt upgrade")
      os.system ("apt install git python2")
      os.system ("pip2 install requests progressbar")
      os.system ("git clone https://github.com/Gameye98/Katak.git")
      print ("Katak Quruldu.")
    
    elif karar3=="9":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("FBBrute Qurulur...")
      os.system ("apt install git python2")
      os.system ("git clone https://github.com/Gameye98/FBBrute.git")
      print ("FBBrute Quruldu.")
   
    elif karar3=="10":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("Aircrack-ng Qurulur...")
      os.system ("apt update")
      os.system ("https://github.com/aircrack-ng/aircrack-ng.git")
      print ("Aircrack-ng Quruldu.")
      
  elif karar=="4":
    os.system ("clear")
    print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•        ~TƏHLÜKƏSİZLİK ANALİZİ ALƏTLƏRİ~         •
•                                                 •
•      [1] Nmap Şəbəkə Axtarışı                   •
•      [2] SQLMap Web Sayt Açığı Axtarışı         • 
•      [3] RED_HAWK Web Sayt Açığı Axtarışı       •
•      [4] Easymap Web Sayt Açığı Axtarışı        •
•      [5] AstraNmap Təhlükəsizlik Brauzereri     •
•      [6] SQLscan SQL Açıx Axtarışı              •
•      [7] Wordpresscan wordpres Axtaraşı         •
•      [8] wpscan Wordpres Açıx Axtarışı          •
•      [9] XAttacker Web Site Açıx Axtarışı       •
•      [10] Admin Paneli Tapan                    •
•                                                 •
•       [x] Çıxmaq Üçün                           •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

""")
    karar5 = input ("Nə etmək istəyirsən: ")
    if karar5=="x":
      print ("Yenə Gözləyirik...")
      break
    elif karar5=="1":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("Nmap Qurulur...")
      os.system ("apt update")
      os.system ("pkg install nmap")
      print ("Nmap Quruldu.")
      
    elif karar5=="2":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("SQLMap Qurulur...")
      os.system ("apt update")
      os.system ("git clone https://github.com/sqlmapproject/sqlmap.git")
      print ("SQLMap Quruldu.")
      
    elif karar5=="3":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("RED_HAWK Qurulur...")
      os.system ("apt update")
      os.system ("git clone https://github.com/Tuhinshubhra/RED_HAWK.git")
      print ("RED_HAWK Quruldu.")
      
    elif karar5=="4":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
      print ("Easymap Qurulur...")
      os.system ("clear")
      os.system ("apt update")
      os.system ("git clone https://github.com/Cvar1984/Easymap.git")
      print ("Easymap Quruldu.")
      
    elif karar5=="5":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("AstraNamp Qurulur...")
      os.system ("apt update")
      os.system ("git clone https://github.com/Gameye98/AstraNmap.git")
      print ("AstraNmap Quruldu.")
      
    elif karar5=="6":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("SQLscan Qurulur...")
      os.system ("apt update")
      os.system ("git clone https://github.com/Cvar1984/sqlscan.git")
      print ("SQLscan Quruldu.")
      
    elif karar5=="7":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("Wordpresscan Qurulur...")
      os.system ("apt update")
      os.system ("git clone https://github.com/swisskyrepo/Wordpresscan.git")
      print ("Wordpresscan Quruldu.")
      
    elif karar5=="8":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("wpscan Qurulur...")
      os.system ("apt update")
      os.system ("git clone https://github.com/wpscanteam/wpscan.git")
      print ("wpscan Quruldu.")
      
    elif karar5=="9":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("XAttacker Qurulur...")
      os.system ("apt update")
      os.system ("git clone https://github.com/Moham3dRiahi/XAttacker.git")
      print ("XAttacker Quruldu.")
      
    elif karar5=="10":
      os.system ("clear")
      print ("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
•                                                 •
•            ~SENSEİ OFFİCAL HACK TOOL~           •
•                                                 •
• github: github.com/senseioffical                •
• instagram: Instagram.com/senseioffical          •
• twitter: twitter.com/senseioffical              •
• telegram: t.me/senseioffical                    •
•                                                 •
•                  created by: @senseioffical     •
•                                                 •
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
      print ("Admin-Panel-Finder Qurulur...")
      os.system ("apt update")
      os.system ("git clone https://github.com/bdblackhat/admin-panel-finder.git")
      print ("Admin-Panel-Finder Quruldu.")
       
  else :
    print ("Zəhmət olmasa etibarlı bir nömrə daxil edin!")
       
       
       
      
    
