def atm():
    saldo = 1000000

    while True:
        print(f"\nSaldo saat ini: Rp{saldo:}")
        print("1. Tarik Uang")
        print("2. Keluar")
        
        pilihan = input("Pilih menu (1/2): ")
        
        if pilihan == '1':
            jumlah_tarik = int(input("Masukkan jumlah penarikan: Rp"))
            
            if jumlah_tarik > saldo:
                print("Saldo tidak mencukupi.")
            else:
                saldo -= jumlah_tarik
                print("Penarikan berhasil!")
        
        elif pilihan == '2':
            print("Terima kasih telah menggunakan ATM!")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            
atm()
