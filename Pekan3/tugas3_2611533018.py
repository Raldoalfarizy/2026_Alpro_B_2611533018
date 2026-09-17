# ==============================================================
# Nama    : Raldo Restanggi Alfarizy
# NIM     : 2611533018
# Kelas   : Praktikum Algoritma dan Pemrograman - Pekan 3
# Topik   : Operator Python
# Studi Kasus : Sistem Simulasi Transaksi dan Validasi Akses Toko
# Catatan : Seluruh nama variabel diakhiri 4 digit terakhir NIM (3018)
# ==============================================================

print("=== SISTEM TRANSAKSI TOKO ===")

# --------------------------------------------------------------
# 1. INPUT DATA PELANGGAN DAN TRANSAKSI
# --------------------------------------------------------------
nama_3018 = input("\nMasukkan Nama Pelanggan : ")
status_3018 = input("Masukkan Status Pelanggan (member/nonmember) : ").strip().lower()
total_belanja_3018 = int(input("Masukkan Total Belanja : "))
jumlah_barang_3018 = int(input("Masukkan Jumlah Barang : "))
kode_promo_3018 = input("Masukkan Kode Promo : ").strip().upper()

# --------------------------------------------------------------
# 2. KONSTANTA / DATA ACUAN TOKO
# --------------------------------------------------------------
batas_belanja_3018 = 200000          # syarat minimum belanja
minimal_barang_3018 = 3              # syarat minimum jumlah barang
persen_diskon_3018 = 10              # besar diskon member (dalam persen)
daftar_promo_3018 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

# --------------------------------------------------------------
# 3. OPERATOR PERBANDINGAN  ( >= , == )
#    Menghasilkan nilai bertipe boolean (True / False)
# --------------------------------------------------------------
syarat_belanja_3018 = total_belanja_3018 >= batas_belanja_3018   # operator >=
syarat_barang_3018 = jumlah_barang_3018 >= minimal_barang_3018   # operator >=
is_member_3018 = status_3018 == "member"                         # operator ==

# --------------------------------------------------------------
# 4. OPERATOR KEANGGOTAAN  ( in , not in )
#    Memeriksa apakah kode promo terdapat pada daftar promo toko
# --------------------------------------------------------------
promo_tersedia_3018 = kode_promo_3018 in daftar_promo_3018           # operator in
promo_tidak_ada_3018 = kode_promo_3018 not in daftar_promo_3018      # operator not in

# --------------------------------------------------------------
# 5. OPERATOR LOGIKA  ( and , or , not )
# --------------------------------------------------------------
dapat_diskon_3018 = is_member_3018 and syarat_belanja_3018        # operator and
dapat_promo_3018 = promo_tersedia_3018 and syarat_barang_3018     # operator and
pelanggan_prioritas_3018 = dapat_diskon_3018 or dapat_promo_3018  # operator or
bukan_member_3018 = not is_member_3018                            # operator not

# --------------------------------------------------------------
# 6. OPERATOR ARITMATIKA  ( * , // , - , % )
# --------------------------------------------------------------
if dapat_diskon_3018:
    diskon_3018 = total_belanja_3018 * persen_diskon_3018 // 100   # operator * dan //
else:
    diskon_3018 = 0

# --------------------------------------------------------------
# 7. OPERATOR PENUGASAN  ( = , -= , += , *= )
# --------------------------------------------------------------
total_bayar_3018 = total_belanja_3018      # operator penugasan dasar ( = )
total_bayar_3018 -= diskon_3018            # augmented assignment ( -= )

poin_3018 = 0
poin_3018 += jumlah_barang_3018 * 10       # augmented assignment ( += )
if is_member_3018:
    poin_3018 *= 2                         # augmented assignment ( *= )

# Perhitungan lanjutan (aritmatika): rata-rata dan sisa pembagian
if jumlah_barang_3018 > 0:
    rata_rata_3018 = total_bayar_3018 // jumlah_barang_3018   # pembagian bulat ( // )
    sisa_bagi_3018 = total_bayar_3018 % jumlah_barang_3018    # sisa bagi ( % )
