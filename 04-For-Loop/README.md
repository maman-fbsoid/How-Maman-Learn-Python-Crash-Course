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

Nah selanjutnya kita bakal tambahin string lagi

Langsung saja


```python
makanan = ['manggis', 'nanas', 'apel', 'pisang']
for buah in makanan:
  print(f"Buah {buah.title()} sangat mwanis!")
  print(f"Aku harap aku bisa makan {buah.title()} terus")

print("Kapan kapan lagi deh makan lagi")
```

Nah sekarang kalian udah ngebikin for loop yang ada variasinya *dikit*

# List Angka

Nah sekarang kita bakal belajar loop angka pake range()

Contoh

```python
for value in range(1,5):
  print(value)
```

Outputnya

```python
1
2
3
4
```

Loh kok cuman sampe 4? kan range nya 5

Jadi gini cuy. Saat kita bilang 1,5 tuh komputer mikir "Oh oke gue jalan terus da berhenti di angka kedua dari belakang"

Nah solusinya? kita pake 1,6 bukan 1,5

# List angka pakai range()

Tadi kan udah tuh kita list angka biasa tuh urut biasa ya kebawah

Nah kita bakal pake range() buat bikin list angka

Caranya pake *list()*

Contoh

```python
angka = list(range(1,6))
print(angka)
```

Outputnya

```python
['1', '2', '3', '4', '5']
```

Nah kalian juga bisa bikin kelipatan. Caranya hampir sama

```python
angka = list(range(2,11,2))
print(angka)
```

Outputnya

```python
['2', '4', ''6, '8', '10']
```

Bisa kan?

Nah ku anggap kalian sudah cukup faham jadi aku akan langsung lanjut ke materi selanjutnya yang agak rumit dikit tapi kalian pasti faham

```python
kotak = []
for value in range(1,11):
  kubus = value**2
  kotak.append(kubus)

print(kotak)
```

Outputnya

```python
['1', '4', '9', '16', '25', '36', '49', '64', '81', ''100]
```

Kok gitu bang?

Artinya apa bang MAMAN?!

### Penjelasan

1. `kotak = []`
   - Membuat list kosong untuk menyimpan hasil.

2. `for value in range(1, 11):`
   - Melakukan perulangan dari angka **1** sampai **10**.

3. `kubus = value**2`
   - Menghitung **kuadrat** dari setiap angka.
   - `**2` berarti dipangkatkan 2.
   - Contoh:
     - `1**2 = 1`
     - `2**2 = 4`
     - `3**2 = 9`

4. `kotak.append(kubus)`
   - Menambahkan hasil kuadrat ke dalam list `kotak`.

5. `print(kotak)`
   - Menampilkan seluruh isi list.

Gimana mpruy? faham ga?

Kalo bingunh issue aja yok

Oh dan jika kalian pengen lebih sederhana dan efisien bisa pakai

```python
kotak = []
for value in range(1,11):
  kotak.append(value**2)
```

## Slicing a List

Kita masuk materi selanjutnya yaitu Slicing a List

Apaan tuh bang MAMAAAAN RACING?

Ya intinya ngambil sebagian elemen dari dalam sebuah list

Pake nya gimana?

Nih ku kasih kodenya dan bakal kujelaskan

```python
tanaman = ['wortel', 'sawi', 'selada', 'ambawi', 'jagung']
print(tanaman[0:3])
```

Outputnya

```python
['wortel', 'sawi', 'selada']
```

KOK ISO NGUNU?!

Jadi saat kita melakukan print tuh kit akan sebut ya tanaman[0:3]

Artinya kita bilang "Sebutin tanaman nomor 0 sampe 2"

Loh kan di bilangnya [0:3] bukan [0:2] harusnya sampe ambawi dong!

Inget tadi kubilang soal range kan dimana ya dia bakal berhenti di angka kedua dari belakang angka yang sudah kita sebut

Kalo kamu mau sebut anggaplah langsung 4 elemen juga bisa kok

Nih caranya

```python
tanaman = ['wortel', 'sawi', 'selada', 'ambawi', 'jagung']
print(tanaman[:4])
```

Hasilnya

```python
['wortel', 'sawi', 'selada', 'ambawi']
```

Nah kan 

Cara kerjanya tuh Python lihat "Oh ni bocah ga bilang awalannya. Ok wes langsung aja gw tabrak sampe nomor terakhir itu"

Lalu bisa kita start dari salah salu elemen

Pake ini

```python
tanaman = ['wortel', 'sawi', 'selada', 'ambawi', 'jagung']
print(tanaman[2:])
```

