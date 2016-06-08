#!/usr/bin/python
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import os
import threading
stylesheet = open("style2.css","r")
stylesheet = stylesheet.read()
liste = []
print '''
\033[1;92m
 $$\   $$\             $$\                         $$\ $$\           
 $$ | $$  |            $$ |                        $$ |\__|          
 $$ |$$  /  $$$$$$\  $$$$$$\    $$$$$$\   $$$$$$\  $$ |$$\ $$$$$$$\  
 $$$$$  /   \____$$\ \_$$  _|  $$  __$$\ $$  __$$\ $$ |$$ |$$  __$$\ 
 $$  $$<    $$$$$$$ |  \033[1;91mKali linux tools installer\033[1;92m |$$ |$$ |$$ |  $$ |
 \033[1;96m$$ |\$$\  $$  __$$ |  $$ |$$\ $$ |  $$ |$$ |  $$ |$$ |$$ |$$ |  $$ |
 $$ | \$$\ \$$$$$$$ |  \$$$$  |\$$$$$$  |\$$$$$$  |$$ |$$ |$$ |  $$ |
 \__|  \__| \_______|   \____/  \______/  \______/ \__|\__|\__|  \__| Gui V1.0 \033[1;m


 \033[1;32m        + -- -- +=[ Author-Gui: En0k4s Worms #H4ckT3ur ]=+ -- ---+ \033[1;m
 \033[1;32m+ -- -- +=[ Credit : LionSec author of Katoolin script-console ]=+ -- --+\033[1;m

		'''
