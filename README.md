# labpy03

Nama: Bagus Sanjaya

NIM: 312410505

Kelas: TI.24.A.5

## Latihan1

1. Mengimpor modul random:

![gambar](screenshot2/lt1hs1.png)

Random adalah modul bawaan python yang berisi fungsi-fungsi untuk menghasilkan bilangan acak.

2. Meminta input dari pengguna:

![gambar](screenshot2/lt1hs2.png)

Program meminta pengguna untuk memasukan nilai N, yang merupakan jumlah bilangan acak yang ingin ditampilkan.

Fungsi input digunakan untuk mengambil input dari pengguna, dan int digunakan untuk mengonversi input menjadi bilangan bulat.

3. Inisialisasi variabel count:

![gambar](screenshot2/lt1hs3.png)

count diiniaialisasi dengan nilai 1, yang akan digunakan untuk melacak jumlah bilangan acak yang telah ditampilkan.

4. Loop while:

![gambar](screenshot2/lt1hs4.png)

loop while digunakan untuk menjalankan blok kode di dalamnya selama kondisi count < n+1 terpenuhi.

5. Menghasilkan bilangan acak:

![gambar](screenshot2/lt1hs5.png)

random.ramndom() menghasilkan bilangan acak antara 0 dan 1.

6. Mengecek nilai bilangan acak:

![gambar](screenshot2/lt1hs6.png)

Kondisi if digunakan untuk mengecek apakah bilangan acak yang dihasilkan lebih kecil dari 0.5.

7. Menampilkan bilangan acak:

![gambar](screenshot2/lt1hs7.png)

Jika bilangan acak kurang dari 0.5, program akan menampilkan bilangan tersebut dengan format "data ke {count} = {angka}".

Menggunaan f-string untuk menyisipkan nilai count dan angka ke dalam string.

8. Increment count:

![gambar](screenshot2/lt1hs8.png)

count dinaikan satu setelah menampilkan bilangan acak yang valid.

## Ini adalah code pemogramannya:

![gambar](screenshot2/latihan1.png)

## Ini adalah hasil pemogramannya

![gambar](screenshot2/hasil1.png)

## Latihan2

1. Inisialisasi modal awal:

![gambar](screenshot2/lt2hs1.png)

Mengatur modal awal sebesar Rp 100.000.000.

2. Inisialisasi total keuntungan:

![gambar](screenshot2/lt2hs2.png)

Mengatur total keuntungan awal bulan sebesar 0.

3. Loop untuk menghitung keuntungan setiap bulan:

![gambar](screenshot2/lt2hs3.png)

Loop for digunakan untuk iterasi dari bulan 1 hingga bulan 8 (dalam range(1, 9)).

4. Pengdondisikan untuk menghitung laba berdasarkan bulan:

![gambar](screenshot2/lt2hs4.png)

Kondisi if-elif digunakan untuk menentukan laba per bulan berdasarkan bulan tertentu:

Bulan 1 dan 2: Tidak ada laba (laba = 0).

Bulan 3 dan 4: Laba 1% dari modal awal.

Bulan 5, 6, dan 7: Laba 5% dari modal awal.

Bulan 8: Laba 3% dari modal awal.

5. Menampilkan laba setiap bulan:

![gambar](screenshot2/lt2hs5.png)

Menampilkan laba setiap bulan dalam format yang rapi.

6. Menambahkan Laba Bulanan ke total keuntungan:

![gambar](screenshot2/lt2hs6.png)

Laba bulanan ditambahkan ke total keuntungan secara akumulatif.

7. Menampilkan total keuntungan setelah 8 bulan:

![gambar](screenshot2/lt2hs7.png)

Setelah loop selesai, program akan menampilkan total keuntungan selama 8 bulan.

## Ini adalah code pemogramannya:

![gambar](screenshot2/latihan2.png)

## Ini adalah hasil pemogramannya:

![gambar](screenshot2/hasil2.png)

## Latihan3

1. Inisialisasi saldo:

![gambar](screenshot2/lt3hs1.png)

Mengatur saldo awal pengguna sebesar Rp1000000.

2. Loop utama:

![gambar](screenshot2/lt3hs2.png)

Program berjalan dalam loop tak terbatas hingga pengguna memilih opsi "Keluar".

3. Menampilkan menu utama dan saldo saat ini:

![gambar](screenshot2/lt3hs3.png)

Menampilkan saldo saat ini dan dua opsi: "Tarik Uang" dan "Keluar".

4. Meminta input pengguna:

![gambar](screenshot2/lt3hs4.png)

Meminta pengguna untuk memilih salah satu opsi: 1(Tarik Uang) atau 2(keluar).

5. Proses penarikan uang:

![gambar](screenshot2/lt3hs5.png)

Jika pengguna memilih opsi 1(Tarik Uang):

Program meminta jumlah penarikan dari penggunna.

Mengecek apakah jumlah penarikan lebih besar dari saldo:

-Jika ya, menampilkan pesan bahwa saldo tidak mencukupi.

-Jika tidak, saldo dikurangi dengan jumlah penarikan.

6. Proses keluar:

![gambar](screenshot2/lt3hs6.png)

Jika pengguna memilih opsi 2(Keluar):

Program menampilkan pesan Terima kasih dan keluar dari loop.

7. Pilihan tidak valid:

![gambar](screenshot2/lt3hs7.png)

Jika pengguna memasukan pilihan yang tidak valid:

Program menampilkan pesan error dan kembali ke menu utama.

## Ini adalah code pemogramannya:

![gambar](screenshot2/latihan3.png)

## Ini adalah hasil programnya:

![gambar](screenshot2/hasil3.png)