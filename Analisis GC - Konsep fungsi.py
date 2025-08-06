def ambil_input_sekuens():
    '''Fungsi ini akan ambi sekuens dari user dan mengembalikannya'''
    input_user = input("Masukkan sekuens DNA : ")
    return input_user

def hitung_komposisi_basa(sekuens):
    '''Fungsi ini akan memberikan nilai value ke dalam dictionary, jika tidak ada maka nilainya 0+1'''
    komposisi =  {}
    for basa in sekuens:
        komposisi[basa] = komposisi.get(basa, 0) + 1
    return komposisi #menambahkan value ke dalam dictionary komposis

def hitung_persentase_gc(komposisi_gc, total_panjang_sekuens):
    '''Fungsi ini akan menerima persentase GC dari dictionary komposisi basa.'''
    jumlah_g = komposisi_gc.get('G', 0) #mengambil jumlah G
    jumlah_c = komposisi_gc.get('C', 0) #mengambil jumlah C

    jumlah_gc_total = jumlah_g + jumlah_c #menghitung total basa di dalam sekuens
    if total_panjang_sekuens == 0:
        return 0.0
    else:
        persentase = (jumlah_gc_total / total_panjang_sekuens)*100
        return persentase 

# Langkah 1 
sekuens_dna_user = ambil_input_sekuens()

# Langkah 2
hitung_persentase = hitung_komposisi_basa(sekuens_dna_user)
total_panjang_sekuens_asli = len(sekuens_dna_user)

# Langkah 3
persentase_gc_akhir = hitung_persentase_gc(hitung_persentase, total_panjang_sekuens_asli)

'''Tampilan hasil akhir pada pengguna'''
print(f"Jumlah basa di sekuens : {hitung_persentase}")

print(f"Panjang sekuens : {total_panjang_sekuens_asli}")

if total_panjang_sekuens_asli > 0:
    print(f"Persentase GC content: {persentase_gc_akhir:.2f}%")
else:
    print("Urutan DNA kosong, tidak dapat menghitung persentase GC.")
