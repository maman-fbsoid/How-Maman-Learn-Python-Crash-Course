# If Else

Selamat datang kembali teman teman, di bab kali ini kita akan belajar soal If Else

Nah sebelum kita mulai 

## Apa sih If Else itu?

Jadii simpelnya tuh If Else tuh cara program mengambil keputusan berdasarkan kondisi

Kalau suatu kondisi benar (True), program akan menjalankan satu blok kode. Kalau salah (False), program akan menjalankan blok kode lain

Intinya If Else tuh digunakan dalam bahasa pemrograman manapun termasuk python untuk bilang

> "Kalo ini kejadian, lakukan ini"

> "Kalo ini gak kejadian, lakukan ini"

## Mengenal lebih dalam If Else

Bayangkan saja terjadi sebuah kebakaran rumah, jika itu terjadi maka kita harus memadamkannya. Jika tidak, tidak perlu memadamkannya ya karena emang ga ada yang kebakaran kan

Itu dadalah contoh If Else jika di dunia nyata

If = Jika

Else = Jika tidak

Contoh simpel dalam Python

```python
menu = ['baso', 'mie ayam', 'tahu', 'tempe']
for makanan in menu:
  if makanan == 'mie ayam':
    print(makanan.upper())
  else:
    print(makanan.title())
```

Nah, jadi gitu contoh kodenya

Kita memberi tahu pakai operator `==` yang bikin kita bilang ke Python "Eh kalo pas kamu nge cek list dan lihat 'mie ayam' jadikan kapital ya" dan "Kalo enggak yowes di .title() aja" Gituu

Secara teknis sih If akan mengevaluasi setiap elemen. Jika elemen tersebut bernilai True, maka blok kode akan dijalankan. Kalau False, bakal di lewati

Nah sekarang lanjut materi selanjutnya. Akan kukenalkan dengan operator baru yakni `!=` yaitu `tidak sama dengan`

Gimana cara kerjanya?

```python
mobil = 'gtr'
if mobil != 'bmw':
  print("Mobilmu bukan bmw!")
```

Dari kode di atas bisa di simpulkan begini

Variabel mengatakan `gtr` dan kita menggunakan operator `!=` pada `bmw`

Simpelnya yang terjadi Python bertanya "Apakan `gtr` berbeda dengan `bmw`?" jawabannya IYA

Makanya dia bilang "Mobilmu bukan bmw!"

Nah apa yang terjadi jika hasilnya sama?

```python
mobil = 'gtr'
if mobil != 'gtr':
  print("Mobilmu bukan bmw!")
```

Python akan bertanya "Apakah `gtr` berbeda dengan `gtr`?" jawabannya TIDAK

Karna False, akhirnya Outputnya kosong

Kita juga bisa coba ke angka

```python
nilai = 10
if nilai != 100:
  print("Nilaimu bukan 100! kembali ke meja!")
```

Gitu loh ya

## Mengenal operator `not in`

Kita udah belajar soal operator `==` dan `!=` dan sekarang kita akan mempelajari `not in`

Seperti namanya udah jelas, kita memberi tahu kalau `tidak di dalam`

Langsung saja kita ke contohnya

```python
haram = ['babi', 'alkohol']
halal = 'sapi'

if halal not in haram:
  print(f"{halal.title()} adalah makanan halal")
```

Penjelasannya gini

Variabel `haram` kita buat untuk nunjukin tuh apa yang haram

Variabel `halal` nunjukin apa yang halal dan boleh di makan

Nah kita pengen If menunjukan kalau variabel `halal` nih boleh di makan karena ga masuk ke dalam variabel `haram`

Makanya kita pake `not in` buat nunjukin nih ke Python "Elemen di dalam variabel halal nih ga ada di variabel haram jadi dia boleh di makan" Gitu simpelnya

Nah kan si Python udah tahu `halal` ini boleh. Jadi dia ngeluarin output

```python
Sapi adalah makanan halal
```

Gituuu

## If Else untuk angka

Sekarang kita akan belajar operator baru untuk angka yaitu `>=` yaitu lebih dari atau sama dengan

Simpelnya aja nih ya dia bisa tahu elemen yang kamu kasih tuh angkanya lebih atau sama

Langsung aja kita ke contohnya

```python
umur = 19

if umur >= 18:
  print("Kamu bisa ikut milih presiden")
else:
  print("Kau masih bocah untuk memilih siapa pemimpin selanjutnya")
```

Dari sini harusnya udah jelas sih dimana

