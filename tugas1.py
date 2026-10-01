# variable untuk menyimpan data
nama = input("masukan nama pengguna")
jadwal_senin = input("masukan aktivitas olahraga hari senin")
jadwal_selasa = input("masukan aktivitas olahraga hari selasa")
jadwal_rabu = input("masukan aktivitas olahraga hari rabu")
jadwal_kamis = input("masukan aktivitas olahraga hari kamis")
jadwal_jumat = input("masukan aktivitas olahraga hari jumat")
jadwal_sabtu = input("masukan aktivitas olahraga hari sabtu")
jadwal_minggu = input("masukan aktivitas olahraga hari minggu")

senin = jadwal_senin
selasa = jadwal_selasa
rabu = jadwal_rabu
kamis = jadwal_kamis
jumat = jadwal_jumat
sabtu = jadwal_sabtu
minggu = jadwal_minggu

# update hari rabu
update = input("Masukan Aktivitas Olahraga Hari Rabu : ")
update_time = input("Masukan Periode Tanggal Latihan : ")
status = f"jadwal olahraga milik {nama} telah di perbarui!"

# output
print(f"===INPUT JADWAL OLAHRAGA {nama}===")
print(f"masukan nama pengguna    : {nama}")
print(f"masukan aktivitas senin  : {jadwal_senin}")
print(f"masukan aktivitas selasa : {jadwal_selasa}")
print(f"masukan aktivitas rabu   : {jadwal_rabu}")
print(f"masukan aktivitas kamis  : {jadwal_kamis}")
print(f"masukan aktivitas jumat  : {jadwal_jumat}")
print(f"masukan aktivitas sabtu  : {jadwal_sabtu}")
print(f"masukan aktivitas minggu : {jadwal_minggu}")
print("")
print("=== JADWAL OLAHRAGA 1 MINGGU ===")
print(f"nama    : {nama}")
print(f"senin   : {senin}")
print(f"selasa  : {selasa}")
print(f"rabu    : {rabu}")
print(f"kamis   : {kamis}")
print(f"jumat   : {jumat}")
print(f"sabtu   : {sabtu}")
print(f"minggu  : {minggu}")
print("----------------------------------")
print("")
print("==== PEMBARUAN JADWAL (TAHAP 2) ====")
print(f"Masukan Aktivitas Tambahan Hari rabu : {update}")
print(f"Masukan Periode Tanggal Latihan      : {update_time}")
print("")
print(f"==== JADWAL OLAHRAGA TERBARU ({update_time}) ====")
print("----------------------------------")
print(f"23-02-26, senin  : {senin}")
print("----------------------------------")
print(f"24-02-26, selasa : {selasa}")
print("----------------------------------")
print(f"25-02-26, rabu   : {rabu} & {update}")
print("----------------------------------")
print(f"26-02-26, kamis  : {kamis}")
print("----------------------------------")
print(f"27-02-26, jumat  : {jumat}")
print("----------------------------------")
print(f"28-02-26, sabtu  : {sabtu}")
print("----------------------------------")
print(f"29-02-26, minggu : {minggu}")
print("----------------------------------")
print(f"Status: {status}")
print("")










