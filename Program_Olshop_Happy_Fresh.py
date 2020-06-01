from os import system

while True :
    ulang = "y"
    totalharga= 0
    print(">==========================================<")
    print(">                                          <")
    print(">  SELAMAT DATANG DI TOKO HAPPY FRESH!     <")
    print("> 🚩Pucang Sawit, Surakarta, Jawa Tengah🚩 <")
    print(">             +6281230526092               <")
    print(">                                          <")
    print(">       Dapatkan kemudahan berbelanja      <")
    print(">         hanya di TOKO HAPPY FRESH        <")
    print(">              • 100% FRESH •              <")
    print(">            • 100% HIGIENIS •             <")
    print(">           • 100% TERJANGKAU •            <")
    print(">                                          <")
    print(">      ❗Pengirimiman Khusus Area Solo❗     <")
    print(">         MENERIMA COD DAN TRANSFER        <")
    print(">                                          <")
    print(">          ❗❗❗ HAPPY SHOPPING ❗❗❗          <")
    print(">             GRAB YOURS FAST              <")
    print(">                                          <")
    print("> ======================================== <")
    print()
    while ulang == 'y':
        print("Produk-produk yang kami tawarkan : ")
        print("1.Daging Sapi\n2.Buah\n3.Sayur ")
        jp = input("Input nomer jenis belanjaan Anda(dalam angka) : ")
        if jp == "1" :
            listDaging = []

            listDaging.append("1. Tenderloin = 170000")
            listDaging.append("2. Sirloin = 150000")
            listDaging.append("3. Rib eye = 140000")
            listDaging.append("4. Brisket = 120000")
            listDaging.extend(["5. Oxtail = 130000"])  # Menambahkan beberapa data ke bagian akhir
            for isi in listDaging:
                print(isi)
            option = int(input("Jenis daging apa yang ingin Anda beli?: "))
            if option == 1:
                qnty = int(input("Masukkan jumlah daging: "))
                total = qnty * 170000
                print("Harga:Rp " + str(total))
            elif option == 2:
                qnty = int(input("Masukkan jumlah daging: "))
                total = qnty * 150000
                print("Harga:Rp " + str(total))
            elif option == 3:
                qnty = int(input("Masukkan jumlah daging: "))
                total = qnty * 140000
                print("Harga:Rp " + str(total))
            elif option == 4:
                qnty = int(input("Masukkan jumlah daging: "))
                total = qnty * 120000
                print("Harga:Rp " + str(total))
            elif option == 5:
                qnty = int(input("Masukkan jumlah daging: "))
                total = qnty * 130000
                print("Harga:Rp " + str(total))
            else:
                print("Opsi tidak ditemukan")
        elif jp == "2" :
            listBuah =[]

            listBuah.append("1. Mangga = 30000") 
            listBuah.append("2. Jeruk = 20000")
            listBuah.append("3. Apel = 50000")
            listBuah.append("4. Pir = 25000")
            listBuah.extend(["5. Buah naga = 30000"]) # Menambahkan beberapa data ke bagian akhir
            for isi in listBuah:
                print(isi)
            option = int(input("Jenis buah apa yang ingin Anda beli?: "))

            if option == 1:
                qnty = int(input("Masukkan jumlah buah: "))
                total = qnty * 30000
                print("Harga:Rp " + str(total))
            elif option == 2:
                qnty = int(input("Masukkan jumlah buah: "))
                total = qnty * 20000
                print("Harga:Rp " + str(total))
            elif option == 3:
                qnty = int(input("Masukkan jumlah buah: "))
                total = qnty * 50000
                print("Harga:Rp " + str(total))
            elif option == 4:
                qnty = int(input("Masukkan jumlah buah: "))
                total = qnty * 25000
                print("Harga:Rp " + str(total))
            elif option == 5:
                qnty = int(input("Masukkan jumlah buah: "))
                total = qnty * 30000
                print("Harga:Rp " + str(total))
            else:
                print("Opsi tidak ditemukan")

        elif jp == "3" :
            listSayur =[]

            listSayur.append("1. Brokoli = 40000") 
            listSayur.append("2. Wortel = 20000")
            listSayur.append("3. Kentang = 25000")
            listSayur.append("4. Cabai = 25000")
            listSayur.extend(["5. Kembang kol = 35000"]) # Menambahkan beberapa data ke bagian akhir
            for isi in listSayur:
                print(isi)
                option = int(input("Jenis sayur apa yang ingin Anda beli?: "))

            if option == 1:
                qnty = int(input("Masukkan jumlah sayur (dalam kg)\t: "))
                total = qnty * 40000
                print("Harga:Rp " + str(total))
            elif option == 2:
                qnty = int(input("Masukkan jumlah sayur (dalam kg)\t: "))
                total = qnty * 20000
                print("Harga:Rp " + str(total))
            elif option == 3:
                qnty = int(input("Masukkan jumlah sayur (dalam kg)\t: "))
                total = qnty * 25000
                print("Harga:Rp " + str(total))
            elif option == 4:
                qnty = int(input("Masukkan jumlah sayur (dalam kg)\t: "))
                total = qnty * 25000
                print("Harga:Rp " + str(total))
            elif option == 5:
                qnty = int(input("Masukkan jumlah sayur (dalam kg)\t: "))
                total = qnty * 35000
                print("Harga \t:Rp " + str(total))
            else:
                print("Opsi tidak ditemukan")
                break
        else :
           system('cls')
           print("-Tidak terdeteksi-")
        totalharga += total
        print("Total belanjaan Anda :", totalharga)
        ulang = input("Apakah Anda ingin menambah keranjang belanjaan? (pilih y/t): ")

        if ulang == "y":
            system('cls')
            True
        elif ulang == "t" :
            print("Total belanjaan Anda :", totalharga)

            nama = input ("Nama: ")
            No_handphone = input ("No Handphone: ")
            Alamat_lengkap = input ("Alamat Lengkap: ")
            alamat = ['Banjarsari', 'Serengan', 'Laweyan', 'Pasar Kliwon', 'Jebres'] 
            print("Daftar Kecamatan: ")
            for i in range (5):
                print(i+1, alamat[i])
            option = str(input("Nama kecamatan : "))
            if option == "Banjarsari":
                system('cls')
                ongkir = 4000
                totalpembayaran = ongkir + totalharga
                print("Nama \t\t: ", nama)
                print("No Handphone \t: ", No_handphone)
                print("Alamat Lengkap \t: ", Alamat_lengkap)
                print("Total belanjaan Anda :", totalharga)
                print("Ongkir               :", ongkir )
                print("                      -------------+")
                print("Total Pembayaran     :", totalpembayaran)
                break
            elif option == "Serengan":
                system('cls')
                ongkir =  3000
                totalpembayaran = ongkir + totalharga
                print("Nama \t\t: ", nama)
                print("No Handphone \t: ", No_handphone)
                print("Alamat Lengkap \t: ", Alamat_lengkap)
                print("Total belanjaan Anda :", totalharga)
                print("Ongkir               :", ongkir )
                print("                      -------------+")
                print("Total Pembayaran     :", totalpembayaran)
                break
            elif option == "Laweyan":
                system('cls')
                ongkir =  5000
                totalpembayaran = ongkir + totalharga
                print("Nama \t\t: ", nama)
                print("No Handphone \t: ", No_handphone)
                print("Alamat Lengkap \t: ", Alamat_lengkap)
                print("Total belanjaan Anda :", totalharga)
                print("Ongkir               :", ongkir )
                print("                      -------------+")
                print("Total Pembayaran     :", totalpembayaran)
                break
            elif option == "Pasar Kliwon":
                system('cls')
                ongkir =  3000
                totalpembayaran = ongkir + totalharga
