import os, sys
import time
import random

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

def flush(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)

def nxt():
	print '---------------------------------------------------'
	raw_input('\n\x1b[1;91m					[ \x1b[1;97mNext \x1b[1;91m]')

print merah+'allow storage access'
nxt()
os.system('termux-setup-storage')
nxt()
os.system('pkg install unstable-repo')
os.system('apt upgrade')
os.system('apt install ruby -y')
os.system('apt install figlet')
os.system('gem install lolcat')
os.system('clear')
print merah+'cleaning...'
print cyan+'[ ! ] Starting CyberkallanCctv...'
time.sleep(3)
os.system('python2 cctv.py')