class Fenetre(QWidget):
     def install(self,name):
         os.system(name)
     def affig5(self):
         if self.x1.isChecked():
            liste.append("git clone https://github.com/LionSec/wifresti.git && cp wifresti/wifresti.py /usr/bin/wifresti && chmod +x /usr/bin/wifresti && wifresti")
            pass
         if self.x2.isChecked():
            liste.append("apt-get install squid3")
         for l in liste:
             self.install(l)
             liste.remove(l)    
     def affig9(self):
         if self.t1.isChecked():
            liste.append("apt-get install bbqsql")
         if self.t2.isChecked():
            liste.append("apt-get install bed")
         if self.t3.isChecked():
            liste.append("apt-get install cisco-auditing-tool")
         if self.t4.isChecked():
            liste.append("apt-get install cisco-global-exploiter")
         if self.t5.isChecked():
            liste.append("apt-get install cisco-ocs")
         if self.t6.isChecked():
            liste.append("apt-get install cisco-torch")
         if self.t7.isChecked():
            liste.append("apt-get install copy-router-config")
         if self.t8.isChecked():
            liste.append("echo 'download page : http://www.cqure.net/wp/tools/database/dbpwaudit/'")
         if self.t9.isChecked():
            liste.append("apt-get install doona")
         if self.t10.isChecked():
            liste.append("apt-get install dotdotpwn")
         if self.t11.isChecked():
            liste.append("apt-get install greenbone-security-assistant")
         if self.t12.isChecked():
            liste.append("apt-get install git && git clone git://git.kali.org/packages/gsd.git")
         if self.t13.isChecked():
            liste.append("apt-get install hexorbase")
         if self.t14.isChecked():
            liste.append("apt-get install inguma")
         if self.t15.isChecked():
            liste.append("apt-get install jsql")
         if self.t16.isChecked():
            liste.append("apt-get install lynis")
         if self.t17.isChecked():
            liste.append("apt-get install nmap")
         if self.t18.isChecked():
            liste.append("apt-get install ohrwurm")
         if self.t19.isChecked():
            liste.append("apt-get install openvas-administrator")
         if self.t20.isChecked():
            liste.append("apt-get install openvas-cli")
         if self.t21.isChecked():
            liste.append("apt-get install openvas-manager")
         if self.t22.isChecked():
            liste.append("apt-get install openvas-scanner")
         if self.t23.isChecked():
            liste.append("apt-get install oscanner")
         if self.t24.isChecked():
            liste.append("apt-get install powerfuzzer")
         if self.t25.isChecked():
            liste.append("apt-get install sfuzz")
         if self.t26.isChecked():
            liste.append("apt-get install sidguesser")
         if self.t27.isChecked():
            liste.append("apt-get install siparmyknife")
         if self.t28.isChecked():
            liste.append("apt-get install sqlmap")
         if self.t29.isChecked():
            liste.append("apt-get install sqlninja")
         if self.t30.isChecked():
            liste.append("apt-get install sqlsus")
         if self.t31.isChecked():
            liste.append("apt-get install thc-ipv6")
         if self.t32.isChecked():
            liste.append("apt-get install tnscmd10g")
         if self.t33.isChecked():
            liste.append("apt-get install unix-privesc-check")
         if self.t34.isChecked():
            liste.append("apt-get install yersinia")
         for l in liste:
             self.install(l)
             liste.remove(l)
     def affig12(self):
         if self.o1.isChecked():
            liste.append("apt-get install burpsuite")
         if self.o2.isChecked():
            liste.append("apt-get install dnschef")
         if self.o3.isChecked():
            liste.append("apt-get install fiked")
         if self.o4.isChecked():
            liste.append("apt-get install hamster-sidejack")
         if self.o5.isChecked():
            liste.append("apt-get install hexinject")
         if self.o6.isChecked():
            liste.append("apt-get install iaxflood")
         if self.o7.isChecked():
            liste.append("apt-get install inviteflood")
         if self.o8.isChecked():
            liste.append("apt-get install ismtp")
         if self.o9.isChecked():
            liste.append("apt-get install git && git clone git://git.kali.org/packages/isr-evilgrade.git")
         if self.o10.isChecked():
            liste.append("apt-get install mitmproxy")
         if self.o11.isChecked():
            liste.append("apt-get install ohrwurm")
         if self.o12.isChecked():
            liste.append("apt-get install protos-sip")
         if self.o13.isChecked():
            liste.append("apt-get install rebind")
         if self.o14.isChecked():
            liste.append("apt-get install responder")
         if self.o15.isChecked():
            liste.append("apt-get install rtpbreak")
         if self.o16.isChecked():
            liste.append("apt-get install rtpinsertsound")
         if self.o17.isChecked():
            liste.append("apt-get install rtpmixsound")
         if self.o18.isChecked():
            liste.append("apt-get install sctpscan")
         if self.o19.isChecked():
            liste.append("apt-get install siparmyknife")
         if self.o20.isChecked():
            liste.append("apt-get install sipp")
         if self.o21.isChecked():
            liste.append("apt-get install sipvicious")
         if self.o22.isChecked():
            liste.append("apt-get install sniffjoke")
         if self.o23.isChecked():
            liste.append("apt-get install sslsplit")
         if self.o24.isChecked():
            liste.append("apt-get install sslstrip")
         if self.o25.isChecked():
            liste.append("apt-get install thc-ipv6")
         if self.o26.isChecked():
            liste.append("apt-get install voiphopper")
         if self.o27.isChecked():
            liste.append("apt-get install webscarab")
         if self.o28.isChecked():
            liste.append("apt-get install wifi-honey")
         if self.o29.isChecked():
            liste.append("apt-get install wireshark")
         if self.o30.isChecked():
            liste.append("apt-get install xspy")
         if self.o31.isChecked():
            liste.append("apt-get install yersinia")
         if self.o32.isChecked():
            liste.append("apt-get install zaproxy")
         for l in liste:
             self.install(l)
             liste.remove(l)   
     def affig4(self):
         if self.h1.isChecked():
            liste.append("apt-get install android-sdk")
            pass
         if self.h2.isChecked():
            liste.append("apt-get install apktool")
         if self.h3.isChecked():
            liste.append("apt-get install arduino")
         if self.h4.isChecked():
            liste.append("apt-get install dex2jar")
         if self.h5.isChecked():
            liste.append("apt-get install sakis3g")
         if self.h6.isChecked():
            liste.append("apt-get install smali")
         for l in liste:
             self.install(l)
             liste.remove(l)
     def affig14(self):
         if self.r1.isChecked():
            liste.append("apt-get install acccheck")
         if self.r2.isChecked():
            liste.append("apt-get install burpsuite")
         if self.r3.isChecked():
            liste.append("apt-get install cewl")
         if self.r4.isChecked():
            liste.append("apt-get install chntpw")
         if self.r5.isChecked():
            liste.append("apt-get install cisco-auditing-tool")
         if self.r6.isChecked():
            liste.append("apt-get install cmospwd")
         if self.r7.isChecked():
            liste.append("apt-get install creddump")
         if self.r8.isChecked():
            liste.append("apt-get install git && git clone git://git.kali.org/packages/dbpwaudit.git")
         if self.r9.isChecked():
            liste.append("apt-get install findmyhash")
         if self.r10.isChecked():
            liste.append("apt-get install gpp-decrypt")
         if self.r11.isChecked():
            liste.append("apt-get install hash-identifier")
         if self.r12.isChecked():
            liste.append("apt-get install hexorbase")
         if self.r13.isChecked():
            liste.append("echo 'please visit : https://www.thc.org/thc-hydra/'")
         if self.r14.isChecked():
            liste.append("apt-get install john the ripper")
         if self.r15.isChecked():
            liste.append("apt-get install johnny")
         if self.r16.isChecked():
            liste.append("apt-get install keimpx")
         if self.r17.isChecked():
            liste.append("apt-get install maltego-teeth")
         if self.r18.isChecked():
            liste.append("apt-get install maskprocessor")
         if self.r19.isChecked():
            liste.append("apt-get install multiforcer")
         if self.r20.isChecked():
            liste.append("apt-get install ncrack")
         if self.r21.isChecked():
            liste.append("apt-get install oclgausscrack")
         if self.r22.isChecked():
            liste.append("apt-get install pack")
         if self.r23.isChecked():
            liste.append("apt-get install patator")
         if self.r24.isChecked():
            liste.append("echo 'please visit : http://www.leidecker.info/projects/phrasendrescher/index.shtml'")
         if self.r25.isChecked():
            liste.append("apt-get install polenum")
         if self.r26.isChecked():
            liste.append("apt-get install rainbowcrack")
         if self.r27.isChecked():
            liste.append("apt-get install rcracki-mt")
         if self.r28.isChecked():
            liste.append("apt-get install rsmangler")
         if self.r29.isChecked():
            liste.append("apt-get install sqldict")
         if self.r30.isChecked():
            liste.append("apt-get install statsprocessor")
         if self.r31.isChecked():
            liste.append("apt-get install thc-pptp-bruter")
         if self.r32.isChecked():
            liste.append("apt-get install truecrack")
         if self.r33.isChecked():
            liste.append("apt-get install webscarab")
         if self.r34.isChecked():
            liste.append("apt-get install wordlists")
         if self.r35.isChecked():
            liste.append("apt-get install zaproxy")
         for l in liste:
             self.install(l)
             liste.remove(l)
     def affig13(self):
         if self.q1.isChecked():
            liste.append("apt-get install binwalk")
         if self.q2.isChecked():
            liste.append("apt-get install bulk-extractor")
         if self.q3.isChecked():
            liste.append("apt-get install git && git clone git://git.kali.org/packages/capstone.git")
         if self.q4.isChecked():
            liste.append("apt-get install chntpw")
         if self.q5.isChecked():
            liste.append("apt-get install cuckoo")
         if self.q6.isChecked():
            liste.append("apt-get install dc3dd")
         if self.q7.isChecked():
            liste.append("apt-get install ddrescue")
         if self.q8.isChecked():
            liste.append("apt-get install dff")
         if self.q9.isChecked():
            liste.append("apt-get install git && git clone git://git.kali.org/packages/distorm3.git")
         if self.q10.isChecked():
            liste.append("apt-get install dumpzilla")
         if self.q11.isChecked():
            liste.append("apt-get install extundelete")
         if self.q12.isChecked():
            liste.append("apt-get install foremost")
         if self.q13.isChecked():
            liste.append("apt-get install galleta")
         if self.q14.isChecked():
            liste.append("apt-get install guymager")
         if self.q15.isChecked():
            liste.append("apt-get install iphone-backup-analyzer")
         if self.q16.isChecked():
            liste.append("apt-get install p0f")
         if self.q17.isChecked():
            liste.append("apt-get install pdf-parser")
         if self.q18.isChecked():
            liste.append("apt-get install pdfid")
         if self.q19.isChecked():
            liste.append("apt-get install pdgmail")
         if self.q20.isChecked():
            liste.append("apt-get install peepdf")
         if self.q21.isChecked():
            liste.append("apt-get install regripper")
         if self.q22.isChecked():
            liste.append("apt-get install volatility")
         if self.q23.isChecked():
            liste.append("apt-get install xplico")
         for l in liste:
             self.install(l)
             liste.remove(l)
     def affig11(self):
         if self.b1.isChecked():
            liste.append("apt-get install apache-users")
         if self.b2.isChecked():
            liste.append("apt-get install arachni")
         if self.b3.isChecked():
            liste.append("apt-get install bbqsql")
         if self.b4.isChecked():
            liste.append("apt-get install blindelephant")
         if self.b5.isChecked():
            liste.append("apt-get install burpsuite")
         if self.b6.isChecked():
            liste.append("apt-get install cutycapt")
         if self.b7.isChecked():
            liste.append("apt-get install davtest")
         if self.b8.isChecked():
            liste.append("apt-get install deblaze")
         if self.b9.isChecked():
            liste.append("apt-get install dirb")
         if self.b10.isChecked():
            liste.append("apt-get install dirbuster")
         if self.b11.isChecked():
            liste.append("apt-get install fimap")
         if self.b12.isChecked():
            liste.append("apt-get install funkload")
         if self.b13.isChecked():
            liste.append("apt-get install grabber")
         if self.b14.isChecked():
            liste.append("apt-get install jboss-autopwn")
         if self.b15.isChecked():
            liste.append("apt-get install joomscan")
         if self.b16.isChecked():
            liste.append("apt-get install jsql")
         if self.b17.isChecked():
            liste.append("apt-get install maltego-teeth")
         if self.b18.isChecked():
            liste.append("apt-get install padbuster")
         if self.b19.isChecked():
            liste.append("apt-get install paros")
         if self.b20.isChecked():
            liste.append("apt-get install parsero")
         if self.b21.isChecked():
            liste.append("apt-get install plecost")
         if self.b22.isChecked():
            liste.append("apt-get install powerfuzzer")
         if self.b23.isChecked():
            liste.append("apt-get install proxystrike")
         if self.b24.isChecked():
            liste.append("apt-get install recon-ng")
         if self.b25.isChecked():
            liste.append("apt-get install skipfish")
         if self.b26.isChecked():
            liste.append("apt-get install sqlmap")
         if self.b27.isChecked():
            liste.append("apt-get install sqlninja")
         if self.b28.isChecked():
            liste.append("apt-get install sqlsus")
         if self.b29.isChecked():
            liste.append("apt-get install ua-tester")
         if self.b30.isChecked():
            liste.append("apt-get install uniscan")
         if self.b31.isChecked():
            liste.append("apt-get install vega")
         if self.b32.isChecked():
            liste.append("apt-get install w3af")
         if self.b33.isChecked():
            liste.append("apt-get install webscarab")
         if self.b34.isChecked():
            liste.append("apt-get install webshag")
         if self.b35.isChecked():
            liste.append("apt-get install git && git clone git://git.kali.org/packages/webslayer.git")
         if self.b36.isChecked():
            liste.append("apt-get install websploit")
         if self.b37.isChecked():
            liste.append("apt-get install wfuzz")
         if self.b38.isChecked():
            liste.append("apt-get install wpscan")
         if self.b39.isChecked():
            liste.append("apt-get install xsser")
         if self.b40.isChecked():
            liste.append("apt-get install zaproxy")
         for l in liste:
             self.install(l)
             liste.remove(l)
     def affig10(self):
         if self.k1.isChecked():
            liste.append("apt-get install Aircrack-ng")
         if self.k2.isChecked():
            liste.append("apt-get install Asleap")
         if self.k3.isChecked():
            liste.append("apt-get install Bluelog")
         if self.k4.isChecked():
            liste.append("apt-get install git && git clone git://git.kali.org/packages/bluemaho.git")
         if self.k5.isChecked():
            liste.append("apt-get install git && git clone git://git.kali.org/packages/bluepot.git")
         if self.k6.isChecked():
            liste.append("apt-get install BlueRanger")
         if self.k7.isChecked():
            liste.append("apt-get install Bluesnarfer")
         if self.k8.isChecked():
            liste.append("apt-get install Bully")
         if self.k9.isChecked():
            liste.append("apt-get install coWPAtty")
         if self.k10.isChecked():
            liste.append("apt-get install crackle")
         if self.k11.isChecked():
            liste.append("apt-get install eapmd5pass")
         if self.k12.isChecked():
            liste.append("apt-get install fern-wifi-cracker")
         if self.k13.isChecked():
            liste.append("apt-get install ghost-phisher")
         if self.k14.isChecked():
            liste.append("apt-get install GISKismet")
         if self.k15.isChecked():
            liste.append("apt-get install git && git clone git://git.kali.org/packages/gr-scan.git")
         if self.k16.isChecked():
            liste.append("apt-get install kalibrate-rtl")
         if self.k17.isChecked():
            liste.append("apt-get install KillerBee")
         if self.k18.isChecked():
            liste.append("apt-get install Kismet")
         if self.k19.isChecked():
            liste.append("apt-get install mdk3")
         if self.k20.isChecked():
            liste.append("apt-get install mfcuk")
         if self.k21.isChecked():
            liste.append("apt-get install mfoc")
         if self.k22.isChecked():
            liste.append("apt-get install mfterm")
         if self.k23.isChecked():
            liste.append("apt-get install multimon-ng")
         if self.k24.isChecked():
            liste.append("apt-get install PixieWPS")
         if self.k25.isChecked():
            liste.append("apt-get install Reaver")
         if self.k26.isChecked():
            liste.append("apt-get install redfang")
         if self.k27.isChecked():
            liste.append("apt-get install rtlsdr-scanner")
         if self.k28.isChecked():
            liste.append("apt-get install Spooftooph")
         if self.k29.isChecked():
            liste.append("apt-get install Wifi Honey")
         if self.k30.isChecked():
            liste.append("apt-get install Wifitap")
         if self.k31.isChecked():
            liste.append("apt-get install Wifite")
         for l in liste:
             self.install(l)
             liste.remove(l)
     def affig7(self):
         if self.r1.isChecked():
            liste.append("apt-get install casefile")
         if self.r2.isChecked():
            liste.append("apt-get install cutycapt")
         if self.r3.isChecked():
            liste.append("apt-get install dos2unix")
         if self.r4.isChecked():
            liste.append("apt-get install dradis")
         if self.r5.isChecked():
            liste.append("apt-get install keepnote")
         if self.r6.isChecked():
            liste.append("apt-get install magictree")
         if self.r7.isChecked():
            liste.append("apt-get install metagoofil")
         if self.r8.isChecked():
            liste.append("apt-get install nipper-ng")
         if self.r9.isChecked():
            liste.append("apt-get install pipal")
         for l in liste:
             self.install(l)
             liste.remove(l)  
     def affig8(self):
         if self.z1.isChecked():
            liste.append("apt-get install cryptcat")
         if self.z2.isChecked():
            liste.append("apt-get install cymothoa")
         if self.z3.isChecked():
            liste.append("apt-get install dbd")
         if self.z4.isChecked():
            liste.append("apt-get install dns2tcp")
         if self.z5.isChecked():
            liste.append("apt-get install http-tunnel")
         if self.z6.isChecked():
            liste.append("apt-get install httptunnel")
         if self.z7.isChecked():
            liste.append("apt-get install intersect")
         if self.z8.isChecked():
            liste.append("apt-get install nishang")
         if self.z9.isChecked():
            liste.append("apt-get install polenum")
         if self.z10.isChecked():
            liste.append("apt-get install powersploit")
         if self.z11.isChecked():
            liste.append("apt-get install pwnat")
         if self.z12.isChecked():
            liste.append("apt-get install ridenum")
         if self.z13.isChecked():
            liste.append("apt-get install sbd")
         if self.z14.isChecked():
            liste.append("apt-get install u3-pwn")
         if self.z15.isChecked():
            liste.append("apt-get install webshells")
         if self.z16.isChecked():
            liste.append("apt-get install weevely")
         print liste
         for l in liste:
             self.install(l)
             liste.remove(l)
     def affig6(self):
         if self.a1.isChecked():
            liste.append("apt-get install armitage")
         if self.a2.isChecked():
            liste.append("apt-get install backdoor-factory")
         if self.a3.isChecked():
            liste.append("apt-get install beef-xss")
         if self.a4.isChecked():
            liste.append("apt-get install cisco-auditing-tool")
         if self.a5.isChecked():
            liste.append("apt-get install cisco-global-exploiter")
         if self.a6.isChecked():
            liste.append("apt-get install cisco-ocs")
         if self.a7.isChecked():
            liste.append("apt-get install cisco-torch")
         if self.a8.isChecked():
            liste.append("apt-get install crackle")
         if self.a9.isChecked():
            liste.append("apt-get install jboss-autopwn")
         if self.a10.isChecked():
            liste.append("apt-get install linux-exploit-suggester")
         if self.a11.isChecked():
            liste.append("apt-get install maltego-teeth")
         if self.a12.isChecked():
            liste.append("apt-get install set")
         if self.a13.isChecked():
            liste.append("apt-get install shellnoob")
         if self.a14.isChecked():
            liste.append("apt-get install sqlmap")
         if self.a15.isChecked():
            liste.append("apt-get install thc-ipv6")
         if self.a16.isChecked():
            liste.append("apt-get install yersinia")
         print liste
         for l in liste:
             self.install(l)
             liste.remove(l)  
     def affig2(self):
         if self.m1.isChecked():
            liste.append("apt-get install dhcpig")
            pass
         if self.m2.isChecked():
            liste.append("apt-get install funkload")
         if self.m3.isChecked():
            liste.append("apt-get install iaxflood")
         if self.m4.isChecked():
            liste.append("apt-get install git && git clone git://git.kali.org/packages/inundator.git")
         if self.m5.isChecked():
            liste.append("apt-get install inviteflood")
         if self.m6.isChecked():
            liste.append("apt-get install ipv6-toolkit")
         if self.m7.isChecked():
            liste.append("apt-get install apt-get install mdk3")
         if self.m8.isChecked():
            liste.append("apt-get install reaver")
         if self.m9.isChecked():
            liste.append("apt-get install rtpflood")
         if self.m10.isChecked():
            liste.append("apt-get install slowhttptest")
         if self.m11.isChecked():
            liste.append("apt-get install t50")
         if self.m12.isChecked():
            liste.append("apt-get install termineter")
         if self.m13.isChecked():
            liste.append("apt-get install thc-ipv6")
         if self.m14.isChecked():
            liste.append("apt-get install thc-ssl-dos")
         print liste
         for l in liste:
             self.install(l)
             liste.remove(l) 
     def affig3(self):
         if self.p1.isChecked():
            liste.append("apt-get install apktool")
            pass
         if self.p2.isChecked():
            liste.append("apt-get install dex2jar")
         if self.p3.isChecked():
            liste.append("apt-get install python-diStorm3")
         if self.p4.isChecked():
            liste.append("apt-get install edb-debugger")
         if self.p5.isChecked():
            liste.append("apt-get install jad")
         if self.p6.isChecked():
            liste.append("apt-get install javasnoop")
         if self.p7.isChecked():
            liste.append("apt-get install JD")
         if self.p8.isChecked():
            liste.append("apt-get install OllyDbg")
         if self.p9.isChecked():
            liste.append("apt-get install smali")
         if self.p10.isChecked():
            liste.append("apt-get install Valgrind")
         if self.p11.isChecked():
            liste.append("apt-get install YARA")
         for l in liste:
             self.install(l)
             liste.remove(l)  
     def affig(self):
         if self.n1.isChecked():
            liste.append("apt-get install acccheck")
            pass
         if self.n2.isChecked():
            liste.append("apt-get install ace-voip")
         if self.n3.isChecked():
            liste.append("apt-get install amap")
         if self.n4.isChecked():
            liste.append("apt-get install automater")
         if self.n5.isChecked():
            liste.append("wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
         if self.n6.isChecked():
            liste.append("apt-get install braa")
         if self.n7.isChecked():
            liste.append("apt-get install casefile")
         if self.n8.isChecked():
            liste.append("apt-get install cdpsnarf")
         if self.n9.isChecked():
            liste.append("apt-get install cisco-torch")
         if self.n10.isChecked():
            liste.append("apt-get install cookie-cadger")
         if self.n11.isChecked():
            liste.append("apt-get install copy-router-config")
         if self.n12.isChecked():
            liste.append("apt-get install dmitry")
         if self.n13.isChecked():
            liste.append("apt-get install dnmap")
         if self.n14.isChecked():
            liste.append("apt-get install dnsenum")
         if self.n15.isChecked():
            liste.append("apt-get install dnsmap")
         if self.n16.isChecked():
            liste.append("apt-get install dnsrecon")
         if self.n17.isChecked():
            liste.append("apt-get install dnstracer")
         if self.n18.isChecked():
            liste.append("apt-get install dnswalk")
         if self.n19.isChecked():
            liste.append("apt-get install dotdotpwn")
         if self.n20.isChecked():
            liste.append("apt-get install enum4linux")
         if self.n21.isChecked():
            liste.append("apt-get install enumiax")
         if self.n22.isChecked():
            liste.append("apt-get install exploitdb")
         if self.n23.isChecked():
            liste.append("apt-get install fierce")
         if self.n24.isChecked():
            liste.append("apt-get install firewalk")
         if self.n25.isChecked():
            liste.append("apt-get install fragroute")
         if self.n26.isChecked():
            liste.append("apt-get install fragrouter")
         if self.n27.isChecked():
            liste.append("apt-get install ghost-phisher")
         if self.n28.isChecked():
            liste.append("apt-get install golismero")
         if self.n29.isChecked():
            liste.append("apt-get install lbd")
         if self.n30.isChecked():
            liste.append("apt-get install maltego-teeth")
         if self.n31.isChecked():
            liste.append("apt-get install masscan")
         if self.n32.isChecked():
            liste.append("apt-get install metagoofil")
         if self.n33.isChecked():
            liste.append("apt-get install miranda")
         if self.n34.isChecked():
            liste.append("apt-get install nmap")
         if self.n35.isChecked():
            liste.append("apt-get install ntop")
         if self.n36.isChecked():
            liste.append("apt-get install p0f")
         if self.n37.isChecked():
            liste.append("apt-get install parsero")
         if self.n38.isChecked():
            liste.append("apt-get install recon-ng")
         if self.n39.isChecked():
            liste.append("apt-get install set")
         if self.n40.isChecked():
            liste.append("apt-get install smtp-user-enum")
         if self.n41.isChecked():
            liste.append("apt-get install snmpcheck")
         if self.n42.isChecked():
            liste.append("apt-get install sslcaudit")
         if self.n43.isChecked():
            liste.append("apt-get install sslsplit")
         if self.n44.isChecked():
            liste.append("apt-get install sslstrip")
         if self.n45.isChecked():
            liste.append("apt-get install sslyze")
         if self.n46.isChecked():
            liste.append("apt-get install thc-ipv6")
         if self.n47.isChecked():
            liste.append("apt-get install theharvester")
         if self.n48.isChecked():
            liste.append("apt-get install tlssled")
         if self.n49.isChecked():
            liste.append("apt-get install twofi")
         if self.n50.isChecked():
            liste.append("apt-get install urlcrazy")
         if self.n51.isChecked():
            liste.append("apt-get install wireshark")
         if self.n52.isChecked():
            liste.append("apt-get install wol-e")
         if self.n53.isChecked():
            liste.append("apt-get install xplico")
         if self.n54.isChecked():
            liste.append("apt-get install ismtp")
         if self.n55.isChecked():
            liste.append("apt-get install intrace")
         if self.n56.isChecked():
            liste.append("apt-get install hping3")
         if self.n57.isChecked():
            liste.append("apt-get install goofile")
         print liste
         for l in liste:
             self.install(l)
             liste.remove(l) 
     def MA(self):
         self.z1 = QCheckBox("CryptCat")
         self.z2 = QCheckBox("Cymothoa")
         self.z3 = QCheckBox("dbd")
         self.z4 = QCheckBox("dns2tcp")
         self.z5 = QCheckBox("http-tunnel")
         self.z6 = QCheckBox("HTTPTunnel")
         self.z7 = QCheckBox("Intersect")
         self.z8 = QCheckBox("Nishang")
         self.z9 = QCheckBox("polenum")
         self.z10 = QCheckBox("PowerSploit")
         self.z11 = QCheckBox("pwnat")
         self.z12 = QCheckBox("RidEnum")
         self.z13 = QCheckBox("sbd")
         self.z14 = QCheckBox("U3-Pwn")
         self.z15 = QCheckBox("Webshells")
         self.z16 = QCheckBox("Weevely") 
         self.affoption_layout8.addWidget(self.z1)
         self.affoption_layout8.addWidget(self.z2)
         self.affoption_layout8.addWidget(self.z3)
         self.affoption_layout8.addWidget(self.z4)
         self.affoption_layout8.addWidget(self.z5)
         self.affoption_layout8.addWidget(self.z6)
         self.affoption_layout8.addWidget(self.z7)
         self.affoption_layout8.addWidget(self.z8)
         self.affoption_layout8.addWidget(self.z9)
         self.affoption_layout8.addWidget(self.z10)
         self.affoption_layout8.addWidget(self.z11)
         self.affoption_layout8.addWidget(self.z12)
         self.affoption_layout8.addWidget(self.z13)
         self.affoption_layout8.addWidget(self.z14)
         self.affoption_layout8.addWidget(self.z15)
         self.affoption_layout8.addWidget(self.z16)
         self.connect(self.selection,SIGNAL("clicked()"),self.affig8)
     def ST(self):
         self.m1 = QCheckBox("DHCPig")
         self.m2 = QCheckBox("FunkLoad")
         self.m3 = QCheckBox("iaxflood")
         self.m4 = QCheckBox("Inundator")
         self.m5 = QCheckBox("inviteflood")
         self.m6 = QCheckBox("ipv6-toolkit")
         self.m7 = QCheckBox("mdk3")
         self.m8 = QCheckBox("Reaver")
         self.m9 = QCheckBox("rtpflood")
         self.m10 = QCheckBox("SlowHTTPTest")
         self.m11 = QCheckBox("t50")
         self.m12 = QCheckBox("Termineter")
         self.m13 = QCheckBox("THC-IPV6")
         self.m14 = QCheckBox("THC-SSL-DOS")
         self.affoption_layout2.addWidget(self.m1)
         self.affoption_layout2.addWidget(self.m2)
         self.affoption_layout2.addWidget(self.m3)
         self.affoption_layout2.addWidget(self.m4)
         self.affoption_layout2.addWidget(self.m5)
         self.affoption_layout2.addWidget(self.m6)
         self.affoption_layout2.addWidget(self.m7)
         self.affoption_layout2.addWidget(self.m8)
         self.affoption_layout2.addWidget(self.m9)
         self.affoption_layout2.addWidget(self.m10)
         self.affoption_layout2.addWidget(self.m11)
         self.affoption_layout2.addWidget(self.m12)
         self.affoption_layout2.addWidget(self.m13)
         self.affoption_layout2.addWidget(self.m14)
         self.connect(self.selection,SIGNAL("clicked()"),self.affig2)
     def RE(self):
         self.p1 = QCheckBox("apktool")
         self.p2 = QCheckBox("dex2jar")
         self.p3 = QCheckBox("diStorm3")
         self.p4 = QCheckBox("edb-debugger")
         self.p5 = QCheckBox("jad")
         self.p6 = QCheckBox("javasnoop")
         self.p7 = QCheckBox("JD-GUI")
         self.p8 = QCheckBox("OllyDbg")
         self.p9 = QCheckBox("smali")
         self.p10 = QCheckBox("Valgrind")
         self.p11 = QCheckBox("YARA")
         self.affoption_layout3.addWidget(self.p1)
         self.affoption_layout3.addWidget(self.p2)
         self.affoption_layout3.addWidget(self.p3)
         self.affoption_layout3.addWidget(self.p4)
         self.affoption_layout3.addWidget(self.p5)
         self.affoption_layout3.addWidget(self.p6)
         self.affoption_layout3.addWidget(self.p7)
         self.affoption_layout3.addWidget(self.p8)
         self.affoption_layout3.addWidget(self.p9)
         self.affoption_layout3.addWidget(self.p10)
         self.affoption_layout3.addWidget(self.p11)
         self.connect(self.selection,SIGNAL("clicked()"),self.affig3)
     def HH(self):
         self.h1 = QCheckBox("android-sdk")
         self.h2 = QCheckBox("apktool")
         self.h3 = QCheckBox("Arduino")
         self.h4 = QCheckBox("dex2jar")
         self.h5 = QCheckBox("Sakis3G")
         self.h6 = QCheckBox("smali")
         self.affoption_layout4.addWidget(self.h1)
         self.affoption_layout4.addWidget(self.h2)
         self.affoption_layout4.addWidget(self.h3)
         self.affoption_layout4.addWidget(self.h4)
         self.affoption_layout4.addWidget(self.h5)
         self.affoption_layout4.addWidget(self.h6)
         self.connect(self.selection,SIGNAL("clicked()"),self.affig4)
     def Ex(self):
         self.x1 = QCheckBox("Wifresti")
         self.x2 = QCheckBox("Squid3")
         self.affoption_layout5.addWidget(self.x1)
         self.affoption_layout5.addWidget(self.x2)
         self.connect(self.selection,SIGNAL("clicked()"),self.affig5)
     def ET(self):
         self.a1 = QCheckBox("Armitage")
         self.a2 = QCheckBox("Backdoor Factory")
         self.a3 = QCheckBox("BeEF")
         self.a4 = QCheckBox("cisco-auditing-tool")
         self.a5 = QCheckBox("cisco-global-exploiter")
         self.a6 = QCheckBox("cisco-ocs")
         self.a7 = QCheckBox("cisco-torch")
         self.a8 = QCheckBox("crackle")
         self.a9 = QCheckBox("jboss-autopwn")
         self.a10 = QCheckBox("Linux Exploit Suggester")
         self.a11 = QCheckBox("Maltego Teeth")
         self.a12 = QCheckBox("SET")
         self.a13 = QCheckBox("ShellNoob")
         self.a14 = QCheckBox("sqlmap")
         self.a15 = QCheckBox("THC-IPV6")
         self.a16 = QCheckBox("Yersinia")
         self.affoption_layout6.addWidget(self.a1)
         self.affoption_layout6.addWidget(self.a2)
         self.affoption_layout6.addWidget(self.a3)
         self.affoption_layout6.addWidget(self.a4)
         self.affoption_layout6.addWidget(self.a5)
         self.affoption_layout6.addWidget(self.a6)
         self.affoption_layout6.addWidget(self.a7)
         self.affoption_layout6.addWidget(self.a8)
         self.affoption_layout6.addWidget(self.a9)
         self.affoption_layout6.addWidget(self.a10)
         self.affoption_layout6.addWidget(self.a11)
         self.affoption_layout6.addWidget(self.a12)
         self.affoption_layout6.addWidget(self.a13)
         self.affoption_layout6.addWidget(self.a14)
         self.affoption_layout6.addWidget(self.a15)
         self.affoption_layout6.addWidget(self.a16)
         self.connect(self.selection,SIGNAL("clicked()"),self.affig6)
     def RT(self):
         self.r1 = QCheckBox("CaseFile")
         self.r2 = QCheckBox("CutyCapt")
         self.r3 = QCheckBox("dos2unix")
         self.r4 = QCheckBox("Dradis")
         self.r5 = QCheckBox("KeepNote")
         self.r6 = QCheckBox("MagicTree")
         self.r7 = QCheckBox("Metagoofil")
         self.r8 = QCheckBox("Nipper-ng")
         self.r9 = QCheckBox("pipal")
         self.affoption_layout7.addWidget(self.r1)
         self.affoption_layout7.addWidget(self.r2)
         self.affoption_layout7.addWidget(self.r3)
         self.affoption_layout7.addWidget(self.r4)
         self.affoption_layout7.addWidget(self.r5)
         self.affoption_layout7.addWidget(self.r6)
         self.affoption_layout7.addWidget(self.r7)
         self.affoption_layout7.addWidget(self.r8)
         self.affoption_layout7.addWidget(self.r9)
         self.connect(self.selection,SIGNAL("clicked()"),self.affig7)
     def VA(self):
         self.t1 = QCheckBox("BBQSQL")
         self.t2 = QCheckBox("BED")
         self.t3 = QCheckBox("cisco-auditing-tool")
         self.t4 = QCheckBox("cisco-global-exploiter")
         self.t5 = QCheckBox("cisco-ocs")
         self.t6 = QCheckBox("cisco-torch")
         self.t7 = QCheckBox("copy-router-config")
         self.t8 = QCheckBox("DBPwAudit")
         self.t9 = QCheckBox("Doona")
         self.t10 = QCheckBox("DotDotPwn")
         self.t11 = QCheckBox("Greenbone Security Assistant")
         self.t12 = QCheckBox("GSD")
         self.t13 = QCheckBox("HexorBase")
         self.t14 = QCheckBox("Inguma")
         self.t15 = QCheckBox("jSQL")
         self.t16 = QCheckBox("Lynis")
         self.t17 = QCheckBox("Nmap")
         self.t18 = QCheckBox("ohrwurm")
         self.t19 = QCheckBox("openvas-administrator")
         self.t20 = QCheckBox("openvas-cli")
         self.t21 = QCheckBox("openvas-manager")
         self.t22 = QCheckBox("openvas-scanner")
         self.t23 = QCheckBox("Oscanner")
         self.t24 = QCheckBox("Powerfuzzer")
         self.t25 = QCheckBox("sfuzz")
         self.t26 = QCheckBox("SidGuesser")
         self.t27 = QCheckBox("SIPArmyKnife")
         self.t28 = QCheckBox("sqlmap")
         self.t29 = QCheckBox("Sqlninja")
         self.t30 = QCheckBox("sqlsus")
         self.t31 = QCheckBox("THC-IPV6")
         self.t32 = QCheckBox("tnscmd10g")
         self.t33 = QCheckBox("unix-privesc-check")
         self.t34 = QCheckBox("Yersinia")
         self.affoption_layout9.addWidget(self.t1)
         self.affoption_layout9.addWidget(self.t2)
         self.affoption_layout9.addWidget(self.t3)
         self.affoption_layout9.addWidget(self.t4)
         self.affoption_layout9.addWidget(self.t5)
         self.affoption_layout9.addWidget(self.t6)
         self.affoption_layout9.addWidget(self.t7)
         self.affoption_layout9.addWidget(self.t8)
         self.affoption_layout9.addWidget(self.t9)
         self.affoption_layout9.addWidget(self.t10)
         self.affoption_layout9.addWidget(self.t11)
         self.affoption_layout9.addWidget(self.t12)
         self.affoption_layout9.addWidget(self.t13)
         self.affoption_layout9.addWidget(self.t14)
         self.affoption_layout9.addWidget(self.t15)
         self.affoption_layout9.addWidget(self.t16)
         self.affoption_layout9.addWidget(self.t17)
         self.affoption_layout9.addWidget(self.t18)
         self.affoption_layout9.addWidget(self.t19)
         self.affoption_layout9.addWidget(self.t20)
         self.affoption_layout9.addWidget(self.t21)
         self.affoption_layout9.addWidget(self.t22)
         self.affoption_layout9.addWidget(self.t23)
         self.affoption_layout9.addWidget(self.t24)
         self.affoption_layout9.addWidget(self.t25)
         self.affoption_layout9.addWidget(self.t26)
         self.affoption_layout9.addWidget(self.t27)
         self.affoption_layout9.addWidget(self.t28)
         self.affoption_layout9.addWidget(self.t29)
         self.affoption_layout9.addWidget(self.t30)
         self.affoption_layout9.addWidget(self.t31)
         self.affoption_layout9.addWidget(self.t32)
         self.affoption_layout9.addWidget(self.t33)
         self.affoption_layout9.addWidget(self.t34)
         self.connect(self.selection,SIGNAL("clicked()"),self.affig9)
     def WA(self):
         self.k1 = QCheckBox("Aircrack-ng")
         self.k2 = QCheckBox("Asleap")
         self.k3 = QCheckBox("Bluelog")
         self.k4 = QCheckBox("BlueMaho")
         self.k5 = QCheckBox("Bluepot")
         self.k6 = QCheckBox("BlueRanger")
         self.k7 = QCheckBox("Bluesnarfer")
         self.k8 = QCheckBox("Bully")
         self.k9 = QCheckBox("coWPAtty")
         self.k10 = QCheckBox("crackle")
         self.k11 = QCheckBox("eapmd5pass")
         self.k12 = QCheckBox("Fern Wifi Cracker")
         self.k13 = QCheckBox("Ghost Phisher")
         self.k14 = QCheckBox("GISKismet")
         self.k15 = QCheckBox("gr-scan")
         self.k16 = QCheckBox("kalibrate-rtl")
         self.k17 = QCheckBox("KillerBee")
         self.k18 = QCheckBox("Kismet")
         self.k19 = QCheckBox("mdk3")
         self.k20 = QCheckBox("mfcuk")
         self.k21 = QCheckBox("mfoc")
         self.k22 = QCheckBox("mfterm")
         self.k23 = QCheckBox("Multimon-NG")
         self.k24 = QCheckBox("PixieWPS")
         self.k25 = QCheckBox("Reaver")
         self.k26 = QCheckBox("redfang")
         self.k27 = QCheckBox("RTLSDR Scanner")
         self.k28 = QCheckBox("Spooftooph")
         self.k29 = QCheckBox("Wifi Honey")
         self.k30 = QCheckBox("Wifitap")
         self.k31 = QCheckBox("Wifite")
         self.affoption_layout10.addWidget(self.k1)
         self.affoption_layout10.addWidget(self.k2)
         self.affoption_layout10.addWidget(self.k3)
         self.affoption_layout10.addWidget(self.k4)
         self.affoption_layout10.addWidget(self.k5)
         self.affoption_layout10.addWidget(self.k6)
         self.affoption_layout10.addWidget(self.k7)
         self.affoption_layout10.addWidget(self.k8)
         self.affoption_layout10.addWidget(self.k9)
         self.affoption_layout10.addWidget(self.k10)
         self.affoption_layout10.addWidget(self.k11)
         self.affoption_layout10.addWidget(self.k12)
         self.affoption_layout10.addWidget(self.k13)
         self.affoption_layout10.addWidget(self.k14)
         self.affoption_layout10.addWidget(self.k15)
         self.affoption_layout10.addWidget(self.k16)
         self.affoption_layout10.addWidget(self.k17)
         self.affoption_layout10.addWidget(self.k18)
         self.affoption_layout10.addWidget(self.k19)
         self.affoption_layout10.addWidget(self.k20)
         self.affoption_layout10.addWidget(self.k21)
         self.affoption_layout10.addWidget(self.k22)
         self.affoption_layout10.addWidget(self.k23)
         self.affoption_layout10.addWidget(self.k24)
         self.affoption_layout10.addWidget(self.k25)
         self.affoption_layout10.addWidget(self.k26)
         self.affoption_layout10.addWidget(self.k27)
         self.affoption_layout10.addWidget(self.k28)
         self.affoption_layout10.addWidget(self.k29)
         self.affoption_layout10.addWidget(self.k30)
         self.affoption_layout10.addWidget(self.k31)
         self.connect(self.selection,SIGNAL("clicked()"),self.affig10)
     def WA2(self):
         self.b1 = QCheckBox("apache-users")
         self.b2 = QCheckBox("Arachni")
         self.b3 = QCheckBox("BBQSQL")
         self.b4 = QCheckBox("BlindElephant")
         self.b5 = QCheckBox("Burp Suite")
         self.b6 = QCheckBox("CutyCapt")
         self.b7 = QCheckBox("DAVTest")
         self.b8 = QCheckBox("deblaze")
         self.b9 = QCheckBox("DIRB")
         self.b10 = QCheckBox("DirBuster")
         self.b11 = QCheckBox("fimap")
         self.b12 = QCheckBox("FunkLoad")
         self.b13 = QCheckBox("Grabber")
         self.b14 = QCheckBox("jboss-autopwn")
         self.b15 = QCheckBox("joomscan")
         self.b16 = QCheckBox("jSQL")
         self.b17 = QCheckBox("Maltego Teeth")
         self.b18 = QCheckBox("PadBuster")
         self.b19 = QCheckBox("Paros")
         self.b20 = QCheckBox("Parsero")
         self.b21 = QCheckBox("plecost")
         self.b22 = QCheckBox("Powerfuzzer")
         self.b23 = QCheckBox("ProxyStrike")
         self.b24 = QCheckBox("Recon-ng")
         self.b25 = QCheckBox("Skipfish")
         self.b26 = QCheckBox("sqlmap")
         self.b27 = QCheckBox("Sqlninja")
         self.b28 = QCheckBox("sqlsus")
         self.b29 = QCheckBox("ua-tester")
         self.b30 = QCheckBox("Uniscan")
         self.b31 = QCheckBox("Vega")
         self.b32 = QCheckBox("w3af")
         self.b33 = QCheckBox("WebScarab")
         self.b34 = QCheckBox("Webshag")
         self.b35 = QCheckBox("WebSlayer")
         self.b36 = QCheckBox("WebSploit")
         self.b37 = QCheckBox("Wfuzz")
         self.b38 = QCheckBox("WPScan")
         self.b39 = QCheckBox("XSSer")
         self.b40 = QCheckBox("zaproxy")
         self.affoption_layout11.addWidget(self.b1)
         self.affoption_layout11.addWidget(self.b2)
         self.affoption_layout11.addWidget(self.b3)
         self.affoption_layout11.addWidget(self.b4)
         self.affoption_layout11.addWidget(self.b5)
         self.affoption_layout11.addWidget(self.b6)
         self.affoption_layout11.addWidget(self.b7)
         self.affoption_layout11.addWidget(self.b8)
         self.affoption_layout11.addWidget(self.b9)
         self.affoption_layout11.addWidget(self.b10)
         self.affoption_layout11.addWidget(self.b11)
         self.affoption_layout11.addWidget(self.b12)
         self.affoption_layout11.addWidget(self.b13)
         self.affoption_layout11.addWidget(self.b14)
         self.affoption_layout11.addWidget(self.b15)
         self.affoption_layout11.addWidget(self.b16)
         self.affoption_layout11.addWidget(self.b17)
         self.affoption_layout11.addWidget(self.b18)
         self.affoption_layout11.addWidget(self.b19)
         self.affoption_layout11.addWidget(self.b20)
         self.affoption_layout11.addWidget(self.b21)
         self.affoption_layout11.addWidget(self.b22)
         self.affoption_layout11.addWidget(self.b23)
         self.affoption_layout11.addWidget(self.b24)
         self.affoption_layout11.addWidget(self.b25)
         self.affoption_layout11.addWidget(self.b26)
         self.affoption_layout11.addWidget(self.b27)
         self.affoption_layout11.addWidget(self.b28)
         self.affoption_layout11.addWidget(self.b29)
         self.affoption_layout11.addWidget(self.b30)
         self.affoption_layout11.addWidget(self.b31)
         self.affoption_layout11.addWidget(self.b32)
         self.affoption_layout11.addWidget(self.b33)
         self.affoption_layout11.addWidget(self.b34)
         self.affoption_layout11.addWidget(self.b35)
         self.affoption_layout11.addWidget(self.b36)
         self.affoption_layout11.addWidget(self.b37)
         self.affoption_layout11.addWidget(self.b38)
         self.affoption_layout11.addWidget(self.b39)
         self.affoption_layout11.addWidget(self.b40)
         self.connect(self.selection,SIGNAL("clicked()"),self.affig11)
     def SS(self):
         self.o1 = QCheckBox("Burp Suite")
         self.o2 = QCheckBox("DNSChef")
         self.o3 = QCheckBox("fiked")
         self.o4 = QCheckBox("hamster-sidejack")
         self.o5 = QCheckBox("HexInject")
         self.o6 = QCheckBox("iaxflood")
         self.o7 = QCheckBox("inviteflood")
         self.o8 = QCheckBox("iSMTP")
         self.o9 = QCheckBox("isr-evilgrade")
         self.o10 = QCheckBox("mitmproxy")
         self.o11 = QCheckBox("ohrwurm")
         self.o12 = QCheckBox("protos-sip")
         self.o13 = QCheckBox("rebind")
         self.o14 = QCheckBox("responder")
         self.o15 = QCheckBox("rtpbreak")
         self.o16 = QCheckBox("rtpinsertsound")
         self.o17 = QCheckBox("rtpmixsound")
         self.o18 = QCheckBox("sctpscan")
         self.o19 = QCheckBox("SIPArmyKnife")
         self.o20 = QCheckBox("SIPp")
         self.o21 = QCheckBox("SIPVicious")
         self.o22 = QCheckBox("SniffJoke")
         self.o23 = QCheckBox("SSLsplit")
         self.o24 = QCheckBox("sslstrip")
         self.o25 = QCheckBox("THC-IPV6")
         self.o26 = QCheckBox("VoIPHopper")
         self.o27 = QCheckBox("WebScarab")
         self.o28 = QCheckBox("Wifi Honey")
         self.o29 = QCheckBox("Wireshark")
         self.o30 = QCheckBox("xspy")
         self.o31 = QCheckBox("Yersinia")
         self.o32 = QCheckBox("zaproxy")
         self.affoption_layout12.addWidget(self.o1)
         self.affoption_layout12.addWidget(self.o2)
         self.affoption_layout12.addWidget(self.o3)
         self.affoption_layout12.addWidget(self.o4)
         self.affoption_layout12.addWidget(self.o5)
         self.affoption_layout12.addWidget(self.o6)
         self.affoption_layout12.addWidget(self.o7)
         self.affoption_layout12.addWidget(self.o8)
         self.affoption_layout12.addWidget(self.o9)
         self.affoption_layout12.addWidget(self.o10)
         self.affoption_layout12.addWidget(self.o11)
         self.affoption_layout12.addWidget(self.o12)
         self.affoption_layout12.addWidget(self.o13)
         self.affoption_layout12.addWidget(self.o14)
         self.affoption_layout12.addWidget(self.o15)
         self.affoption_layout12.addWidget(self.o16)
         self.affoption_layout12.addWidget(self.o17)
         self.affoption_layout12.addWidget(self.o18)
         self.affoption_layout12.addWidget(self.o19)
         self.affoption_layout12.addWidget(self.o20)
         self.affoption_layout12.addWidget(self.o21)
         self.affoption_layout12.addWidget(self.o22)
         self.affoption_layout12.addWidget(self.o23)
         self.affoption_layout12.addWidget(self.o24)
         self.affoption_layout12.addWidget(self.o25)
         self.affoption_layout12.addWidget(self.o26)
         self.affoption_layout12.addWidget(self.o27)
         self.affoption_layout12.addWidget(self.o28)
         self.affoption_layout12.addWidget(self.o29)
         self.affoption_layout12.addWidget(self.o30)
         self.affoption_layout12.addWidget(self.o31)
         self.affoption_layout12.addWidget(self.o32)
         self.connect(self.selection,SIGNAL("clicked()"),self.affig12)
     def FT(self):
         self.q1 = QCheckBox("Binwalk")
         self.q2 = QCheckBox("bulk-extractor")
         self.q3 = QCheckBox("Capstone")
         self.q4 = QCheckBox("chntpw")
         self.q5 = QCheckBox("Cuckoo")
         self.q6 = QCheckBox("dc3dd")
         self.q7 = QCheckBox("ddrescue")
         self.q8 = QCheckBox("DFF")
         self.q9 = QCheckBox("diStorm3")
         self.q10 = QCheckBox("Dumpzilla")
         self.q11 = QCheckBox("extundelete")
         self.q12 = QCheckBox("Foremost")
         self.q13 = QCheckBox("Galleta")
         self.q14 = QCheckBox("Guymager")
         self.q15 = QCheckBox("iPhone Backup Analyzer")
         self.q16 = QCheckBox("p0f")
         self.q17 = QCheckBox("pdf-parser")
         self.q18 = QCheckBox("pdfid")
         self.q19 = QCheckBox("pdgmail")
         self.q20 = QCheckBox("peepdf")
         self.q21 = QCheckBox("RegRipper")
         self.q22 = QCheckBox("Volatility")
         self.q23 = QCheckBox("Xplico")
         self.affoption_layout13.addWidget(self.q1)
         self.affoption_layout13.addWidget(self.q2)
         self.affoption_layout13.addWidget(self.q3)
         self.affoption_layout13.addWidget(self.q4)
         self.affoption_layout13.addWidget(self.q5)
         self.affoption_layout13.addWidget(self.q6)
         self.affoption_layout13.addWidget(self.q7)
         self.affoption_layout13.addWidget(self.q8)
         self.affoption_layout13.addWidget(self.q9)
         self.affoption_layout13.addWidget(self.q10)
         self.affoption_layout13.addWidget(self.q11)
         self.affoption_layout13.addWidget(self.q12)
         self.affoption_layout13.addWidget(self.q13)
         self.affoption_layout13.addWidget(self.q14)
         self.affoption_layout13.addWidget(self.q15)
         self.affoption_layout13.addWidget(self.q16)
         self.affoption_layout13.addWidget(self.q17)
         self.affoption_layout13.addWidget(self.q18)
         self.affoption_layout13.addWidget(self.q19)
         self.affoption_layout13.addWidget(self.q20)
         self.affoption_layout13.addWidget(self.q21)
         self.affoption_layout13.addWidget(self.q22)
         self.affoption_layout13.addWidget(self.q23)
         self.connect(self.selection,SIGNAL("clicked()"),self.affig13)
     def PA(self):
         self.r1 = QCheckBox("acccheck")
         self.r2 = QCheckBox("Burp Suite")
         self.r3 = QCheckBox("CeWL")
         self.r4 = QCheckBox("chntpw")
         self.r5 = QCheckBox("cisco-auditing-tool")
         self.r6 = QCheckBox("CmosPwd")
         self.r7 = QCheckBox("creddump")
         self.r8 = QCheckBox("crunch")
         self.r9 = QCheckBox("DBPwAudit")
         self.r10 = QCheckBox("findmyhash")
         self.r11 = QCheckBox("gpp-decrypt")
         self.r12 = QCheckBox("hash-identifier")
         self.r13 = QCheckBox("HexorBase")
         self.r14 = QCheckBox("THC-Hydra")
         self.r15 = QCheckBox("John the Ripper")
         self.r16 = QCheckBox("Johnny")
         self.r17 = QCheckBox("keimpx")
         self.r18 = QCheckBox("Maltego Teeth")
         self.r19 = QCheckBox("Maskprocessor")
         self.r20 = QCheckBox("multiforcer")
         self.r21 = QCheckBox("Ncrack")
         self.r22 = QCheckBox("oclgausscrack")
         self.r23 = QCheckBox("PACK")
         self.r24 = QCheckBox("patator")
         self.r25 = QCheckBox("phrasendrescher")
         self.r26 = QCheckBox("polenum")
         self.r27 = QCheckBox("RainbowCrack")
         self.r28 = QCheckBox("rcracki-mt")
         self.r29 = QCheckBox("RSMangler")
         self.r30 = QCheckBox("SQLdict")
         self.r31 = QCheckBox("Statsprocessor")
         self.r32 = QCheckBox("THC-pptp-bruter")
         self.r33 = QCheckBox("TrueCrack")
         self.r34 = QCheckBox("WebScarab")
         self.r35 = QCheckBox("wordlists")
         self.r36 = QCheckBox("zaproxy")
         self.affoption_layout14.addWidget(self.r1)
         self.affoption_layout14.addWidget(self.r2)
         self.affoption_layout14.addWidget(self.r3)
         self.affoption_layout14.addWidget(self.r4)
         self.affoption_layout14.addWidget(self.r5)
         self.affoption_layout14.addWidget(self.r6)
         self.affoption_layout14.addWidget(self.r7)
         self.affoption_layout14.addWidget(self.r8)
         self.affoption_layout14.addWidget(self.r9)
         self.affoption_layout14.addWidget(self.r10)
         self.affoption_layout14.addWidget(self.r11)
         self.affoption_layout14.addWidget(self.r12)
         self.affoption_layout14.addWidget(self.r13)
         self.affoption_layout14.addWidget(self.r14)
         self.affoption_layout14.addWidget(self.r15)
         self.affoption_layout14.addWidget(self.r16)
         self.affoption_layout14.addWidget(self.r17)
         self.affoption_layout14.addWidget(self.r18)
         self.affoption_layout14.addWidget(self.r19)
         self.affoption_layout14.addWidget(self.r20)
         self.affoption_layout14.addWidget(self.r21)
         self.affoption_layout14.addWidget(self.r22)
         self.affoption_layout14.addWidget(self.r23)
         self.affoption_layout14.addWidget(self.r24)
         self.affoption_layout14.addWidget(self.r25)
         self.affoption_layout14.addWidget(self.r26)
         self.affoption_layout14.addWidget(self.r27)
         self.affoption_layout14.addWidget(self.r28)
         self.affoption_layout14.addWidget(self.r29)
         self.affoption_layout14.addWidget(self.r30)
         self.affoption_layout14.addWidget(self.r31)
         self.affoption_layout14.addWidget(self.r32)
         self.affoption_layout14.addWidget(self.r33)
         self.affoption_layout14.addWidget(self.r34)
         self.affoption_layout14.addWidget(self.r35)
         self.affoption_layout14.addWidget(self.r36)
         self.connect(self.selection,SIGNAL("clicked()"),self.affig14)
     def IG(self):
         self.n1 = QCheckBox("acccheck")
         self.n2 = QCheckBox("ace-voip")
         self.n3 = QCheckBox("Amap")
         self.n4 = QCheckBox("Automater")
         self.n5 = QCheckBox("bing-ip2hosts")
         self.n6 = QCheckBox("braa")
         self.n7 = QCheckBox("CaseFile")
         self.n8 = QCheckBox("CDPSnarf")
         self.n9 = QCheckBox("cisco-torch")
         self.n10 = QCheckBox("Cookie Cadger")
         self.n11 = QCheckBox("copy-router-config")
         self.n12 = QCheckBox("DMitry")
         self.n13 = QCheckBox("dnmap")
         self.n14 = QCheckBox("dnsenum")
         self.n15 = QCheckBox("dnsmap")
         self.n16 = QCheckBox("DNSRecon")
         self.n17 = QCheckBox("dnstracer")
         self.n18 = QCheckBox("dnswalk")
         self.n19 = QCheckBox("DotDotPwn")
         self.n20 = QCheckBox("enum4linux")
         self.n21 = QCheckBox("enumIAX")
         self.n22 = QCheckBox("exploitdb")
         self.n23 = QCheckBox("Fierce")
         self.n24 = QCheckBox("Firewalk")
         self.n25 = QCheckBox("fragroute")
         self.n26 = QCheckBox("fragrouter")
         self.n27 = QCheckBox("Ghost Phisher")
         self.n28 = QCheckBox("GoLismero")
         self.n29 = QCheckBox("lbd")
         self.n30 = QCheckBox("Maltego Teeth")
         self.n31 = QCheckBox("masscan")
         self.n32 = QCheckBox("Metagoofil")
         self.n33 = QCheckBox("Miranda")
         self.n34 = QCheckBox("Nmap")
         self.n35 = QCheckBox("ntop")
         self.n36 = QCheckBox("p0f")
         self.n37 = QCheckBox("Parsero")
         self.n38 = QCheckBox("Recon-ng")
         self.n39 = QCheckBox("SET")
         self.n40 = QCheckBox("smtp-user-enum")
         self.n41 = QCheckBox("snmpcheck")
         self.n42 = QCheckBox("sslcaudit")
         self.n43 = QCheckBox("SSLsplit")
         self.n44 = QCheckBox("sslstrip")
         self.n45 = QCheckBox("SSLyze")
         self.n46 = QCheckBox("THC-IPV6")
         self.n47 = QCheckBox("theHarvester")
         self.n48 = QCheckBox("TLSSLed")
         self.n49 = QCheckBox("twofi")
         self.n50 = QCheckBox("URLCrazy")
         self.n51 = QCheckBox("Wireshark")
         self.n52 = QCheckBox("WOL-E")
         self.n53 = QCheckBox("Xplico")
         self.n54 = QCheckBox("iSMTP")
         self.n55 = QCheckBox("InTrace")
         self.n56 = QCheckBox("hping3")
         self.n57 = QCheckBox("goofile")
         self.affoption_layout.addWidget(self.n1)
         self.affoption_layout.addWidget(self.n2)
         self.affoption_layout.addWidget(self.n3)
         self.affoption_layout.addWidget(self.n4)
         self.affoption_layout.addWidget(self.n5)
         self.affoption_layout.addWidget(self.n6)
         self.affoption_layout.addWidget(self.n7)
         self.affoption_layout.addWidget(self.n8)
         self.affoption_layout.addWidget(self.n9)
         self.affoption_layout.addWidget(self.n10)
         self.affoption_layout.addWidget(self.n11)
         self.affoption_layout.addWidget(self.n12)
         self.affoption_layout.addWidget(self.n13)
         self.affoption_layout.addWidget(self.n14)
         self.affoption_layout.addWidget(self.n15)
         self.affoption_layout.addWidget(self.n16)
         self.affoption_layout.addWidget(self.n17)
         self.affoption_layout.addWidget(self.n18)
         self.affoption_layout.addWidget(self.n19)
         self.affoption_layout.addWidget(self.n20)
         self.affoption_layout.addWidget(self.n21)
         self.affoption_layout.addWidget(self.n22)
         self.affoption_layout.addWidget(self.n23)
         self.affoption_layout.addWidget(self.n24)
         self.affoption_layout.addWidget(self.n25)
         self.affoption_layout.addWidget(self.n26)
         self.affoption_layout.addWidget(self.n27)
         self.affoption_layout.addWidget(self.n28)
         self.affoption_layout.addWidget(self.n29)
         self.affoption_layout.addWidget(self.n30)
         self.affoption_layout.addWidget(self.n31)
         self.affoption_layout.addWidget(self.n32)
         self.affoption_layout.addWidget(self.n33)
         self.affoption_layout.addWidget(self.n34)
         self.affoption_layout.addWidget(self.n35)
         self.affoption_layout.addWidget(self.n36)
         self.affoption_layout.addWidget(self.n37)
         self.affoption_layout.addWidget(self.n38)
         self.affoption_layout.addWidget(self.n39)
         self.affoption_layout.addWidget(self.n40)
         self.affoption_layout.addWidget(self.n41)
         self.affoption_layout.addWidget(self.n42)
         self.affoption_layout.addWidget(self.n43)
         self.affoption_layout.addWidget(self.n44)
         self.affoption_layout.addWidget(self.n45)
         self.affoption_layout.addWidget(self.n46)
         self.affoption_layout.addWidget(self.n47)
         self.affoption_layout.addWidget(self.n48)
         self.affoption_layout.addWidget(self.n49)
         self.affoption_layout.addWidget(self.n50)
         self.affoption_layout.addWidget(self.n51)
         self.affoption_layout.addWidget(self.n52)
         self.affoption_layout.addWidget(self.n53)
         self.affoption_layout.addWidget(self.n54)
         self.affoption_layout.addWidget(self.n55)
         self.affoption_layout.addWidget(self.n56)
         self.affoption_layout.addWidget(self.n57)
         self.connect(self.selection,SIGNAL("clicked()"),self.affig)
     def affiche_IG(self):
         self.affiche_layout = QFrame()
         self.affiche_widget.setWidget(self.affiche_layout)
         self.affoption_layout = QVBoxLayout()
         self.IG()
         self.affiche_layout.setGeometry(0,0,432,1300)
         self.affiche_layout.setLayout(self.affoption_layout)
     def affiche_ET(self):
         self.affiche_layout6 = QFrame()
         self.affiche_widget.setWidget(self.affiche_layout6)
         self.affoption_layout6 = QVBoxLayout()
         self.ET()
         self.affiche_layout6.setGeometry(0,0,432,300)
         self.affiche_layout6.setLayout(self.affoption_layout6)
     def affiche_RT(self):
         self.affiche_layout7 = QFrame()
         self.affiche_widget.setWidget(self.affiche_layout7)
         self.affoption_layout7 = QVBoxLayout()
         self.RT()
         self.affiche_layout7.setGeometry(0,0,432,300)
         self.affiche_layout7.setLayout(self.affoption_layout7)
     def affiche_Ex(self):
         self.affiche_layout5 = QFrame()
         self.affiche_widget.setWidget(self.affiche_layout5)
         self.affoption_layout5 = QVBoxLayout()
         self.Ex()
         self.affiche_layout5.setGeometry(0,0,432,50)
         self.affiche_layout5.setLayout(self.affoption_layout5)
     def affiche_RE(self):
         self.affiche_layout3 = QFrame()
         self.affiche_widget.setWidget(self.affiche_layout3)
         self.affoption_layout3 = QVBoxLayout()
         self.RE()
         self.affiche_layout3.setGeometry(0,0,432,350)
         self.affiche_layout3.setLayout(self.affoption_layout3)
     def affiche_HH(self):
         self.affiche_layout4 = QFrame()
         self.affiche_widget.setWidget(self.affiche_layout4)
         self.affoption_layout4 = QVBoxLayout()
         self.HH()
         self.affiche_layout4.setGeometry(0,0,432,150)
         self.affiche_layout4.setLayout(self.affoption_layout4)
     def affiche_ST(self):
         self.affiche_layout2 = QFrame()
         self.affiche_widget.setWidget(self.affiche_layout2)
         self.affoption_layout2 = QVBoxLayout()
         self.ST()
         self.affiche_layout2.setGeometry(0,0,432,430)
         self.affiche_layout2.setLayout(self.affoption_layout2)
     def affiche_MA(self):
         self.affiche_layout8 = QFrame()
         self.affiche_widget.setWidget(self.affiche_layout8)
         self.affoption_layout8 = QVBoxLayout()
         self.MA()
         self.affiche_layout8.setGeometry(0,0,432,430)
         self.affiche_layout8.setLayout(self.affoption_layout8)
     def affiche_VA(self):
         self.affiche_layout9 = QFrame()
         self.affiche_widget.setWidget(self.affiche_layout9)
         self.affoption_layout9 = QVBoxLayout()
         self.VA()
         self.affiche_layout9.setGeometry(0,0,432,830)
         self.affiche_layout9.setLayout(self.affoption_layout9)
     def affiche_WA(self):
         self.affiche_layout10 = QFrame()
         self.affiche_widget.setWidget(self.affiche_layout10)
         self.affoption_layout10 = QVBoxLayout()
         self.WA()
         self.affiche_layout10.setGeometry(0,0,432,800)
         self.affiche_layout10.setLayout(self.affoption_layout10)
     def affiche_WA2(self):
         self.affiche_layout11 = QFrame()
         self.affiche_widget.setWidget(self.affiche_layout11)
         self.affoption_layout11 = QVBoxLayout()
         self.WA2()
         self.affiche_layout11.setGeometry(0,0,432,1030)
         self.affiche_layout11.setLayout(self.affoption_layout11)
     def affiche_SS(self):
         self.affiche_layout12 = QFrame()
         self.affiche_widget.setWidget(self.affiche_layout12)
         self.affoption_layout12 = QVBoxLayout()
         self.SS()
         self.affiche_layout12.setGeometry(0,0,432,1030)
         self.affiche_layout12.setLayout(self.affoption_layout12)
     def affiche_FT(self):
         self.affiche_layout13 = QFrame()
         self.affiche_widget.setWidget(self.affiche_layout13)
         self.affoption_layout13 = QVBoxLayout()
         self.FT()
         self.affiche_layout13.setGeometry(0,0,432,650)
         self.affiche_layout13.setLayout(self.affoption_layout13)
     def affiche_PA(self):
         self.affiche_layout14 = QFrame()
         self.affiche_widget.setWidget(self.affiche_layout14)
         self.affoption_layout14 = QVBoxLayout()
         self.PA()
         self.affiche_layout14.setGeometry(0,0,432,1030)
         self.affiche_layout14.setLayout(self.affoption_layout14)
     def affiche_ST(self):
         self.affiche_layout2 = QFrame()
         self.affiche_widget.setWidget(self.affiche_layout2)
         self.affoption_layout2 = QVBoxLayout()
         self.ST()
         self.affiche_layout2.setGeometry(0,0,432,430)
         self.affiche_layout2.setLayout(self.affoption_layout2)
     def surfacei(self):
         self.sinfo_layout = QVBoxLayout()
         self.liste = QFrame()
         self.liste.setStyleSheet("border:1px solid green")
         self.console = QTextEdit("<center><font color='white'>Ce programme est le gui de Katoolin creer par lionsec <br>il a ete adaper au gui par EnOK4s w0rms "
                        "                           <br>#H4ckT3ur ")
         self.console.setReadOnly(True)
         self.console.setStyleSheet("border:1px dotted white;")
         self.sinfo_layout.addWidget(self.liste)
         self.sinfo_layout.addWidget(self.console)
         self.choix = QComboBox(self.liste)
         self.choix.addItem("Selectionner ")
         self.choix.addItem("Information Gathering")
         self.choix.addItem("Vulnerability Analysis")
         self.choix.addItem("Wireless Attacks")
         self.choix.addItem("Web Applications")
         self.choix.addItem("Sniffing & Spoofing")
         self.choix.addItem("Maintaining Access")
         self.choix.addItem("Reporting Tools")
         self.choix.addItem("Exploitation Tools")
         self.choix.addItem("Forensics Tools")
         self.choix.addItem("Stress Testing")
         self.choix.addItem("Password Attacks")
         self.choix.addItem("Reverse Engineering")
         self.choix.addItem("Hardware Hacking")
         self.choix.addItem("Extra")
         self.choix.setGeometry(5,5,350,40)
         self.lancer = QPushButton("Afficher",self.liste)
         self.lancer.setGeometry(360,5,78,40)
         self.console.setMaximumSize(QSize(650, 60))
         self.affiche_widget = QScrollArea(self.liste)
         self.affiche_widget.setGeometry(5,50,452,260)
         self.affiche_widget.setStyleSheet("border:none")
         self.surfaceinfo.setLayout(self.sinfo_layout)
         self.connect(self.lancer,SIGNAL("clicked()"),self.affiche)
     def affiche(self):
         c = QString()
         c = self.choix.currentText()
         if c=="Information Gathering":
            print"===========>[\033[92mInformation Gathering\033[0m]<============"
            self.affiche_IG()
         elif c=="Stress Testing":
            print"===========>[\033[92mStress Testing\033[0m]<============"
            self.affiche_ST()
         elif c=="Reverse Engineering":
            print"===========>[\033[92mReverse Engineering\033[0m]<============"
            self.affiche_RE()
         elif c=="Hardware Hacking":
            print"===========>[\033[92mHardware Hacking\033[0m]<============"
            self.affiche_HH()
         elif c=="Extra":
            print"===========>[\033[92mExtra\033[0m]<============"
            self.affiche_Ex()
         elif c=="Exploitation Tools":
            print"===========>[\033[92mExploitation Tools\033[0m]<============"
            self.affiche_ET()
         elif c=="Reporting Tools":
            print"===========>[\033[92mReporting Tools\033[0m]<============"
            self.affiche_RT()
         elif c=="Maintaining Access":
            print"===========>[\033[92mMaintaining Access\033[0m]<============"
            self.affiche_MA()
         elif c=="Vulnerability Analysis":
            print"===========>[\033[92mVulnerability Analysis\033[0m]<============"
            self.affiche_VA()
         elif c=="Wireless Attacks": 
            print"===========>[\033[92mWireless Attacks\033[0m]<============"
            self.affiche_WA()
         elif c=="Web Applications":
            print"===========>[\033[92mWeb Applications\033[0m]<============"
            self.affiche_WA2()
         elif c=="Sniffing & Spoofing":
            print"===========>[\033[92mSniffing & Spoofing\033[0m]<============"
            self.affiche_SS()
         elif c=="Forensics Tools":
            print"===========>[\033[92mForensics Tools\033[0m]<============"
            self.affiche_FT()
         elif c=="Password Attacks":
            print"===========>[\033[92mPassword Attacks\033[0m]<============"
            self.affiche_PA()
     def blist(self):
         #=======[Recherche lancer]======
         self.list_layout = QVBoxLayout()
         self.addppa = QPushButton("Ajouter kali-ppa")
         self.all = QPushButton("Install tout kali")
         self.selection = QPushButton("Install selection")
         self.kalimenu = QPushButton("Ajouter kali-menu")
         self.kaliindicator = QPushButton("kali-indicator")
         self.deleteppa = QPushButton("Update")
         self.propos = QPushButton("sources.list")
         self.fermer = QPushButton("Fermer")
         self.list_layout.addWidget(self.addppa)
         self.list_layout.addWidget(self.all)
         self.list_layout.addWidget(self.selection)
         self.list_layout.addWidget(self.kalimenu)
         self.list_layout.addWidget(self.kaliindicator)
         self.list_layout.addWidget(self.deleteppa)
         self.list_layout.addWidget(self.propos)
         self.list_layout.addWidget(self.fermer)
         self.boutonlist.setLayout(self.list_layout)
         self.connect(self.fermer,SIGNAL("clicked()"),self.close)
         self.connect(self.deleteppa,SIGNAL("clicked()"),self.up)
         self.connect(self.propos,SIGNAL("clicked()"),self.slist)
         self.connect(self.addppa,SIGNAL("clicked()"),self.add)
         self.connect(self.all,SIGNAL("clicked()"),self.ally)
         self.connect(self.kalimenu,SIGNAL("clicked()"),self.kali_menu)
         self.connect(self.kaliindicator,SIGNAL("clicked()"),self.kali_indict)
     def kali_indict(self):
          cmd1 = os.system("add-apt-repository ppa:diesch/testing && apt-get update")
	  cmd = os.system("sudo apt-get install classicmenu-indicator")
     def kali_menu(self):
          cmd1 = os.system("apt-get install kali-menu")
     def ally(self):
          cmd = "acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap ntop p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase inguma jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab webshag websploit wfuzz wpscan xsser zaproxy burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dff dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf regripper volatility xplico dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler sqldict statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy apktool dex2jar python-distorm3 edb-debugger jad javasnoop jd ollydbg smali valgrind yara android-sdk apktool arduino dex2jar sakis3g smali&& wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/"
          ret = QMessageBox.information(self, str("Installation de tout kali"),
                                str("<font size=1>Voulez vous installer Tout les tools de kali?"),
                                QMessageBox.Ok | QMessageBox.No);
          print ret
          if ret==1024:
              os.system("apt-get install "+cmd)
          else:
             pass
     def add(self):
         cmd1 = os.system("apt-key adv --keyserver pgp.mit.edu --recv-keys ED444FF07D8D0BF6")
	 cmd2 = os.system("echo '# Kali linux repositories | Added by Katoolin\ndeb http://http.kali.org/kali kali-rolling main contrib non-free\ndeb http://repo.kali.org/kali kali-bleeding-edge main' >> /etc/apt/sources.list")
     def slist(self):
         os.system("gedit /etc/apt/sources.list & cat /etc/apt/sources.list")
     def up(self):
         os.system("apt-get update -m")
     def close(self):
         sys.exit()
     def __init__(self):
         QWidget.__init__(self)
         self.setStyleSheet(stylesheet)
         self.setFixedSize(680,570)
         self.entete = QFrame()
         self.entete.setMaximumSize(QSize(650, 150))
         self.surface = QFrame()
         self.layout = QVBoxLayout()
         self.layout.addWidget(self.entete)
         self.layout.addWidget(self.surface)
         self.setLayout(self.layout)
         self.entete_layout = QVBoxLayout()
         self.entete.setLayout(self.entete_layout)
         text="==[<font color='green'>katoolin</font>-Gui]==\n"
         self.enteteText = QLabel("<center>"+text+"</center>")
         self.enteteText.setMaximumSize(QSize(650, 50))
         self.enteteText2 = QLabel("<center><font size=0.5 color='white'><em><blink>H4ckT3ur & LionSec</center>")
         self.enteteText2.setMaximumSize(QSize(650, 50))
         self.enteteText3 = QLabel("<center><font size=0.1 color='green'><em><marquee>1111111111111111111111111111111111111111111111111111111111111</center>")
         self.enteteText3.setMaximumSize(QSize(630, 9))
         self.entete_layout.addWidget(self.enteteText)
         self.entete_layout.addWidget(self.enteteText2)
         self.entete_layout.addWidget(self.enteteText3)
         self.surface_layout = QHBoxLayout()
         self.surfaceinfo = QFrame()
         self.surfaceinfo.setStyleSheet("border:none")
         self.boutonlist = QFrame()
         self.boutonlist.setMaximumSize(QSize(2000,1000))
         self.boutonlist.setMinimumSize(QSize(150,430))
         self.surface_layout.addWidget(self.surfaceinfo)
         self.surface_layout.addWidget(self.boutonlist)
         self.blist()
         self.surfacei()
         self.surface.setLayout(self.surface_layout)
     
         
def main():
     app = QApplication(sys.argv)
     fenetre = Fenetre()
     fenetre.show()
     r = app.exec_()
main()
