# Buat file dengan nama multi_if2_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Pogram ini menggunakan fungsi input ()
# Program menghitung diskon belanja

# input dari user
total_belanja_3018 = int(input("Masukkan total belanja (Rp): "))

# Input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_3018 = input("Apakah Anda member (y/t): ").strip().lower()
is_member_3018 = input_member_3018 in ['y', 'ya']

# Input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo_3018 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_3018 = input_promo_3018 in ['y', 'ya']

total_diskon_persen_3018 = 0

# Multi-IF terpisah: setiap kondisi diperiksa secara independen
# Diskon bisa ditumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus

if total_belanja_3018 > 100000:
    total_diskon_persen_3018 += 10  # Diskon belanja besar

if is_member_3018:
    total_diskon_persen_3018 += 5  # Diskon member

if kode_promo_valid_3018:
    total_diskon_persen_3018 += 15  # Diskon Voucher

# Menghitung nominal diskon dan total bayar
nominal_diskon_3018 = total_belanja_3018 * total_diskon_persen_3018 / 100
total_bayar_3018 = total_belanja_3018 - nominal_diskon_3018

# Output hasil
print("---Rincian Pembayaran---")
print(f"Total Diskon :  {total_diskon_persen_3018}% (Rp {nominal_diskon_3018:,.0f})") 
print(f"Total bayar : Rp {total_bayar_3018:,.0f}")

print(f"Total diskon yang anda dapatkan: {total_diskon_persen_3018}%")
# Output: Total diskon yang anda dapatkan: 30% jika belanja > 100000, member, dan kode promo valid