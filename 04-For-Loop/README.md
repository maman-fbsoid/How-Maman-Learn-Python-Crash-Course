## APA itu for loop

Baiklah kita sudah masuk ke bab 4 soal for loop

Jadi for loop adalah perulangan yang kita lakukan kepada list 

Nah comman dyang kita pakai adalah *for nama_variabel in nama_variabel*

Disini kalian akan tahu soal Python pakai spasi bukan tanda kurung

Akan kuberi contoh sederhana dari for loop

```python
makanan = ['manggis', 'nanas', 'apel', 'pisang']
for buah in makanan:
  print(buah)
```
Nah nanti outputnya gimana?

```python
manggis
nanas
apel
pisang
```

Nah gitu, jadi dia bakal langsung ngurutin isi list yang kalian buat

Lebih lengkapnya gini

makanan tuh adalah variabel list kalian

for buah in makanan adalah for loop nya

Nah mungkin kalian bertanya

Bang kenapa kok itu for nya pake buah? kenapa ga pake sekalian sama sama makanan

Ini nih jebakan pemula

Saya dulu juga mikir gitu.

Jadii kenapa kok pake buah? karena gini loh ya. Kalo kita pake for makanan in makanan dan kalian masih mau pakai list makanan di command lain, ya itu bakal bikin masalah karena bisa nabrak. Jadi intinya kita beritahu komputer "Eh mas ini makanannya buah loh ya" gituu

## Tantangan sederhana

Sebelum lanjut coba kalian bikin program for loop dengan clue yang aku berikan

for minuman in warung

for makanan in resto

for gila in rumah_sakit_jiwa

Silahkan dicoba yaa

## Loop lebih lanjut

Coba kita gabungkan dengan string yang  jauh lebih lengkap

Jadi kita akan beri kata kata lanjutan untuk setiap buahnya

Contoh saja

```python
makanan = ['manggis', 'nanas', 'apel', 'pisang']
for buah in makanan:
  print(f"Buah {buah.title()} sangat mwanis!")
```

Nah nanti jadinya bakalan

```python
Buah Manggis sangat mwanis
buah Nanas sangat mwanis
buah Apel sangat mwanis
buah Pisang sangat mwanis
```

How? udah ngeri? kalo ga ngerti gapapa. Coba baca ulang dan praktek ulang (atau maybe mungkin kode ku yang typo :V)

# LANJUT NANTI NGAB DI SURUH MAKAN SAMA EMAK
