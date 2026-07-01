# APA itu Dictionary?

Dictionary adalah tipe data di Python yang digunakan untuk menyimpan data dalam bentuk pasangan key dan value

Simpelnya sih

Kalau list itu seperti deretan barang yang diberi nomor (0, 1, 2, ...), maka dictionary seperti lemari yang setiap lacinya punya label ("nama", "umur", "alamat"). Karena memakai label, data jadi lebih rapi dan mudah dicari.

## Kenapa pake Dictionary?

Kalau pake list nih contoh

```python
player = ['maman', 32, 'kstaria']
```

Terus kamu lihat lagi

```python
player[1]
```

Nah `1` itu apaan?

Nama?

Umur?

Role?

Nah makanya kita pake Dictionary

Contoh

```python
maman = {
'role': 'ksatria',
'umur': 15
}

print(maman['role'])
print(maman['umur'])
```

Outputnya

```python
kstaria
15
```

Nah jadi Dictionary tuh pake `{}`, `:` sebagai pemisah key dan value, `,` untuk misahin setiap pasangan data

Intinya sih ini `list` tapi lebih rapi dan terorganisir

Kalian bisa jadiin string juga

```python
maman = {
'role': 'ksatria',
'umur': 15
}

umur_maman = maman['umur']
print(f"Maman berumur {umur_maman}")
```

## Kenapa harus bikin variabel `umur_maman`? kan bisa langsung di satu print

Medokseh...

Kenapa kok di simpan dulu ke variabel padahal kita bisa langsung 

Kalo kita print langsung gini

```python
maman = {
'role': 'ksatria',
'umur': 15
}

print(f"Maman berumur {maman['umur']}")
```

Ya bebas aja sih

Tapi ya gini loh

Kalo kamu simpan di satu variabel itu bisa buat berkali kali

Tapi ya sesuka kalian toh juga kalian yang nulis. Senyaman kalian aja. Tapi kalo mau ga ribet nulis `maman['umur']` ya coba deh simpen di variabel, pasti enak

## Menambahkan Key dan Value baru

Sekarang kita coba nambahin key dan value baru. Simpel caranya. Lihat gue lihat gue

```python
maman = {
'role': 'ksatria',
'umur': 15
}

maman['makanan'] = 'pecel'
print(maman)
```

Outputnya

```python
{'role': 'ksatria', 'umur': 15, 'makanan': 'pecel'}
```

Nah kan bisa di lihat bahwa makanan ditambahkan

Gimana cara kerjanya?

Kita lihat kita nunjukin Directory kita yaitu `maman[]` di dalam `[]` kita nambahin `makanan` dan lalu kita tambahkan value nya `pecel`

Gituu

Nah kalian juga bisa pake teknik tersebut jika Dictionary kosong

Contoh

```python
maman = {}

maman['role'] = 'ksatria'
maman['umur'] = 15

print(maman)
```

Bisa di lihat bahwa Dictionary maman hanya menggunakan `{}` tanpa elemen di dalamnya yang artinya kalian bisa mengisinya sendiri

## Modifikasi Value

Nah sekarang kita akan belajar gimana cara ngubah suatu value di dalam Dictionary 

Jadi kita bisa ubah value dari key yang ada di Dictionary

Contoh

```python
maman = {'role': 'ksatria'}
print(f"Role pertama maman adalah {maman['role']}")

maman['role'] = 'raja'
print(f"\nRole maman sekarang adalah {maman['role']}")
```

Outputnya

```python
Role pertama maman adalah ksatria

Role maman sekarang adalah raja
```

Nah sekarang kita gabungin sama `if-elif-else`

Gimana? Gini caranya

```python
maman = {
'role': 'ksatria',
'umur': '15',
'level': '25'
}

if maman['role'] == 'penyihir':
  print("Maman adalah seorang penyihir")
elif maman['role'] == 'ksatria':
  print("Maman adalah seorang ksatria")
else:
  print("Role tidak diketahui")
```

Output

```python
Maman adalah seorang ksatria
```

Kita udah belajar menambahkan value. sekarang kita akan menghapus key dan value

Gimana caranya?

Ingat command `del`? kita bakal pake itu

Contoh caranya

```python
maman = {'kolor': 'ijo',
'umur': 15
}

print(maman)
del maman['umur']
print(maman)
```

Outputnya

```python
{'kolor': 'ijo', 'umur': 15}
{'kolor': 'ijo'}
```

Bisa di lihat bahwa

`del` Digunakan untuk menghapus `maman['umur']`

## Loop dengan Dictionary

Sekarang kita akan melakukan for loop dengan Dictionary

Gak beda jauh dengan for loop di `list`

Maka langsung saja kita ke contoh

```python
user = {
'XxiDragon': 'budi',
'BocahBegal123': 'epan',
'OrangKokUnik1': 'maman'
}

for key, value in user.items():
  print(f"\nKey: {key}")
  print(f"Value: {value}")
```

Outputnya

```python
Key: XxiDragon
Value: budi

Key: BocahBegal123
Value: epan

Key: OrangKokUnik1
Value: maman
```

Nah bisa di lihat kan loop nya berhasil

Jadi cara kerjanya gimana?

Pertama kita sudah membuat dictionary `user` dan ya lalu kita melakukan for loop

Jadi gimana sih maksud `for key, value in user.items()`?

Jadi gini loh yak

Bisa di lihat `for key, value in user.items()` maka simpelnya gini. Python ngambil key dan value pada dictionary `user`

Lah `.items()` apaan

Jadi `.items()` tuh tugasnya "Mengambil semua pasangan key dan value" yang ada di dalam dictionary

Jadi dia ngambil semua key dan value di dalam `user`

# TO BE CONTINUED (Aing capek)
