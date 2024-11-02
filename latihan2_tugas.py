modal_awal = 100_000_000

total_keuntungan = 0

for bulan in range(1, 9):
    if bulan <= 2:
        laba = 0  
    elif bulan == 3 or bulan == 4:
        laba = 0.01 * modal_awal  
    elif bulan == 5 or bulan == 6 or bulan == 7:
        laba = 0.05 * modal_awal  
    elif bulan == 8:
        laba = 0.03 * modal_awal  
    
    print(f"Laba bulan ke-{bulan} sebesar: Rp{laba:.0f}")
    
    total_keuntungan += laba

print(f"Total laba selama 8 bulan adalah: Rp{total_keuntungan:.0f}")
