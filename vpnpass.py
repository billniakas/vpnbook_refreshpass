import os.path
import re
import urllib.request
import urllib.error
import fileinput
def vpn_page(url):
        
        req = urllib.request.Request(url)
        try:
            with urllib.request.urlopen(req) as response:
                html = response.read().decode()
            
            filename = "vpnpass.html"
            with open(filename, "w", encoding="utf-8") as p:
                p.write(html)
        except urllib.error.HTTPError as e:
            print(e.code)
            print(e.readline())
            return 0
        except urllib.error.URLError as e:
            print(e)
            if hasattr(e, 'reason'):  # χωρίς σύνδεση ιντερνετ
                print('Failed to connect to the server')
                print('Reason : ', e.reason)
            return 0
        else:
            if (process_file(filename)) : return 1
            else : return 0

def process_file(filename):
            
        with open(filename, 'r', encoding = 'utf-8') as f:
            vpn = f.read()#.replace("\n", " ")
            password = re.findall(r'<li>Password: <strong>\b([A-Z0-9]{7})\b',vpn, re.I)
            if len(password)>1:
                password = password[0]
                print("Το τελευταίο password είναι το",password)
            else: print("Το τελευταίο password είναι το",password)


        with open('password.txt', 'r+', encoding = 'utf-8') as v:
            lines = v.readlines()
            current_pass = lines[1].strip()
            #print(len(current_pass))
            print ("Το παρόν password είναι",current_pass)
            if password == current_pass :
                print("Το password δεν έχει αλλάξει")
            else:
                v.seek(8)
                v.write(password)
                print("Το password άλλαξε από",current_pass,"σε", password)
           

url = "https://www.vpnbook.com/freevpn"
vpn_page(url)
