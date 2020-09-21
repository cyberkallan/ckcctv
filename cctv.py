# -- coding = utf-8 -- CIE YNG NGINTIP

"follow ig arz_beats"
"sub to CYBER KALLAN"
"telegram @THREEALIENHACKERS"

import os, sys
import time
import random
import os.path

putih="\x1b[1;97m"
merah="\x1b[1;91m"
hijau="\x1b[1;92m"
red= '\033[91m'
orange= '\33[38;5;208m'
green= '\033[92m'
cyan= '\033[36m'
bold= '\033[1m'
end= '\033[0m'

os.system('clear')

def cek():
       print merah+"You will install materials from these tools"
       oke = raw_input(merah+"Continue (y/n) : ")
       if oke == 'y':
           cek1()
       else:
           if oke == 'n':
               sys.exit()

def cek1():
        os.system('clear')
        print merah+'allow storage access'
        nxt()
        os.system(termux-setup-storage)
        nxt()
        os.system('apt install figlet -y && apt install ruby -y && gem install lolcat')
        print cyan+"Cleaning..."
        print green+"[ ! ] Starting CCTV.py"
        menu()

def flush(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.01)

def out():
        exit()

def back():
        raw_input('\n\x1b[1;91m                                 [ \x1b[1;97mBack \x1b[1;91m]')
        home()

def nxt():
        raw_input('\n\x1b[1;91m                                 [ \x1b[1;97mNext \x1b[1;91m]')
        os.system('clear')

def logo():
        f = open('asci')
        print merah+f.read()
        f.close
        print '---------------------------------------------------'
        print cyan+' Author  : '+green+'Arjun Arz '
        print cyan+' Github  : '+green+'http://github.com/Cyberkallan '
        print cyan+' Youtube : '+green+'CYBERKALLAN '
        print putih+'---------------------------------------------------'
        print ''

def update():
        os.system('clear')
        os.system('git stash && git pull origin master')
        os.system('python2 install.py')
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        home()

def help():
        print green+"List Commands :"
        print cyan+"===================================="
        print merah+"cctv/jabar patient : CCTV PUBLIC WEST JAVA"
        print merah+"cctv/kalsel: CCTV PUBLIC CITY "
        print merah+"cctv/jakarta : cctv PUBLIC ROAD"
        print merah+"Coming Soon"
        print cyan+"====================================="
        back()

def kalsel():
          os.system('clear')
          os.system('figlet CCTV ACCESS | lolcat')
          print cyan+"1.Area Simpang Tower - Simpang Pal6"
          print cyan+"2.Area Siring - Cambodia"
          kalsel = raw_input(merah+"$CCTV > ")
          if kalsel == '1':
              kalsel1()
          else:
              if kalsel == '2':
                  kalsel3()

def kalsel1():
           os.system('clear')
           print cyan+"you will enter the cctv website"
           ok = raw_input(merah+"Continue (y/n) : ")
           if ok == 'y':
               kalsel2()
           else:
               if ok == 'y':
                   kalsel()

def kalsel2():
           os.system('clear')
           os.system('termux-open https://atcs.banjarmasinkota.go.id/')
           back()

def kalsel3():
           os.system('clear')
           os.system('termux-open https://cctv.banjarmasinkota.go.id/list')
           back()

def jabar():
         os.system('clear')
         print merah+"You will be redirected to CCTV JAWA BARAT website"
         lol = raw_input(cyan+"Continue (y/n) : ")
         if lol == 'y':
             jabar1()
         else:
             if lol == 'n':
                 jabar()

def jabar1():
          os.system('clear')
          os.system('termux-open http://rttmc.dephub.go.id/rttmc/m/page/cctv')
          back()

def pongede():
           os.system('clear')
           print green+'You Will Be Redirected To The Pondgede CCTV Website (Jakarta)'
           acc = raw_input(merah+'Continue (y/n) : ')
           if acc == 'y':
               pongede1()
           else:
               if acc == 'n':
                   pongede()

def pongede1():
            os.system('clear')
            os.system('termux-open http://jasamargalive.com/webjm3/mjm/index.php?r=site/getarea&a=2&b=568')
            back()

def menu():
        os.system('clear')
        logo()
        print cyan+"CCTV PUBLIC BY CYBER KALLAN"
        print merah+"Not for sale!!"

def pilih():
    zedd = raw_input(merah+'CCTV$ > ')
    if zedd == '':
        print merah+'[!] You Understood Me'
        time.sleep(1)
        os.system('clear')
        home()
    else:
        if zedd == 'cctv/kalsel':
            kalsel()
        else:
            if zedd == 'cctv/jabar':
                jabar()
            else:
              if zedd == 'help':
                help()
                home()
              else:
                                  if zedd == 'cctv/jakarta':
                                        pongede()
                                  else:
                                         if zedd == 'update':
                                           update()
                                         else:
                                           print 'ok'
                                           if zedd == 'exit':
                                             exit()
                                           else:
                                             print '\x1b[1;91m[!] select 1-6'
                                             os.system('clear')
                                             home()

def home():
        menu()
        pilih()

home()

