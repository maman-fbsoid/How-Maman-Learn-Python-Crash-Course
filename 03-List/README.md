## HALO HALO HALO

Oke oke selamat datang di bab 3 dimana kita akan belajar cara melakukan listing... atau entahlah bagaimana cara bilangnya

## APA itu list?

List adalah tipe data kolektif untuk menyimpan beberapa item dalam variabel

Jadi simpelnya kalian diberi ruangan tapi lebih besar. Lebih luas. Lebih mahal (ga juga sih b aja) dan intinya bisa menyimpan banyak benda

Nah List digunakan untuk apa? untuk mengelola data dalam satu variabel

Kuberi satu permintaan

Eh maksudnya satu contoh

```python
barang = ['meja', 'kursi', 'ayam']
```

Nah itu List

Jadi alih alih variabel barang cuman nyimpen meja, dia bisa nyimpen kursi dan ayam (oke ini aneh sih tapi siapa peduli)

oke coba kita gabungkan dengan print

```python
barang = ['meja', 'kursi', 'ayam']
print(barang)
```

hasilnya gimana?

```python
['meja', 'kursi', 'ayam']
```

Ya dia bakal nyebutin isi list kalian

Nah jika kamu mau nyebut satu bendaa aja juga bisa dengan cara nyebut nomor urutnya

Contohnya

```python
barang = ['meja', 'kursi', 'ayam']
print(barang[0].title())
```

Nah nanti yang bakal muncul adalah

```python
Meja
```

# KOK BISA?

Jadi sebenarnya urutan yang digunakan itu bukaan 123, tapi 0123. Jadi variabel meja itu pakai angka 0 karena dia pertama

Nah karna udah faham, sekarang kita bakal gabungin sama string

```python
teman = ['budi', 'epan', 'topek', 'maman']
message = f"Temanku terbaikku adalah {teman[0].title()}."
print(message)
```

Nah itu dia!

Kenapa kok di jadiin message bang? jawabannya EFISIENSI DALAM MENULIS KODE

Ya karna kalo di taruh di print semua malah jadi kepanjangan dan kelihatan berantakan

## Menambah

Oke anggap kita tadi sudah punya list teman. Tapi kita ingin menambahkan teman tapi tidak mau menulis dalam kolom list

Apakah bisa? tentu bisa malah cukup banyak dipakai

Command yang akan kita pakai adalah *.append()*

Jadi tugasnya adalah nambahin string baru dalam list kita

Contoh

```python
teman = ['budi', 'epan', 'topek', 'maman']
teman.append('bambang')
print(teman)
```

Nah, maka bambang akan masuk dalam list teman

Welcome Bambang

## Menghapus

Nah tadi kan udah tuh nambah teman, sekarang kita akan ngehapus teman

Gimana nyakk caranya?

Kita akan pakai command *del*

Nah dari namanya aja udah jelas. del untuk delete

Contoh
```python
teman = ['budi', 'epan', 'topek', 'maman']
del teman[1]
print(teman)
```

BOOM

Kamu baru saja menghapus epan dari pertemanan

## Mengubah

Kan udah nih soal menambahkan dan menghapus, sekarang saatnya untuk kita mengubah

Hah mengubah? iya kita akan mengubah topek menjadi bambang

Caranya kita akan pakai command *teman[] = 'bambang'*

Contoh

```python
teman = ['budi', 'epan', 'topek', 'maman']
teman[2] = 'bambang'
print(teman)
```

Nah kan sekarang Topek telah diganti dengan bambang

Welcome back bambang

## Insert

Nah sekarang saatnya kita belajar menyisipkan

Insert, jadi ya kalian bisa menyisipkan string dalam list di posisi tertentu

Kita akan menambahkan bambang di nomor 2 tanpa mengganti topek

Caranya gimana? kit akan pakai command *.insert()*

Fungsinya? ya tadi itu menyisipkan string

