# --- MENGHITUNG GC DARI SEKUNS

# 1. User input sekuen (string)p
komposisi_sekuens = {}#dictionary kosong untuk simpan hasil perhitungan
total_basa = 0 #jumlah awal dari total basa untuk dijumlahkan 
user_input_sekuens = input("Masukkan sekuens DNA : ")

# 2. Mengolah data sekuens dari user
user_sekuens = user_input_sekuens.upper()

for basa in user_sekuens:
    if basa in komposisi_sekuens:
        komposisi_sekuens[basa] += 1 #jika basa ditemukan di dictionary maka ditambah 1
    else:
        komposisi_sekuens[basa] =1 #jika basa tidak ditemukan di dalam dictionary
# 3. Cetak komposisi sekuens setelah pengolahan data
print(f"Komposisi basa : {komposisi_sekuens}")

 # 4. Jumlah seluruh basa dalam sekuens user
jumlah_g = komposisi_sekuens.get('G', 0)
jumlah_c = komposisi_sekuens.get('C', 0)
akses_data_value = jumlah_g + jumlah_c

# 5. Hitung persentasei GC dari sekuens
total_basa = len(user_sekuens)

if total_basa > 0:
    persentase_GC = (akses_data_value / total_basa) * 100
    print(f"Jumlah komposisi GC : {akses_data_value}")
    print(f"Total basa dalam sekuens : {total_basa}")
    print(f"persentase GC : {persentase_GC}")
else:
    print("Urutan DNA kosong, tidak bisa menghitung persentase.")


