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