Outputnya

```python
['selada', 'ambawi', 'jagung']
```

Gimana tuh kerjanya?

Jadi Python lihat "Oh mulainya dari nomor 2, oke saatnya laksanakan sampe akhir nomor di list ini"

Nah coba kita gabungkan dengan string dan loop

```python
tanaman = ['wortel', 'sawi', 'selada', 'ambawi', 'jagung']

print("Tanaman favoritku adalah:")
for sayur in tanaman[:3]:
  print(sayur.title())
```

Nah jadi kan

## Copying a List

Sekarang kita akan belajar menyaring sebuah list

Langsung aja kuberi tahu caranya lalu kujelaskan

```python
mainanku = ['komputer', 'airsoft', 'kaido_house']
mainan_budi = mainanku[:]

print("Mainan favoritku adalah:")
print(mainanku)

print("\nMainan favorit Budi adalah:")
print(mainan_budi)
```

Outputnya

```python
Mainan favoritku adalah:
['komputer', 'airsoft', 'kaido_house']

Mainan favorit Budi adalah:
['komputer', 'airsoft', 'kaido_house']
```

Nah jadi kita ngesalin list pertama untuk membuat list kedua

Faham kan?

Saatnya kita hias dikit biar bervariasi *dikit*

```python
mainanku = ['komputer', 'airsoft', 'kaido_house']
mainan_budi = mainanku[:]

mainanku.append('python')
mainan_budi.append('konsol')

print("Mainan favoritku adalah:")
print(mainanku)

print("\nMainan favorit Budi adalah:")
print(mainan_budi)
```

Outputnya

```python
Mainan favoritku adalah:
['komputer', 'airsoft', 'kaido_house', 'python']

Mainan favorit Budi adalah:
['komputer', 'airsoft', 'kaido_house', 'konsol']
```

## Tuples

SELAMAT DATANG DI MATERI TERAKHIR YAITU SOAL *Tuples*

Tuples ya bukan Toples

Jadi apa sih Tuples tuh?

Tuples tuh beda ya sama list biasa tapi mirip dikit

Bedanya tuh kalo list pake [], Tuples pake ()

Contoh

```python
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
```

Outputnya

```python
200
50
```

Nah mirip aja sama List bedanya aja ini lebih kaku

Coba kita gabung sama for loop

```python
dimensions = (200, 50)
for dimension in dimensions:
  print(dimension)
```

Gimana? (Jujur aku sendiri agak bingung pas awal awal)

Nah sekarang akan ku tunjukan sihir dari toples kaca ini

Kita akan memakai teknik `Tuples Unpacking`

Behh namanya aja udah kayak... tukang paket

Nah jadi fungsiny apa sih? lu ga perlu ngetik satu persatu buat munculin elemennya

Oke akan kutunjukan perbedaannya

Manual

```python
# Ada data motor (Nama Barang, Harga)
barang = ("Komputer", 18000)

# Ngambil manual pake indeks
nama = barang[0]
harga = barang[1]

print(nama) 
print(harga)
```

Kalo di lihat kan kepanjangan ya, nah kita coba pake teknik

Teknik

```python
barang = ("Komputer", 18000)

# Proses UNPACKING terjadi di sini:
nama, harga = barang

print(nama)  
print(harga) 
```

Gimana? jauh lebh cepet bukan

Sekarang kita gabungkan sama for loop

```python
antrean_barang = [
("Fahri", "Basikal"),
("Budi", "Blender"),
("Yono", "Drum")
]

for nama, barang in antrean_barang:
  print(f"Tuh masukin barang si {nama}, barangnya {barang}")
```

Gimana? udah dicoba?

Cara kerjanya gimana sih

Jadi si toples, eh toples. Tuples bakal bikin list pake () yang isinya lu bebas tuh mau lu isi angka atau string

Nah terus kalo kita lihat kan itu masih ada [], gunanya apa? kita analogikan kurung siku tuh plastik kresek. Terus kurung biasa (), itu bungkusan pecel di dalam kresek. Lalu "Fahri" dan "Basikal" itu nasi sama lauknya. Faham?

# Penutup dan minta maaf

Baiklah saya Maman dan saya mengakhiri bab ini dengan ucapan terimakasih. Dan juga maaf

Saya minta maaf bila banyak kata kata yang diulang ulang dan juga materi yang kurang lengkap atau diloncat loncat

Jadi sekian dari saya, terimakasih

JANGAN LUPA CUCI MUKA!
