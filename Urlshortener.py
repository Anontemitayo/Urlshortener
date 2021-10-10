import os,sys
import time
import pyshorteners

os.system("pip install pyshorteners")
os.system("clear")
time.sleep(3)
print("""
\033[1;32;40m
 _   _      _       _                _
| | | |_ __| |  ___| |__   ___  _ __| |_ _ __   ___ _ __
| | | | '__| | / __| '_ \ / _ \| '__| __| '_ \ / _ \ '__|
| |_| | |  | | \__ \ | | | (_) | |  | |_| | | |  __/ |
 \___/|_|  |_| |___/_| |_|\___/|_|   \__|_| |_|\___|_|
          
+=========================================+
| Created By:    AnonTemitayo |
| Contact:   facebook.com/Anon.Temitayo |
| Thanks To: Raveesha,Stegano,Kämöhëlö,Red taren, Uel sam |
+=========================================+
""")
print("""
 [1] Tinyurl
 [2] Chilp.it
 [3] Clck.ru
 [4] Da.gd
 [5] Exit the program
  """)

web = input(" Choose any of your choice : ")
if web == "1":
	os.system("clear")
	print("""
\033[1;32;40m
 _   _      _       _                _
| | | |_ __| |  ___| |__   ___  _ __| |_ _ __   ___ _ __
| | | | '__| | / __| '_ \ / _ \| '__| __| '_ \ / _ \ '__|
| |_| | |  | | \__ \ | | | (_) | |  | |_| | | |  __/ |
 \___/|_|  |_| |___/_| |_|\___/|_|   \__|_| |_|\___|_|
          
          [+] By AnonTemitayo
""")


	site = input("Enter the site link : ")
	s = pyshorteners.Shortener()
	print("The shortened link :", s.tinyurl.			short(site))



elif web == "2":
	
	os.system("clear")
	print("""
\033[1;32;40m
 _   _      _       _                _
| | | |_ __| |  ___| |__   ___  _ __| |_ _ __   ___ _ __
| | | | '__| | / __| '_ \ / _ \| '__| __| '_ \ / _ \ '__|
| |_| | |  | | \__ \ | | | (_) | |  | |_| | | |  __/ |
 \___/|_|  |_| |___/_| |_|\___/|_|   \__|_| |_|\___|_|
          
          [+] By AnonTemitayo
""")

	site = input("Enter the site link : ")
	s = pyshorteners.Shortener()
	print("The shortened link : ", s.chilpit.		short(site))

elif web == "3":
	
	os.system("clear")
	print("""
\033[1;32;40m
 _   _      _       _                _
| | | |_ __| |  ___| |__   ___  _ __| |_ _ __   ___ _ __
| | | | '__| | / __| '_ \ / _ \| '__| __| '_ \ / _ \ '__|
| |_| | |  | | \__ \ | | | (_) | |  | |_| | | |  __/ |
 \___/|_|  |_| |___/_| |_|\___/|_|   \__|_| |_|\___|_|
          
          [+] By AnonTemitayo
""")

	site = input("Enter the site link : ")
	s = pyshorteners.Shortener()
	print("The shortened link : ", s.clckru.		short(site))

elif web == "4":
	
	os.system("clear")
	print("""
\033[1;32;40m
 _   _      _       _                _
| | | |_ __| |  ___| |__   ___  _ __| |_ _ __   ___ _ __
| | | | '__| | / __| '_ \ / _ \| '__| __| '_ \ / _ \ '__|
| |_| | |  | | \__ \ | | | (_) | |  | |_| | | |  __/ |
 \___/|_|  |_| |___/_| |_|\___/|_|   \__|_| |_|\___|_|
          
          [+] By AnonTemitayo
""")

	site = input("Enter the site link : ")
	s = pyshorteners.Shortener()
	print("The shortened link : ", s.dagd.		short(site))	
elif web == "5":
	sys.exit()
else:
	print("\033[1;31;40mError : Please enter a digit \033")