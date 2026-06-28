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

# TO BE CONTINUED
