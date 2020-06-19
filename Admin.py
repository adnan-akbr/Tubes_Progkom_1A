import csv
import getpass
import os
from os import system

def ulang():
    print(">=====================================================================<")
    print(">                            PROGRAM ADMIN                            <")
    print(">                             HAPPY FRESH                             <")
    print(">                   🚩Pucang Sawit, Surakarta, Jawa Tengah🚩         <")
    print(">                           +6281230526092                            <")
    print(">=====================================================================<")
    print("daftar menu : ")
    print("Enter 1. Tambah Daftar Daging")
    print("Enter 2. Tambah Daftar Buah")
    print("Enter 3. Tambah Daftar Sayur")
    print("Enter 4. Daftar Daging")
    print("Enter 5. Daftar Buah")
    print("Enter 6. Daftar Sayur")
    print("Enter 7. To exit")
    x = input("Input nomer yang ingin diinginkan(dalam angka) : ")
    if x == "1":
        namafile = 'daging.csv'
        kodemenu = int(input("Masukkan Kode Menu : "))
        namamenu = input("Masukkan Nama Menu: ")
        hargamenu = int(input("Harga Menu: "))

        csvheader = ['Kode', 'Menu', 'Harga']
        with open(namafile, 'a', newline='\n') as filecsv:
            
            
            dictmenu = {'Kode': kodemenu, 'Menu': namamenu, 'Harga': hargamenu}
            
            writer = csv.DictWriter(filecsv, fieldnames = csvheader)
            
            
            if os.stat(namafile).st_size == 0:
                writer.writeheader()
            else:
                None
                    
                writer.writerow(dictmenu)

    elif x == "2":
        namafile = 'buah.csv'
        kodemenu = int(input("Masukkan Kode Menu : "))
        namamenu = input("Masukkan Nama Menu: ")
        hargamenu = int(input("Harga Menu: "))
                 
        csvheader = ['Kode', 'Menu', 'Harga']
            
            
        with open(namafile, 'a', newline='\n') as filecsv:
            
            
            dictmenu = {'Kode': kodemenu, 'Menu': namamenu, 'Harga': hargamenu}
            
            writer = csv.DictWriter(filecsv, fieldnames = csvheader)
            
            
            if os.stat(namafile).st_size == 0:
                writer.writeheader()
            else:
                None
                    
                writer.writerow(dictmenu)

    elif x == "3":
        namafile = 'sayur.csv'
        kodemenu = int(input("Masukkan Kode Menu : "))
        namamenu = input("Masukkan Nama Menu: ")
        hargamenu = int(input("Harga Menu: "))
                 
        csvheader = ['Kode', 'Menu', 'Harga']
            
            
        with open(namafile, 'a', newline='\n') as filecsv:
            
            
            dictmenu = {'Kode': kodemenu, 'Menu': namamenu, 'Harga': hargamenu}
            
            writer = csv.DictWriter(filecsv, fieldnames = csvheader)
            
            
            if os.stat(namafile).st_size == 0:
                writer.writeheader()
            else:
                None
                    
                writer.writerow(dictmenu)

    elif x == "4":
        namafile = 'daging.csv'
        with open (namafile) as filecsv:
            readCSV = csv.reader (filecsv,delimiter = ',')
            line_count = 0
                    
            for row in readCSV:
                if line_count == 0:
                    print (f"Nama Kolom: \n{row}")
                    line_count += 1
                        
                else:
                    line_count += 1
                    print (row)
                    jmldata = int(line_count - 1)
            print ("Jumlah Produk: ", jmldata) 
                        
    elif x == "5":
        namafile = 'buah.csv'
        with open (namafile) as filecsv:
            readCSV = csv.reader (filecsv,delimiter = ',')
            line_count = 0
                    
            for row in readCSV:
                if line_count == 0:
                    print (f"Nama Kolom: \n{row}")
                    line_count += 1
                        
                else:
                    line_count += 1
                    print (row)
                    jmldata = int(line_count - 1)
            print ("Jumlah Produk: ", jmldata) 
                        
    elif x == "6":
        namafile = 'sayur.csv'
        with open (namafile) as filecsv:
            readCSV = csv.reader (filecsv,delimiter = ',')
            line_count = 0
                    
            for row in readCSV:
                if line_count == 0:
                    print (f"Nama Kolom: \n{row}")
                    line_count += 1
                        
                else:
                    line_count += 1
                    print (row)
                    jmldata = int(line_count - 1)
            print ("Jumlah Produk: ", jmldata) 

                
    elif x == "7":
        print("Terima kasih, Semangat!")
    
    else:
        print("Please enter a valid choice from 1-7")
                
    loop = input("Apakah Anda ingin memakai lagi Program Happy Fresh? (pilih y/t): ") 
    
    if loop == "y":
        ulang() #gen isoh neng menu awal/menu admin
    elif loop == "t" :
        print("------Terima kasih atas kunjungannya------")
        system.exit()

       
        

def Admin():
    from os import system   
    system ("cls")
    print ("")
    print(">=====================================================================<")
    print(">                            PROGRAM ADMIN                            <")
    print(">                             HAPPY FRESH                             <")
    print(">                   🚩Pucang Sawit, Surakarta, Jawa Tengah🚩         <")
    print(">                           +6281230526092                            <")
    print(">=====================================================================<")
    print ("")
    print ("NB: Saat memasukkan password, huruf yang diketik memang tidak terlihat")
    print ("")
    username = input("Masukkan Username: ")
    password = getpass.getpass("Masukkan Password: ")
    filepass = open("password.txt", "r")
    for line in filepass.readlines():
        us, pw = line.strip().split(",")
        if (username == us) and (password == pw):
            print ("")
            print ("Login Berhasil")
            ulang()
            

            
