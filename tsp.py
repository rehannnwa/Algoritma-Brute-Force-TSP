from itertools import permutations

def hitung_jarak_rute(rute, matriks):
    total = 0
    for i in range(len(rute) - 1):
        total += matriks[rute[i]][rute[i+1]]
    total += matriks[rute[-1]][rute[0]]
    return total

def tsp_brute_force(matriks, nama_lokasi):
    n = len(matriks)
    kota_tujuan = list(range(1, n))

    rute_terbaik = None
    jarak_terbaik = float('inf')
    semua_rute = []

    for perm in permutations(kota_tujuan):
        rute = [0] + list(perm)
        jarak = hitung_jarak_rute(rute, matriks)
        semua_rute.append((rute, jarak))

        if jarak < jarak_terbaik:
            jarak_terbaik = jarak
            rute_terbaik = rute

    return rute_terbaik, jarak_terbaik, semua_rute

# ============================================
# MAIN PROGRAM
# ============================================
print("=" * 55)
print("  Nama  : Rehan Wahyu Andika")
print("  NIM   : [24533915]")
print("  Kelas : 4 C - Teknik Informatika")
print("=" * 55)
print("\n=== Algoritma Brute Force TSP - Simulasi Pengiriman Paket ===\n")

n = int(input("Masukkan jumlah lokasi: "))

nama_lokasi = []
print("\nMasukkan nama setiap lokasi:")
for i in range(n):
    if i == 0:
        nama = input(f"Nama lokasi ke-{i+1} (Gudang/Start): ")
    else:
        nama = input(f"Nama lokasi ke-{i+1} (Rumah pelanggan): ")
    nama_lokasi.append(nama)

print("\nMasukkan jarak antar lokasi (dalam km):")

# Buat matriks kosong dulu
matriks = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n): 
        jarak = int(input(f"Jarak {nama_lokasi[i]} <-> {nama_lokasi[j]}: "))
        matriks[i][j] = jarak
        matriks[j][i] = jarak 

# Tampilkan matriks hasil
print("\n===== MATRIKS JARAK (otomatis terisi) =====")
header = f"{'':12}" + "".join(f"{nama:10}" for nama in nama_lokasi)
print(header)
for i in range(n):
    baris = f"{nama_lokasi[i]:12}" + "".join(f"{matriks[i][j]:<10}" for j in range(n))
    print(baris)

# Proses TSP
rute, jarak, semua_rute = tsp_brute_force(matriks, nama_lokasi)

# Tampilkan semua rute yang dicoba + detail perhitungan
print("\n===== SEMUA KEMUNGKINAN RUTE =====")
for i, (r, j) in enumerate(semua_rute):

    # Nama rute
    rute_nama = [nama_lokasi[k] for k in r] + [nama_lokasi[r[0]]]
    rute_str  = " -> ".join(rute_nama)

    # Detail perhitungan jarak tiap segmen
    segmen = []
    for s in range(len(r) - 1):
        segmen.append(str(matriks[r[s]][r[s+1]]))
    segmen.append(str(matriks[r[-1]][r[0]])) 
    detail_str = " + ".join(segmen) + f" = {j} km"

    print(f"Rute {i+1:2d}: {rute_str} = {detail_str}")
    print()

# Hasil
print("\n===== HASIL TERBAIK =====")
rute_nama = [nama_lokasi[i] for i in rute] + [nama_lokasi[rute[0]]]
print("Rute Optimal :", " -> ".join(rute_nama))
print(f"Total Jarak  : {jarak} km")
print("\nPaket berhasil diantar semua dengan rute terefisien!")