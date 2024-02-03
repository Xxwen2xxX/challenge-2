print("<<\tPENJUALAN TOKO-XYZ\t>>")
print("-"*34)

nama = input("nama barang : ")
harga = int(input("harga barang : Rp."))
jumlah_beli = int(input("jumlah beli : "))

subtotal = harga * jumlah_beli
diskon = harga * jumlah_beli * 0.2
total = subtotal + diskon

print(f"subtotal : Rp.{subtotal:>20}")
print(f"Diskon(20%) : Rp.{int(diskon):>17}")
print(f"Total : Rp.{int(total):>23}")

besar_bayar = int(input("besar bayar : Rp.          "))

print("-"*35)
kembalian = besar_bayar -total 
print(f"kembalian : Rp.{kembalian:>20}")
print("Rincian kembalian:")
limapuluh = 0
duapuluh = 0
sepuluh = 0
limaribu = 0
duaribu = 0
seribu = 0
while kembalian >= 50000:
    limapuluh += 1
    kembalian -=50000
while kembalian >= 20000:
    duapuluh += 1
    kembalian -=20000
while kembalian >= 10000:
    sepuluh += 1
    kembalian -=10000
while kembalian >= 5000:
    limaribu += 1
    kembalian -=5000
while kembalian >= 2000:
    duaribu += 1
    kembalian -= 2000
while kembalian >= 1000:
    seribu += 1
    kembalian -=1000
print(f"Rp.50000 : {limapuluh:>24}")
print(f"Rp.20000 : {duapuluh:>24}")
print(f"Rp.10000 : {sepuluh:>24}")
print(f"Rp.5000 : {limaribu:>25}")
print(f"Rp.2000 : {duaribu:>25}")
print(f"Rp.1000 : {seribu:>25}")
