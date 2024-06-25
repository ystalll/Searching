def sequential_search(daftar_pasien, nama_cari):
    for i in range(len(daftar_pasien)):
        if daftar_pasien[i]['nama'] == nama_cari:
            return i
    return -1

daftar_pasien = []

jumlah_pasien = int(input("Masukkan jumlah pasien: "))

for i in range(jumlah_pasien):
    print(f"Masukkan data pasien ke-{i + 1}:")
    nama = input("Nama: ")
    umur = int(input("Umur: "))
    keluhan = input("Keluhan: ")
    daftar_pasien.append({'nama': nama, 'umur': umur, 'keluhan': keluhan})

nama_cari = input("Masukkan nama pasien yang ingin dicari: ")

index = sequential_search(daftar_pasien, nama_cari)

if index != -1:
    pasien = daftar_pasien[index]
    print(f"Data pasien ditemukan: Nama: {pasien['nama']}, Umur: {pasien['umur']}, Keluhan: {pasien['keluhan']}")
else:
    print(f"Maaf, data pasien tersebut tidak ditemukan.")