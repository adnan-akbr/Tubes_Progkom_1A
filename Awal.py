# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 01:27:14 2020

@author: adnan akbar
"""

import customer
import Admin

def Awal():
    while(True):
        print(">===========================================<")
        print(">                                           <")
        print(">    SELAMAT DATANG DI TOKO HAPPY FRESH!    <")
        print("> 🚩Pucang Sawit, Surakarta, Jawa Tengah🚩 <")
        print(">              +6281230526092               <")
        print(">                                           <")
        print(">       Dapatkan kemudahan berbelanja       <")
        print(">         hanya di TOKO HAPPY FRESH         <")
        print(">               • 100% FRESH •              <")
        print(">             • 100% HIGIENIS •             <")
        print(">            • 100% TERJANGKAU •            <")
        print(">                                           <")
        print(">      ❗Pengirimiman Khusus Area Solo❗      <")
        print(">          MENERIMA COD DAN TRANSFER        <")
        print(">                                           <")
        print(">          ❗❗❗ HAPPY SHOPPING ❗❗❗          <")
        print(">              GRAB YOURS FAST              <")
        print(">                                           <")
        print("> ========================================= <")
        print("Enter 1. jika anda Admin")
        print("Enter 2. Jika and pembeli")
        print("Enter 3. To exit")
        try:
            a=int(input("pilih angka 1-3: "))
            print()
            if(a==1):
                Admin.Admin()
            elif(a==2):
                customer.customer()
            elif(a==3):
                print("Terima kasih telah menggunakan propgram Happy Fresh")
                break
            else:
                print("Please enter a valid choice from 1-3")
        except ValueError:
            print("Please input as suggested.")
Awal()