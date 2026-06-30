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

# To Be Continued
