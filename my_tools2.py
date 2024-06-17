import os 
import re
import requests
from bs4 import BeautifulSoup as bs
import platform
class Tool2:
    #0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    White = "\033[1;97m"
    Grean = "\033[1;92m"
    Yellow = "\033[1;93m"
    Red = "\033[1;91m"
    #    clear cmd and terminal 
    def clear_os(osys):
        if osys=="Linux":
            os.system("clear")
        elif osys == "Windows":
            os.system("cls")
        elif osys == "Darwin":
            os.system("clear")
    #    input  usar command
    def inp_regular_expression_cheatsheet():
        Tool2.regular_expression_cheatsheet()
        inp_comand=str(input("{} Your regular expression:{} ".format(Tool2.Yellow,Tool2.Grean)))
        return inp_comand
    #    help usar codeing 
    def regular_expression_cheatsheet ():
        print("{}Regular expression cheatsheet ".format(Tool2.Red))
        print("\n{}Special characters{}\n".format(Tool2.Grean,Tool2.Yellow))
        print("\ 	escape special characters")
        print(". 	matches any character")
        print("^ 	matches beginning of string")
        print("$ 	matches end of string")
        print("[5b-d] 	matches any chars '5', 'b', 'c' or 'd'")
        print("[^a-c6] 	matches any char except 'a', 'b', 'c' or '6'")
        print("R|S 	matches either regex R or regex S")
        print("() 	creates a capture group and indicates precedence\n")
        print("{}Quantifiers\n{}".format(Tool2.Grean,Tool2.Yellow))
        print("* 	0 or more (append ? for non-greedy)")
        print("+ 	1 or more (append ? for non-greedy)")
        print("? 	0 or 1 (append ? for non-greedy)")
        print("{m} 	exactly mm occurrences")
        print("{m, n} 	from m to n. m defaults to 0, n to infinity")
        print("{m, n}? 	from m to n, as few as possible\n")
        print("{}Special sequences{}\n".format(Tool2.Grean,Tool2.Yellow))
        print("\A 	start of string")
        print("\\"+"b 	matches empty string at word boundary (between \w and \W)")
        print("\B 	matches empty string not at word boundary")
        print("\d 	digit")
        print("\D 	non-digit")
        print("\s 	whitespace: [ \\t\\n\\r\\f\\v]")
        print("\S 	non-whitespace")
        print("\w 	alphanumeric: [0-9a-zA-Z_]")
        print("\W 	non-alphanumeric")
        print("\Z 	end of string")
        print("\g<id> 	matches a previously defined group\n")
        print("{}Special sequences\n{}".format(Tool2.Grean,Tool2.Yellow))
        print("(?iLmsux) 	matches empty string, sets re.X flags")
        print("(?:...) 	non-capturing version of regular parentheses")
        print("(?P...) 	matches whatever matched previously named group")
        print("(?P=) 	digit")
        print("(?#...) 	a comment; ignored")
        print("(?=...) 	lookahead assertion: matches without consuming")
        print("(?!...) 	negative lookahead assertion")
        print("(?<=...) 	lookbehind assertion: matches if preceded")
        print("?<!...) 	negative lookbehind assertion")
        print("(?(id)yes|no) 	match 'yes' if group 'id' matched, else 'no'")
    #0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    #1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    #    seve text for list
    def text_input():
        osys=platform.system()
        Tool2.clear_os(osys)
        lis=[]
        while 1 :
            string=str(input("{}Entar  Your test string: :==> {}".format(Tool2.Yellow,Tool2.Grean)))
            if string !="done":
                x=string
                lis.append(x)
            else : 
                break
        return lis
    #    seve text for list Then print  
    def findall_lis_usar1(lis,code):
        x=1
        for i in lis:
            r=re.findall(code,i)
            for i in r:
                print(f"{Tool2.Red}[{Tool2.Grean}{x}{Tool2.Red}] {Tool2.Red}{Tool2.Yellow}{i}")
                x=x+1
    #    seve text for list Then print  
    def findall_lis1(lis,code):
        x=1
        for i in lis:
            r=re.findall(code,i)
            for i in r:
                print(f"{Tool2.Red}[{Tool2.Grean}{x}{Tool2.Red}] {Tool2.Red}{Tool2.Yellow}{i}")
                x=x+1
    #11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
    #    extract ip                         [1]     [1]
    def serch_ip1(lis):
        ip_code = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
        print("{}This is IP: ".format(Tool2.Grean))
        x=1
        Tool2.findall_lis1(lis,ip_code)
    #    extract E-mile                     [1]     [2]
    def serch_E_mail1(lis):
        E_mail_code = "\S{1,}\@\S{1,}"
        print("{}This is E-maile: ".format(Tool2.Grean))
        Tool2.findall_lis1(lis,E_mail_code)
    #    extract phone                      [1]     [3]
    def serch_phone1(lis):
        osys=platform.system()
        phone_code = "\+\d{1,}\s{1,}\d{1,}\s\d{1,}"
        print("{}This is Phone number: ".format(Tool2.Grean))
        Tool2.findall_lis1(lis,phone_code)
    #    extract email and ip               [1]     [4]
    def serch_email_ip1(lis):
        print(" ")
        Tool2.serch_E_mail1(lis)
        print(" ")
        Tool2.serch_ip1(lis)
    #    extract phone and ip               [1]     [5]
    def serch_phone_ip1(lis):
        print(" ")
        Tool2.serch_phone1(lis)
        print(" ")
        Tool2.serch_ip1(lis)
    #    extract email and phone            [1]     [6]
    def serch_email_phone1(lis):
        print(" ")
        Tool2.serch_E_mail1(lis)
        print(" ")
        Tool2.serch_phone1(lis)
    #    extract email and phone and ip     [1]     [7]
    def serch_email_phone_ip1(lis):
        print(" ")
        Tool2.serch_E_mail1(lis)
        print(" ")
        Tool2.serch_ip1(lis)
        print(" ")
        Tool2.serch_phone1(lis)
    #    extract usar command               [1]     [8]
    def usar_com1(lis):
        osys=platform.system()
        Tool2.clear_os(osys)
        code = Tool2.inp_regular_expression_cheatsheet()
        print("{}This is regular expression cheatsheet:{} ".format(Tool2.Yellow,Tool2.Grean))
        Tool2.findall_lis_usar1(lis,code)
    #    start1 Tool  In a way that the information is written
    def start1():
        osys=platform.system()
        Tool2.clear_os(osys)
        print()
        print("{}[0]{} exit: ".format(Tool2.Red,Tool2.White))
        print("{}[1]{} extract IP :  ".format(Tool2.Red,Tool2.White))
        print("{}[2]{} extract E-mail : ".format(Tool2.Red,Tool2.White))
        print("{}[3]{} extract Phone : ".format(Tool2.Red,Tool2.White))
        print("{}[4]{} extract E-mail and IP : ".format(Tool2.Red,Tool2.White))
        print("{}[5]{} extract Phone and IP : ".format(Tool2.Red,Tool2.White))
        print("{}[6]{} extract E-mail and Phone : ".format(Tool2.Red,Tool2.White))
        print("{}[7]{} extract E-mail and Phone and IP : ".format(Tool2.Red,Tool2.White))
        print("{}[8]{} usar regular expression cheatsheet : ".format(Tool2.Red,Tool2.White))
        num=int(input("{}Entar number extract type: ==> {}".format(Tool2.Yellow,Tool2.Grean)))
        if num == 0:
            exit()
        string=Tool2.text_input()
        if num == 1:
            osys=platform.system()
            Tool2.clear_os(osys)
            Tool2.serch_ip1(string)
        elif num == 2:
            osys=platform.system()
            Tool2.clear_os(osys)
            Tool2.serch_E_mail1(string)
        elif num == 3:
            osys=platform.system()
            Tool2.clear_os(osys)
            Tool2.serch_phone1(string)
        elif num == 4:
            osys=platform.system()
            Tool2.clear_os(osys)
            Tool2.serch_email_ip1(string)
        elif num == 5 :
            osys=platform.system()
            Tool2.clear_os(osys)
            Tool2.serch_phone_ip1(string)
        elif num == 6:
            osys=platform.system()
            Tool2.clear_os(osys)
            Tool2.serch_email_phone1(string)
        elif num == 7:
            osys=platform.system()
            Tool2.clear_os(osys)
            Tool2.serch_email_phone_ip1(string)
        elif num == 8 :
            osys=platform.system()
            Tool2.clear_os(osys)
            Tool2.usar_com1(string)
        else :
            print("ERURR")
            print("please Entar number [1] or [2] or [3] or[4] or [5] or [6] or [7]: ")
            Tool2.start1()
    ##################################################################################################
    #2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
    #    Open the file for reading
    def open_file():
        while 1:
            command = str(input("{}Entar write the command:==>{} ".format(Tool2.Yellow,Tool2.Grean)))
            if command == "pwd":
                pwd = os.getcwd()
                print(pwd)
            elif command == "help":
                print(Tool2.White)
                print("cd 	[ Enter my folder ]")
                print("pwd	[ pwd - print name of current/working directory ]")
                print("ls      [ list directory contents  file color grean    Folder color Red   ]")
                print("exit	[ To exit the program ]")
                print("done	[ To enter my file when I find it ]")
                print("clear	[ pwd - print name of current/working directory ]")
            elif command =="cd" :
                to_file=str(input("Entar name file: "))
                os.chdir(to_file)
            elif command =="ls":
                ls=os.listdir()
                for i in ls:
                    if os.path.isdir(i)==1:
                        print(f"{Tool2.Red}{i}")
                    else:
                        print(f"{Tool2.Grean}{i}")
                print(Tool2.White)
            elif command =="exit":
                exit()
            elif command == "clear":
                osys=platform.system()
                Tool2.clear_os(osys)
            elif command =="done":
                file_read=str(input("{}Enter the name of the file to be read, and its information will be extracted==>{} ".format(Tool2.Yellow,Tool2.Grean)))
                pwd = os.getcwd()
                path =os.path.join(pwd,file_read)
                return path
    #    Read file 
    def read_file(path):
        fi=open(path,"r")
        lis=fi.read()
        return lis
    #    In a way that the information is reading
    def findall_lis2(lis,code):
        x=1
        r=re.findall(code,lis)
        for i in r:
            print(f"{Tool2.Red}[{Tool2.Grean}{x}{Tool2.Red}] {Tool2.Red}{Tool2.Yellow}{i}")
            x=x+1
    #    seve rade for list Then print  
    def findall_lis_usar2(lis,code):
        x=1
        r=re.findall(code,lis)
        for i in r:
            print(f"{Tool2.Red}[{Tool2.Grean}{x}{Tool2.Red}] {Tool2.Red}{Tool2.Yellow}{i}")
            x=x+1
    #22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
    #    extract ip                         [2]     [1]
    def serch_ip2(lis):
        ip_code = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
        print("{}This is IP: ".format(Tool2.Grean))
        x=1
        Tool2.findall_lis2(lis,ip_code)
    #    extract E-mile                     [2]     [2]
    def serch_E_mail2(lis):
        E_mail_code = "\S{1,}\@\S{1,}"
        print("{}This is E-maile: ".format(Tool2.Grean))
        Tool2.findall_lis2(lis,E_mail_code)
    #    extract phone                      [2]     [3]
    def serch_phone2(lis):
        osys=platform.system()
        phone_code = "\+\d{1,}\s{1,}\d{1,}\s\d{1,}"
        print("{}This is Phone number: ".format(Tool2.Grean))
        Tool2.findall_lis2(lis,phone_code)
    #    extract email and ip               [2]     [4]
    def serch_email_ip2(lis):
        print(" ")
        Tool2.serch_E_mail2(lis)
        print(" ")
        Tool2.serch_ip2(lis)
    #    extract phone and ip               [2]     [5]
    def serch_phone_ip2(lis):
        print(" ")
        Tool2.serch_phone2(lis)
        print(" ")
        Tool2.serch_ip2(lis)
    #    extract email and phone            [2]     [6]
    def serch_email_phone2(lis):
        print(" ")
        Tool2.serch_E_mail2(lis)
        print(" ")
        Tool2.serch_phone2(lis)
    #    extract email and phone and ip     [2]     [7]
    def serch_email_phone_ip2(lis):
        print(" ")
        Tool2.serch_E_mail2(lis)
        print(" ")
        Tool2.serch_ip2(lis)
        print(" ")
        Tool2.serch_phone2(lis)
    #    extract read usar command          [2]     [8]
    def usar_com2(lis):
        osys=platform.system()
        Tool2.clear_os(osys)
        code = Tool2.inp_regular_expression_cheatsheet()
        print("{}This is regular expression cheatsheet:{} ".format(Tool2.Yellow,Tool2.Grean))
        Tool2.findall_lis_usar2(lis,code)
    #    start2 Tool  In a way that the information is read
    def start2():
        osys=platform.system()
        Tool2.clear_os(osys)
        print()
        print("{}[0]{} exit: ".format(Tool2.Red,Tool2.White))
        print("{}[1]{} extract IP :  ".format(Tool2.Red,Tool2.White))
        print("{}[2]{} extract E-mail : ".format(Tool2.Red,Tool2.White))
        print("{}[3]{} extract Phone : ".format(Tool2.Red,Tool2.White))
        print("{}[4]{} extract E-mail and IP : ".format(Tool2.Red,Tool2.White))
        print("{}[5]{} extract Phone and IP : ".format(Tool2.Red,Tool2.White))
        print("{}[6]{} extract E-mail and Phone : ".format(Tool2.Red,Tool2.White))
        print("{}[7]{} extract E-mail and Phone and IP : ".format(Tool2.Red,Tool2.White))
        print("{}[8]{} usar regular expression cheatsheet : ".format(Tool2.Red,Tool2.White))
        num=int(input("{}Entar number extract type: ==> {}".format(Tool2.Yellow,Tool2.Grean)))
        if num==0:
            exit()
        path=Tool2.open_file()
        string=Tool2.read_file(path)
        if num == 1:
            # osys=platform.system()
            # Tool2.clear_os(osys)
            Tool2.serch_ip2(string)
        elif num == 2:
            osys=platform.system()
            Tool2.clear_os(osys)
            Tool2.serch_E_mail2(string)
        elif num == 3:
            osys=platform.system()
            Tool2.clear_os(osys)
            Tool2.serch_phone2(string)
        elif num == 4:
            osys=platform.system()
            Tool2.clear_os(osys)
            Tool2.serch_email_ip2(string)
        elif num == 5 :
            osys=platform.system()
            Tool2.clear_os(osys)
            Tool2.serch_phone_ip2(string)
        elif num == 6:
            osys=platform.system()
            Tool2.clear_os(osys)
            Tool2.serch_email_phone2(string)
        elif num == 7:
            osys=platform.system()
            Tool2.clear_os(osys)
            Tool2.serch_email_phone_ip2(string)
        elif num == 8 :
            osys=platform.system()
            Tool2.clear_os(osys)
            Tool2.usar_com2(string)
        else :
            print("ERURR")
            print("please Entar number [1] or [2] or [3] or[4] or [5] or [6] or [7]: ")
            Tool2.start2()
    ###################################################################################################
    #33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    #    Enter the URL you want to get its information
    def req_html(url):
        req= requests.get(url).text
        b=bs(req,"html.parser")
        b=b.find_all()
        for i in b:
            return i
    #    seve text HTML for list Then print
    def findall_lis3(code,url):
        lis=str(Tool2.req_html(url))
        x=1
        r=re.findall(code,lis)
        for i in r:
            print(f"[{x}] {i}")
            x=x+1
    #    seve text HTML for list Then print
    def findall_lis3(code,url):
        lis=str(Tool2.req_html(url))
        x=1
        r=re.findall(code,lis)
        for i in r:
            print(f"[{x}] {i}")
            x=x+1
    #    seve text HTML for list Then print the usar command
    def findall_lis_usar3(code,url):
        lis=str(Tool2.req_html(url))
        x=1
        r=re.findall(code,lis)
        for i in r:
            print(f"{Tool2.Red}[{Tool2.Grean}{x}{Tool2.Red}] {Tool2.Red}{Tool2.Yellow}{i}")
            x=x+1
    #    input URL WEPSIT
    def inp_url():
        url=str(input("Entar URL targit: "))
        return url
    #33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    #    extract ip                         [3]     [1]
    def serch_ip3(lis,url):
        ip_code = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
        print("{}This is IP:{} ".format(Tool2.Yellow,Tool2.Grean))
        Tool2.findall_lis3(ip_code,url)
    #    extract E-mile                     [3]     [2]
    def serch_E_mail3(lis,url):
        E_mail_code = "\S{1,}\@\S{1,}"
        print("{}This is E-maile: {}".format(Tool2.Yellow,Tool2.Grean))
        Tool2.findall_lis3(E_mail_code,url)
    #    extract phone                      [3]     [3]
    def serch_phone3(lis,url):
        phone_code = "\+\d{1,}\s{1,}\d{1,}\s\d{1,}"
        print("{}This is Phone number: {}".format(Tool2.Yellow,Tool2.Grean))
        Tool2.findall_lis3(phone_code,url)
    #    extract email and ip               [3]     [4]
    def serch_email_ip3(lis,url):
        lis=lis
        print(" ")
        Tool2.serch_E_mail3(lis,url)
        print(" ")
        Tool2.serch_ip3(lis,url)
    #    extract phone and ip               [3]     [5]
    def serch_phone_ip3(lis,url):
        lis=lis
        print(" ")
        Tool2.serch_phone3(lis,url)
        print(" ")
        Tool2.serch_ip3(lis,url)
    #    extract email and phone            [3]     [6]
    def serch_email_phone3(lis,url):
        lis=lis
        print(" ")
        Tool2.serch_E_mail3(lis,url)
        print(" ")
        Tool2.serch_phone3(lis,url)
    #    extract email and phone and ip     [3]     [7]
    def serch_email_phone_ip3(lis,url):
        lis=lis
        print(" ")
        Tool2.serch_E_mail3(lis,url)
        print(" ")
        Tool2.serch_ip3(lis,url)
        print(" ")
        Tool2.serch_phone3(lis,url)
    #    extract usar command               [3]     [8]
    def usar_com3(url):
        osys=platform.system()
        Tool2.clear_os(osys)
        code = Tool2.inp_regular_expression_cheatsheet()
        print("{}This is regular expression cheatsheet:{} ".format(Tool2.Yellow,Tool2.Grean))
        Tool2.findall_lis_usar3(code,url)
    #    start3 Tool In a way that the information is URL HTML
    def start3():
        osys=platform.system()
        Tool2.clear_os(osys)
        print(" ")
        print("{}[0]{} exit: ".format(Tool2.Red,Tool2.White))
        print("{}[1]{} extract IP :  ".format(Tool2.Red,Tool2.White))
        print("{}[2]{} extract E-mail : ".format(Tool2.Red,Tool2.White))
        print("{}[3]{} extract Phone : ".format(Tool2.Red,Tool2.White))
        print("{}[4]{} extract E-mail and IP : ".format(Tool2.Red,Tool2.White))
        print("{}[5]{} extract Phone and IP : ".format(Tool2.Red,Tool2.White))
        print("{}[6]{} extract E-mail and Phone : ".format(Tool2.Red,Tool2.White))
        print("{}[7]{} extract E-mail and Phone and IP : ".format(Tool2.Red,Tool2.White))
        print("{}[8]{} usar regular expression cheatsheet : ".format(Tool2.Red,Tool2.White))
        print(" ")
        num=int(input("{}Entar number extract type: ==> {}".format(Tool2.Yellow,Tool2.Grean)))
        if num == 0:
            exit()
        url=Tool2.inp_url()
        string=Tool2.req_html(url)
        if num == 1:
            osys=platform.system()
            Tool2.clear_os(osys)
            Tool2.serch_ip3(string,url)
        elif num == 2:
            osys=platform.system()
            Tool2.clear_os(osys)
            Tool2.serch_E_mail3(string,url)
        elif num == 3:
            osys=platform.system()
            Tool2.clear_os(osys)
            Tool2.serch_phone3(string,url)
        elif num == 4:
            osys=platform.system()
            Tool2.clear_os(osys)
            Tool2.serch_email_ip3(string,url)
        elif num == 5 :
            osys=platform.system()
            Tool2.clear_os(osys)
            Tool2.serch_phone_ip3(string,url)
        elif num == 6:
            osys=platform.system()
            Tool2.clear_os(osys)
            Tool2.serch_email_phone3(string,url)
        elif num == 7:
            osys=platform.system()
            Tool2.clear_os(osys)
            Tool2.serch_email_phone_ip3(string,url)
        elif num == 8:
            Tool2.clear_os(osys)
            Tool2.usar_com3(url)
        else :
            print("ERURR")
            print("please Entar number [1] or [2] or [3] or[4] or [5] or [6] or [7]: ")
            Tool2.start3()
    ###################################################################################################
    def start():
        osys=platform.system()
        Tool2.clear_os(osys)
        while 1:
            print(" ")
            print(f"{Tool2.Red}[0]{Tool2.White} exit : ")
            print(f"{Tool2.Red}[1]{Tool2.White} Enters information by typing it: ")
            print(f"{Tool2.Red}[2]{Tool2.White} Enters the information through a file saved on the computer: ")
            print(f"{Tool2.Red}[3]{Tool2.White} Enters information by URL of my HTML page: ")
            stars_inp=int(input("{}Enter how to read the file: ==>{} ".format(Tool2.Yellow,Tool2.Grean)))
            if stars_inp==0:
                exit()
            elif stars_inp == 1 :
                Tool2.start1()
            elif stars_inp == 2 :
                Tool2.start2()
            elif stars_inp == 3 : 
                Tool2.start3()
            else :
                print("ERURR")
                print("please Entar number [0] or [1] or [2] or [3] ")
                Tool2.start()

Tool2.start()