else:
    rata_rata_3018 = 0
    sisa_bagi_3018 = 0

# --------------------------------------------------------------
# 8. OPERATOR IDENTITAS  ( is , is not )
#    salinan_promo_3018  -> menunjuk objek list yang SAMA
#    duplikat_promo_3018 -> objek BARU dengan isi yang sama
# --------------------------------------------------------------
salinan_promo_3018 = daftar_promo_3018        # referensi ke objek yang sama
duplikat_promo_3018 = daftar_promo_3018[:]    # objek baru hasil penyalinan

identitas_sama_3018 = salinan_promo_3018 is daftar_promo_3018        # operator is
identitas_beda_3018 = duplikat_promo_3018 is not daftar_promo_3018   # operator is not
nilai_sama_3018 = duplikat_promo_3018 == daftar_promo_3018           # operator ==

# --------------------------------------------------------------
# 9. OPERATOR BITWISE  ( | , & , ^ , << )
#    Setiap kondisi pelanggan diwakili satu bit:
#    0001 = member | 0010 = belanja >= 200000
#    0100 = barang >= 3 | 1000 = kode promo tersedia
# --------------------------------------------------------------
bit_member_3018 = 0b0001
bit_belanja_3018 = 0b0010
bit_barang_3018 = 0b0100
bit_promo_3018 = 0b1000

kode_status_3018 = 0
if is_member_3018:
    kode_status_3018 |= bit_member_3018      # operator OR ( | )
if syarat_belanja_3018:
    kode_status_3018 |= bit_belanja_3018     # operator OR ( | )
if syarat_barang_3018:
    kode_status_3018 |= bit_barang_3018      # operator OR ( | )
if promo_tersedia_3018:
    kode_status_3018 |= bit_promo_3018       # operator OR ( | )

cek_member_3018 = kode_status_3018 & bit_member_3018     # operator AND ( & )
cek_promo_3018 = kode_status_3018 & bit_promo_3018       # operator AND ( & )

kode_referensi_3018 = 0b1011                             # kode transaksi pembanding
beda_status_3018 = kode_status_3018 ^ kode_referensi_3018  # operator XOR ( ^ )

geser_kiri_3018 = kode_status_3018 << 1                  # operator geser kiri ( << )

# Hak akses pelanggan ditentukan dari pemeriksaan bit
mask_ongkir_3018 = bit_barang_3018 | bit_promo_3018      # 1100
member_access_3018 = cek_member_3018 == bit_member_3018
promo_access_3018 = cek_promo_3018 == bit_promo_3018
free_shipping_3018 = (kode_status_3018 & mask_ongkir_3018) == mask_ongkir_3018

# ==============================================================
# 10. TAMPILAN HASIL PROGRAM
# ==============================================================
print()
print("=== DATA PELANGGAN ===")
print("Nama Pelanggan       :", nama_3018)
print("Status Pelanggan     :", status_3018)
print("Total Belanja        : Rp" + str(total_belanja_3018))
print("Jumlah Barang        :", jumlah_barang_3018)
print("Kode Promo           :", kode_promo_3018)

print()
print("=== HASIL PERHITUNGAN ===")
print("Besar Diskon         : Rp" + str(diskon_3018))
print("Total Pembayaran     : Rp" + str(total_bayar_3018))
print("Rata-rata Harga      : Rp" + str(rata_rata_3018))
print("Sisa Pembagian (%)   :", sisa_bagi_3018)
print("Poin Pelanggan       :", poin_3018)

print()
print("=== HASIL VALIDASI ===")
print("Belanja >= Rp" + str(batas_belanja_3018) + "   :", syarat_belanja_3018)
print("Jumlah Barang >= " + str(minimal_barang_3018) + "     :", syarat_barang_3018)
print("Status Member          :", is_member_3018)
print("Kode Promo Tersedia    :", promo_tersedia_3018)
print("Mendapatkan Diskon     :", dapat_diskon_3018)
print("Mendapatkan Promo      :", dapat_promo_3018)
print("Pelanggan Prioritas    :", pelanggan_prioritas_3018)