Variabel yang kita punya kan `19` sedangkan di if statement nya tuh `18` dan variabel kita juga lebih dari `18` yang dimana kita lolos

Ada operator lain yang tugasnya sama

`>` lebih dari (gabisa buat angka yang sama)
`<` kurang dari (gabisa buat angka yang sama)
`<=` kurang dari atau sama dengan (bisa dengan angka yang sama)

## Elif

Beberapa dari kalian mungkin ada yang sudah pernah mendengar istilah ini di bahasa lain atau kalian pernah mendengar kata ini dari seseorang mungkin

Nah `elif` ini fungsinya apa sih???

Fungsinya adalah bikin sebuah percangan dalam If-Else. Maksudny adalah `else if` atau ya kondisi yang lebih dari dua. Jadi kalau kalian pake `if` dan `else` kan cuman buat dua kondisi. Nah `elif` ini buat lebih dari satu

Contoh

```python
umur = 6

if umur < 4:
  print("Kamu boleh masuk ke taman, bayar Rp.2000")
elif umur < 18:
  print("Kamu boleh masuk ke taman, bayar Rp.5000")
else:
  print("Kamu boleh masuk ke taman, bayar Rp.10000")
```

Nah bisa terlihat kita bisa pake sampe 3 kondisi

Kalian juga bisa untuk lebih efisien pake `str()`

Apa tuh bang Messi? Eh bang Maman maksudnya

Jadi `str()` tuh fungsi untuk mengubah nilai menjadi teks dalam string

Emang kenapa pake `str()`?

Alasannya ya alih alih kalian nulis "Kamu boleh masuk ke taman, bayar Rp." kalian bisa langsung jadiin satu aja

Contoh

```python
umur = 6

if umur < 4:
  harga = 2000
elif umur < 18:
  harga = 5000
else:
  harga = 10000

print(f"Kamu boleh masuk, bayar Rp.{str(harga)}.")
```

Nah bisa di lihat kan kalau lebih baik gini karena lebih hemat waktu dan ruang juga

Gimana kalau kita pake `elif` dan tanpa `else`? emang bisa?

BISA.

Contoh

```python
if umur < 4:
  harga = 2000
elif umur < 18:
  harga = 5000
elif umur >= 20:
  harga = 10000

print(f"Kamu boleh masuk, bayar Rp.{str(harga)}.")
```

Nah kok bisa ya `else` ga usah tapi kita pake `elif` dan anehnya bisa

Jawaban simpelnya gini sih

`elif` tidak harus selalu diakhiri dengan `else`. `else` bersifat opsional. Kalau semua kondisi `if` dan `elif` bernilai `False`, maka program hanya akan melewati blok tersebut dan melanjutkan ke kode berikutnya

Faham? tentu dong harusnya faham :V

Next

Sekarang jika kita pengen bikin beberapa kondisi tapi kit apake `if` saja? 

BISA

Contoh

```python
kendaraan = ['motor', 'mobil']

if 'motor' in kendaraan:
  print("Motor adalah kendaraam")
if 'naga' in kendaraan:
  print("Naga bukan kendaraan, patrick")
if 'mobil' in kendaraan:
  print("Mobil adalah kendaraan")

print("\nBaiklah sekian ilmu saya")
```

Nah bisa di lihat kan jadi gitu... anu... ya gitu

Oke oke jadi KOK BISA?

Jawabannya BISA karena

If bakal ngelihat isi dalam list dan selama itu True dia bakal jalanin. Kalau False yo dia ga bakal ngeluarin outputnya

Sekarang coba kita gabungkan sama for loop

```python
garasi = ['motor', 'naga', 'mobil']

for motor in garasi:
    if motor == 'naga':
        print("Naga bukan kendaraan, patrick")
    else:
        print(f"{motor.title()}, adalah kendaraan")

print("\nSekian ilmu dari saya")
```

Nah bisa di lihat kita bilang ke Python kalau "Eh kalau nanti ada naga itu bilang aja itu bukan kendaraan ya"

Gitu

# Penutup dan minta maaf

Oke ternyata udah selesai ya materinya

Gak nyangka kalian baca repo ini (atau gak sih idk but its okay :V)

Nah saya minta maaf kalau ada kode di atas yang eror karena saya juga sering banyak salah

Saya juga berterimakasih soalnya kalian udah mau baca repo ini (buat yang baca aja sih :V)

Soo makasih ya yang udah star, upvote di reddit dan lain lain

Semoga ilmu ini bermanfaat

### ADIOS!
