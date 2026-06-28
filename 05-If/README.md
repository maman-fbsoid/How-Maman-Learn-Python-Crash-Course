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

Kita memberi tahu "Eh kalo pas kamu nge cek list dan lihat 'mie ayam' jadikan kapital ya" dan "Kalo enggak yowes di .title() aja" Gituu

Secara teknis sih If akan mengevaluasi setiap elemen. Jika elemen tersebut bernilai True, maka blok kode akan dijalankan. Kalau False, bakal di lewati

## SAMA DENGAN

Oke ini singkat aja gue mau kasih tahu kalian soal tanda `sama dengan` karena di python `=` beda sama `==`

# LANJUT ENTAR YA NGAB
