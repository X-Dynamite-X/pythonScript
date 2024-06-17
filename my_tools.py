class Tool():
    White = "\033[1;97m"
    Grean = "\033[1;92m"
    Yellow = "\033[1;93m"
    Red = "\033[1;91m"
    # scan open port wepsit           [1]
    def scan_open_port_wepsit():
        import socket
        import platform
        osys=platform.system()
        Tool.clear_os(osys)
        name_folder="scan open port wepsit"
        ip = str(input(Tool.Grean+"Entar ip targit URL: "+Tool.White))
        p1 = int(input(Tool.Red+"Entar first number port: "+Tool.White))
        p2 = int(input(Tool.Red+"Entar end number port: "+Tool.White))
        Tool.folder_programm(name_folder)
        Tool.remove_file(name_folder,ip)
        for p1 in range(p1,p2+1):
            s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.settimeout(1)
            r =s.connect_ex((ip,p1))
            if r == 0 :
                ser = socket.getservbyport(p1)
                print("{}--[* {}{}{} * is open --> {}{}{} ]{}".format(Tool.Yellow,Tool.Grean,p1,Tool.Yellow,Tool.Grean,ser,Tool.Yellow,Tool.White))
                save="--[* {} * is open -->{} ]\n".format(p1,ser)
                Tool.save_file_scan(name_folder,ip,save)
            s.close()
        Tool.start()
    # serch dns domin                 [2]
    def dns_scan():
        import dns.resolver
        import platform
        osys=platform.system()
        Tool.clear_os(osys) 
        name_folder="dns scan"
        Tool.folder_programm(name_folder)
        ip = str (input(Tool.Grean+"Entar targit URL name: "+Tool.White))
        Tool.remove_file(name_folder,ip)
        types = ["A","AAAA","MX","NS","SOA","SRV","CNAME"]
        for i in types:
            d = dns.resolver.query(ip,i,raise_on_no_answer=0)
            if d.rrset is not None:
                print(d.rrset)
                save="{}\n".format(d.rrset)
                Tool.save_file_scan(name_folder,ip,save)
    # network scaner                  [3]
    def net_scan(ip):
        from scapy.all import ARP , Ether ,srp
        from scapy.utils import restart
        import sys
        import platform
        osys=platform.system()
        Tool.clear_os(osys)     
        print(" ")
        id =0
        exitst=[]
        print(f"{Tool.Yellow}ID\t{Tool.Grean}IP \t\t\t\t\t\t {Tool.Red}MAC{Tool.White}")
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
        while 1:
            try:
                arp_erq = ARP(pdst=ip)
                brodcast = Ether(dst ="ff:ff:ff:ff:ff:ff")
                arp_brodcast = brodcast/arp_erq
                result = srp(arp_brodcast,timeout=1,verbose=False)[0]
                lst=[]
                for element in result:
                    clintes = {"ip": element[1].psrc,"mac":element[1].hwsrc}
                    lst.append(clintes)
                for i in lst:
                    if i["mac"] not in exitst:
                        print("{}{}\t{}{} \t\t\t\t{}{} \n".format(Tool.Yellow,id,Tool.Grean,i["ip"],Tool.Red,i["mac"]))
                        id =id+1
                        exitst.append(i["mac"])
            except:
                print("\Exit..!")
                sys.exit()
    # serch number port               [4]
    def scan_port_for_numper():
        import socket
        import platform
        osys=platform.system()
        Tool.clear_os(osys)
        s=socket
        port1 = int(input(f"{Tool.Grean}Entar number port: {Tool.White}"))
        if port1 != "exit":
            int_port=s.getservbyport(port1)
            str_port = str(s.getservbyname(int_port))
            print(Tool.Yellow+"Numper Port: "+Tool.Grean+str_port)
            print(Tool.Yellow+"Name Port: "+Tool.Grean+int_port)
        elif port1 == "exit":
            exit()
    # serch number port               [5]
    def scan_port_for_name():
        import socket
        import platform
        osys = platform.system()
        Tool.clear_os(osys)     
        s=socket
        port1 = str(input(f"{Tool.Grean}Entar name port: {Tool.White}"))
        if port1 != "exit":
            str_port = s.getservbyname(port1)
            int_port=str(s.getservbyport(str_port))
            print("{}Name Port:{}{}".format(Tool.Yellow,Tool.Grean,str_port))
            print("{}Numper Port: {}{}".format(Tool.Yellow,Tool.Grean,int_port))
        elif port1 == "exit":
            exit()
    # serch server                    [6]
    def scan_server():
        import socket
        import platform
        osys=platform.system()
        Tool.clear_os(osys)   
        folder="scan server"
        s=socket
        ip = str(input(f"{Tool.Grean}Entar name target: {Tool.White}"))
        Tool.folder_programm(folder)
        if ip != "exit":
            name_ip=s.gethostbyaddr(ip)
            Tool.remove_file(folder,ip)
            x=0
            for name_ip in name_ip:
                if x==0 :
                    print(f"{Tool.Yellow}server name: {Tool.Grean} {name_ip}")
                    save=f"server name: {name_ip}\n"
                    Tool.save_file_scan(folder,ip,save)
                elif x ==2:
                    print(f"{Tool.Yellow}IP : {Tool.Grean} {name_ip}")
                    save=f"server ip: {name_ip}"
                    Tool.save_file_scan(folder,ip,save)
                x=x+1
        elif ip == "exit":
            exit()    
    # clear os
    def clear_os(osys):
        import os 
        if osys=="Linux":
            os.system("clear")
        elif osys == "Windows":
            os.system("cls")
        elif osys == "Darwin":
            os.system("clear")
    # save serch data for wepsit
    def save_file_scan(name_folder,name_file,data):
        import os 
        pwd =os.getcwd()
        folder=name_folder
        file = name_file
        folder=os.path.join(pwd,folder)
        path_file=os.path.join(folder,"{}.txt".format(file))
        app=open(path_file,"a")
        app.write(data)
        app.close()
    # remove file 
    def remove_file(name_folder,name_file):
        import os 
        pwd =os.getcwd()
        file = name_file
        folder=name_folder
        folder=os.path.join(pwd,folder)
        path_file=os.path.join(folder,"{}.txt".format(file))
        Tool.files_programm(path_file)
    # files programm
    def files_programm(path):
        import os
        path_file=path
        path=os.path.exists(path_file)
        if path ==1:
            Tool.reade_or_remove(path_file)
        else:
            non= " "
    # read file 
    def reade_file(path):
        red=open(path,"r")
        re=red.read()
        print(Tool.Grean+re)
        red.close
        Tool.start()
    # read or remove 
    def reade_or_remove(path):
        import os
        yes_no= input("This file already exists, do you want to delete it? [y,n]:")
        if yes_no == "y":
            os.unlink(path)
        else:
            Tool.reade_file(path)
    # Nwe folder 
    def folder_programm(path):
        import os
        pwd =os.getcwd()
        os.chdir(pwd)
        path_folder=path
        path=os.path.exists(path_folder)
        if path ==0:
            os.mkdir(path_folder)
        else:
            non= " "
    # start Tool 
    def start():
        while 1:
            print(" ")
            print(Tool.White+"\n|_____ 0 == exit \n|_____ 1 == scan open port wepsit\n|_____ 2 == serch dns domin\n|_____ 3 == network scaner\n|_____ 4 == serch numper port\n|_____ 5 == serch name port\n|_____ 6 == serch server\n\t")
            x = int(input(Tool.Grean+"Entar code -------> "+Tool.White))
            if x ==1:
                Tool.scan_open_port_wepsit()
            elif x == 2:
                Tool.dns_scan()
            elif x == 3:
                ip =str (input(Tool.Grean+"Entar ip network :"+Tool.White))
                ip=f"{ip}/24"
                Tool.net_scan(ip)
            elif x == 4:
                Tool.scan_port_for_numper()
            elif x == 5:
                Tool.scan_port_for_name()
            elif x == 6:
                Tool.scan_server()
            elif x == 0:
                exit()
            else :
                print("Erurr")
                print("Entar 0 --> 6")
                Tool.start()

Tool.start()