print()
print("=== HAK AKSES PELANGGAN ===")
print("Kode Hak Akses (biner) :", format(kode_status_3018, "04b"))
print("Kode Hak Akses (des)   :", kode_status_3018)
print("Member Access          :", member_access_3018)
print("Promo Access           :", promo_access_3018)
print("Free Shipping Access   :", free_shipping_3018)

print()
print("=== HASIL OPERATOR ===")

print()
print("-- Operator Aritmatika --")
print("Diskon  :", total_belanja_3018, "*", persen_diskon_3018, "// 100 =", diskon_3018)
print("Bayar   :", total_belanja_3018, "-", diskon_3018, "=", total_bayar_3018)
print("Rata2   :", total_bayar_3018, "//", jumlah_barang_3018, "=", rata_rata_3018)
print("Sisa    :", total_bayar_3018, "%", jumlah_barang_3018, "=", sisa_bagi_3018)

print()
print("-- Operator Perbandingan --")
print(total_belanja_3018, ">=", batas_belanja_3018, "=", syarat_belanja_3018)
print(jumlah_barang_3018, ">=", minimal_barang_3018, "=", syarat_barang_3018)
print("'" + status_3018 + "'", "==", "'member'", "=", is_member_3018)

print()
print("-- Operator Logika --")
print("member and belanja cukup (and) =", dapat_diskon_3018)
print("dapat diskon or dapat promo (or) =", pelanggan_prioritas_3018)
print("not member (not) =", bukan_member_3018)

print()
print("-- Operator Penugasan --")
print("total_bayar -= diskon  -> Rp" + str(total_bayar_3018))
print("poin += jumlah*10      -> ", jumlah_barang_3018 * 10)
print("poin *= 2 (jika member)-> ", poin_3018)

print()
print("-- Operator Keanggotaan --")
print("Daftar promo toko :", daftar_promo_3018)
print("'" + kode_promo_3018 + "' in daftar_promo =", promo_tersedia_3018)
print("'" + kode_promo_3018 + "' not in daftar_promo =", promo_tidak_ada_3018)

print()
print("-- Operator Identitas --")
print("salinan is daftar_promo      =", identitas_sama_3018)
print("duplikat is not daftar_promo =", identitas_beda_3018)
print("duplikat == daftar_promo     =", nilai_sama_3018)
print("Kesimpulan: 'is' membandingkan identitas objek, '==' membandingkan nilai/isi objek.")

print()
print("-- Operator Bitwise --")
print("Kode Status Transaksi")
print("Kode Biner   :", format(kode_status_3018, "04b"))
print("Kode Desimal :", kode_status_3018)

print()
print("Cek Member")
print(format(kode_status_3018, "04b"), "&", format(bit_member_3018, "04b"))
print("Hasil Biner   :", format(cek_member_3018, "04b"))
print("Hasil Desimal :", cek_member_3018)

print()
print("Cek Promo")
print(format(kode_status_3018, "04b"), "&", format(bit_promo_3018, "04b"))
print("Hasil Biner   :", format(cek_promo_3018, "04b"))
print("Hasil Desimal :", cek_promo_3018)

print()
print("Perbandingan Status")
print("Kode Transaksi :", format(kode_status_3018, "04b"))
print("Kode Referensi :", format(kode_referensi_3018, "04b"))
print(format(kode_status_3018, "04b"), "^", format(kode_referensi_3018, "04b"))
print("Hasil Biner   :", format(beda_status_3018, "04b"))
print("Hasil Desimal :", beda_status_3018)

print()
print("Shift")
print(format(kode_status_3018, "04b"), "<< 1")
print("Hasil Biner   :", format(geser_kiri_3018, "05b"))
print("Hasil Desimal :", geser_kiri_3018)

print()
print("=== SELESAI ===")