Contohnya

```python
teman = ['budi', 'epan', 'topek', 'maman']
teman.insert(2, 'bambang')
print(teman)
```

Nah sekarang bambang sudah masuk tanpa mengeluarkan anggota manapun

Welcome bambang

## Menghapus dan Mengambil

Baiklah semuanya sekarang akan ku ajarkan kalian cara mengambil salah satu string dari list

Jadi kita akan memakai *.pop()*

Fungsinya? menghapus elemen dan mengembalikan nilai nya

Jadi langsung saja ke contoh agar kalian faham

Contoh

```python
teman = ['budi', 'epan', 'topek', 'maman']
teman_terbaik = teman.pop()
print(f"Teman terbaikku adalah {teman_terbaik.title()}.")
```

Bagaimana? sudah faham?

Tentu... kalian aslinya tidak faham kan...

Oke oke ku perjelas kalau kalian tidak faham

Variabel teman menunjukan daftar list teman kita

Lalu muncul variabel baru yaitu teman_terbaik untuk menunjukan string mana di list yang ingin di ambil nilainya

Lalu kita buat string untuk menampilkan output

BOOM

Sekarang kalian memberitahu bahwa teman terbaikmu adalah Maman

Nah jika ingin spesifik kita bisa ppakai angka juga untuk nunjukin "Eh ini loh yang di ambil"

Contoh

```python
teman = ['budi', 'epan', 'topek', 'maman']
teman_terbaik = teman.pop(1)
print(f"Teman terbaikku adalah {teman_terbaik.title()}."
```

Nah sekarang teman terbaikmu adalah Epan

## Menghapus elemen berdasarkan isi data

Nah tadi kan udah ada pop()

Sekarang kita pakai kembarannya pop() yaitu *remove()*

Jadi fungsinya menghapus berdasarkan nama. Jadi kita gak pake angka tapi nama

Contoh
```python
teman = ['budi', 'epan', 'topek', 'maman']
teman_terbaik = 'budi'
teman.remove(teman_terbaik)
print(f"\nJadi teman terbaikku adalah {teman_terbaik.title()}.")
```

Nah jelas kan? cuman beda tipis sebenernya

## Menyortir

Nah kita sekarang masuk ke materi selanjutnya dan sekaligus terakhir di bab 3 ini

Oke langsung aja ya

Apa maksudnya menyrotir?

Soo ini tuh command simpel untuk bikin elemen di dalam list bisa di urutkan sesuai hurufnya

Kita akan pakai command *.sort()* yang fungsinya untuk ya itu tadi, mengurutkan

Contoh

```python
makanan = ['mie ayam', 'nasgor', 'bakmi', 'gacoan']
makanan.sort()
print(makanan)
```

Nah udah faham kan? hasilnya gimana? bakal di urutkan sesuai hurufnya kan

Lanjut, kita punya reverse

Kalau sort biasa hanya akan mengurutkan dari depan, reverse bakal bikin urutan kebalik dari belakang

Command yang bakal kita pakai adalah *reverse=True*

Contoh

```python
makanan = ['mie ayam', 'nasgor', 'bakmi', 'gacoan']
makanan.sort(reverse=True)
print(makanan)
```

Nah dia bakal ngurutin bukan dari A ke Z tapi Z ke A

Nah kalian juga bisa balik list nya tapi tidak di urutkan dengan command *.reverse()*

Contoh

```python
makanan = ['mie ayam', 'nasgor', 'bakmi', 'gacoan']
makanan.reverse()
print(makanan)
```

Nah lihat outputnya. Cuman di balik tanpa di urutkan

# Penutup

Di bagian penutup ini, aku ingin bertanya

"LU PADA FAHAM GA?"

Kalo iya

Syukur

Kalo enggak

Yowes

Nah jadi makasih yang udah mau baca repo aneh yang di tulis bocah ini

Kalau begitu ADIOS!
