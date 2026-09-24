"""
Tugas 4 - Praktikum Algoritma & Pemrograman
Sistem Loket Terpadu & Audit Transaksi Ekspedisi Wahana
Nama   : Raldo Restanggi Alfarizy
NIM    : 2611533018
Materi : if tunggal, if-elif-else + operator logika, multi-if terpisah
         (diskon akumulasi), dan match-case
"""

print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")


# Input Data Pengunjung & String Handling

nama_pengunjung_3018 = input("Masukkan Nama Pengunjung        : ")
umur_3018 = int(input("Input umur anda                 : "))
sim_3018 = input("Apakah Anda Sudah Punya SIM C (y/t): ").strip().lower()
jumlah_tiket_3018 = int(input("Masukkan jumlah tiket           : "))

# Validasi kelogisan jumlah tiket (if tunggal)
if jumlah_tiket_3018 <= 0:
    print("Peringatan: Kuota tiket tidak valid!")


# Pemilihan Wahana Menggunakan match-case (kasus 1-5 + default _)
print("\nPilihan Paket Wahana (1-5):")
print("  1. Safari Rimba         (Rp 50,000)")
print("  2. Arung Jeram          (Rp 75,000)")
print("  3. Motor ATV Ekstrim    (Rp 120,000)")
print("  4. Roller Coaster Kilat (Rp 100,000)")
print("  5. All-Access VIP       (Rp 220,000)")
paket_3018 = int(input("Masukkan nomor paket (1-5)      : "))

match paket_3018:
    case 1:
        nama_wahana_3018 = "Wahana Safari Rimba"
        harga_satuan_3018 = 50000
    case 2:
        nama_wahana_3018 = "Wahana Arung Jeram"
        harga_satuan_3018 = 75000
    case 3:
        nama_wahana_3018 = "Wahana Motor ATV Ekstrim"
        harga_satuan_3018 = 120000
    case 4:
        nama_wahana_3018 = "Wahana Roller Coaster Kilat"
        harga_satuan_3018 = 100000
    case 5:
        nama_wahana_3018 = "Wahana All-Access VIP"
        harga_satuan_3018 = 220000
    case _:
        print("Paket wahana tidak valid!")
        exit()

is_member_3018 = input("Apakah Anda member? (y/t)       : ").strip().lower()
kode_promo_valid_3018 = input("Apakah kode promo valid? (y/t)  : ").strip().lower()


# Validasi Izin Kendali Wahana
#    - Paket 3 (ATV): if-elif-else dengan operator logika (and, !=)
#    - Paket lain   : if-else sederhana (umur >= 10)
#    Ditulis sebagai SATU rangkaian if-elif-else (tanpa nested-if)
#    dengan menggabungkan syarat paket_3018 == 3 di setiap kondisi.

print("\n--- KELAYAKAN PENGENDARA WAHANA ---")

if paket_3018 == 3 and umur_3018 >= 17 and sim_3018 == 'y':
    print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
elif paket_3018 == 3 and umur_3018 >= 17 and sim_3018 != 'y':
    print("Status Akses: Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
elif paket_3018 == 3 and umur_3018 < 17 and sim_3018 == 'y':
    print("Status Akses: Identitas tidak valid: Belum cukup umur memiliki SIM.")
elif paket_3018 == 3:
    print("Status Akses: Anda belum cukup umur dan tidak boleh bawa motor ATV.")
elif umur_3018 >= 10:
    print(f"Status Akses: Anda memenuhi syarat umur untuk {nama_wahana_3018}.")
else:
    print(f"Status Akses: Anda belum cukup umur untuk {nama_wahana_3018}.")


# 4. Akumulasi Diskon Bertingkat Menggunakan Multi-IF Terpisah
subtotal_3018 = harga_satuan_3018 * jumlah_tiket_3018
total_diskon_persen_3018 = 0

if subtotal_3018 >= 200000:
    total_diskon_persen_3018 += 10          # Diskon Belanja Besar

if is_member_3018 in ['y', 'ya']:
    total_diskon_persen_3018 += 5           # Diskon Member

if kode_promo_valid_3018 in ['y', 'ya']:
    total_diskon_persen_3018 += 15          # Diskon Voucher Promo

if jumlah_tiket_3018 >= 5:
    total_diskon_persen_3018 += 5           # Diskon Tambahan Rombongan

nominal_diskon_3018 = subtotal_3018 * (total_diskon_persen_3018 / 100)
total_bayar_3018 = subtotal_3018 - nominal_diskon_3018


# Evaluasi Kelulusan Audit Menggunakan if-else
if total_bayar_3018 > 300000:
    catatan_layanan_3018 = "Selamat! Anda berhak mendapatkan Souvenir Gratis."
else:
    catatan_layanan_3018 = "Terima kasih telah berkunjung."

print("\n--- Rincian Pembayaran ---")
print(f"Subtotal Belanja : Rp {subtotal_3018:,.0f}")
print(f"Total Diskon     : {total_diskon_persen_3018}% (Rp {nominal_diskon_3018:,.0f})")
print(f"Total Bayar      : Rp {total_bayar_3018:,.0f}")
print(f"Catatan Layanan  : {catatan_layanan_3018}")
print("Program Selesai")