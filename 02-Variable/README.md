## Variable

Baiklah kita masuk ke materi soal variable dan ya ini adalah basic paling penting di Python. Kalo kata emak sih ini adalah *PONDASI KEHIDUPAN*. Anjayyyyy

Oke oke aku serius

## Bagaimana cara pakai Variable?

Baiklah kita akan langsung praktek

Semuanya Siapkan, notepad, code editor atau apapun yang kalian punya

Ikuti langkah ini

- Buat file belajar.py
- Ketik print("Halo dunia!")
- Jalankan

SELAMAT KAMU MENJADI PROGRAMMER

Ya itu adalah ritual pertama masuk Python dan ya semua bahasa sih kayaknya.

Oke kita masuk ke variabel

Jadi Variabel tuh kayak kamu ngasih satu ruangan dan di dalamnya memiliki suatu isi. Contoh aku punya ruangan dengan isi meja. Dan aku akan menyebutkan isinya. Bagaimana aku menyebutkan isi dalam ruangan itu? tentu saja dengan *print*

Contoh

```python
message = "Meja"
print(message)
```

message adalah variabel

print() adalah fungsi untuk menampilkan output ke layar

Selain itu variabel juga kalian sebenarnya bebas sih mau di namain apa. intinya kalian ga harus selalu message. bisa age, umur, negara, kotak dan nama nama lain

Jadi intinya jangan mikir variabel tuh ya cuman satu

## String

String adalah sekumpulan kata dari berbagai variabel yang dijadikan satu

Soo simpelnya di ikat

Jadi anggap kalian punya sebuah baju yang sobek jadi dua dan ingin di jadikan satu dengan benang. Nah itu string

Dan ya... cara pakeknya juga simpel kek matematika (baca: matematika kelas 1 SD)

```python
barang = "Meja"
barang_kedua = "Tas"
print(barang + " " + barang_kedua)
```

Silahkan dicoba yaa

Nah bagaimana jika kita pengen bikin kata katanya disambung sama teks kayak "Saya punya Meja baru"

Kita bakal pake f-string

Simpelnya aja sih ini lebih mudah daripada kalian pake + " " + yang bikin panjang dan ga efisien

Bagaimana contohnya?

```python
barang = "Meja"
print(f"Saya punya {barang} baru")
```

Silahkan di coba yaa

Nah jadi fungsinya gimana?

barang itu variabel

print outputnya

f itu tanda "Eh ini variabelnya jadi satu sama kalimat ya" jadi dipakenya dibelakang tanda kutip

{} sebagai penanda "Eh ini variabelnya jangan di anggep teks biasa ya"

## Loh katanya Python gak pake kurung kurawal?

:V

## Newline

Newline tuh simpelnya ngasih tahu komputer "Ini kalimatnya taruh di baris baru ya"

fungsinya apa? ya sebagai peemberi garis baru agar ga nyampur jadi satu

kita bakal pake *\n*

contoh

```python
print("Halo")
print("\nNama saya Budi")
```

Silahkan dicoba yaa

Nah seperti yang kalian lihat kan, ini tuh bikin baris baru yang ngepisahin dua kalimat agar ga nabrak kek

```python
Halo
Saya Budi
```

Kan kelihatan ga rapi

## Ubah huruf besar/kecil di string dengan metode

Nah kan males ya masa nulis harus caps lock mati nyala

Python punya solusi dengan

.title(), .upper(), dan .lower()

Fungsinya apa?

.title: bikin huruf dari "halo dunia" jadi "Halo Dunia". Fungsinya ubah huruf pertama kalimat jadi kapital

.upper: ubah semua kalimat/kata jadi kapital semua

.lower: ubah semua huruf jadi huruf kecil

Contoh aja sih

```python
nama = "budi"
print(nama.title())
```

Dan

```python
nama = "Fahri Basikal"
print(nama.upper())
print(nama.lower())
```

Silahkan di coba yaa... AH CAPEK GUE BILANG GINI

Oke intinya kalian faham kan? kan?

## Angka

Oke kita masuk akhir materi yaitu Python itu kalkulator

Nah kita belajar matematika TK ya

Simpel aja ada empat simbol yaitu +. -, *, dan /

Faham kan semua fungsinya?

Kalian bisa bikin jika ada angka yang ingin di jumlahkan dulu pake aja ()

Contoh

```python
>>> (2+2) * 2
```

Nah jadi gitu

Kalo mau kelipatan perkalian pake aja **

Contoh

```python
>>> 3 ** 3
```

Nahhhhh

## Catatan

Dulu aku ngira variabel cuman message. padahak ya sebenernya bebas mau di namain apa

> Aslinya karna dulu aku belajar Python cuman karena pengen kelihatan keren aja sih

## Penutup

Baiklah, untuk bab Variabel sebini dulu karena emang mudah ya. jadi see ya semua. maaf kalau ada typo atau salah
