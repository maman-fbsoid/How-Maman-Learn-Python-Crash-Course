## Contoh aja sih ini gabungan semua materi kita coba jadi satu di sini bikin sebuah program sederhana

print("--SELAMAT DATANG DI TOKO MAMAN!--")
print("Di sini kami menyediakan banyak barang")

barang = ['vario', 'beat karbu', 'apel', 'pisang', 'pecel', 'toples', 'helm', 'pedang', 'anggur', 'cirebon']
print(f"Ini adalah barang yang tersedia {barang}")
print("\nSilahkan ingin memesan apa? staff kami akan membantu anda  memilih jadi tenang")

staff = ['amba', 'rusdi', 'mas gatot', 'si imut']
for pekerja in staff:
  print(f"\n{pekerja.title()} akan membantu anda memilih")

print("\natau anda mau memilih sendiri?")

best_seller = barang.pop(1)
underrated = barang.pop(9)

print(f"\nBarang best seller di sini adalah {best_seller.title()}.\n")
message = f"Barang underrated di sini adalah {underrated}"
print(message)

print("Baiklah silahkan mengantri. Kamu juga bisa lihat nomor antrean loh")

daftar_antrean = [
("1", "Budi"),
("2", "Joko"),
("3", "Kamu")
]
for nomor, pelanggan in daftar_antrean:
  print(f"Jadi nomor {nomor} adalah {pelanggan}.")

print("Terimakasih sudah belanja!")
