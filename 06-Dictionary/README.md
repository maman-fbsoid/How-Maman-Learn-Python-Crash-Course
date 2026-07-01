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

Nah coba kita gabungin sama string

```python
user = {
'XxiDragon': 'budi',
'BocahBegal123': 'epan',
'OrangKokUnik1': 'maman'
}

for username, name in user.items():
  print(f"{username.title()} nama aslinya adalah {name.title()}")
```

Outputnya

```python
Xxidragon nama aslinya adalah Budi
Bocahbegal123 nama aslinya adalah Epan
Orangkokunik1 nama aslinya adalah Maman
```

Nah bisa dilihat bahwa `username` adalah `key` dan `name` adalah `value`

### Loop semua `key` dalam Dictionary

Sekarang kita mencoba `for loop` tapi hanya untuk semua `key` jadi enggak sama `value`

Caranya gimana?

Gini caranya

```python
user = {
'XxiDragon': 'budi',
'BocahBegal123': 'epan',
'OrangKokUnik1': 'maman'
}

for username in user.keys():
  print(username.title())
```

Outputnya

```python
Xxidragon
Bocahbegal123
Orangkokunik1
```

Nah bisa di lihat caranya hampir sama hanya saja kita memasukan `key` yaitu `username`

Nah kita juga di sini menggunakan `.keys()` bukan `.items()`

Gimana? simpel bukan (i hope kalian faham xixixi)

Oke oke sekarang agak rumit dikit kita

BAKAL GABUNGIN SAMA `LIST` DAN `IF`

Gimana?

Gini

```python
user = {
'XxiDragon': 'budi',
'BocahBegal123': 'epan',
'OrangKokUnik1': 'maman'
}

teman = ['XxiDragon', 'OrangKokUnik1']
for username in user.keys():
  print(username.title())

  if username in teman:
    print(f"  Hai {username.title()}, Aku tahu nama aslimu adalah {user[username].title()}")
```

Nah nah nah nah

Sekarang kalian bingung? tenang itu wajar

Jadi disini kita memakai `for name in user.keys` sebagai loop dan list `teman` dan di dalam for loop ada `if` statements

Nah di dalam list ada `['XxiDragon', 'OrangKokUnik1']` lalu kita pakai `if username in teman` untuk nunjukin "Eh kalau nanti di dalam key ada nama di dalam list nanti lakuin ini ya" yang akhirnya munculin `Hai XxiDragon, Aku tahu nama aslimu adalah Budi`

Gitu

### Loop Directory yang sudah di urutkan

Nah ini logicnya simpel sih

```python
user = {
'XxiDragon': 'budi',
'BocahBegal123': 'epan',
'OrangKokUnik1': 'maman'
}

for username in sorted(user.keys()):
  print(f"{username.title()}, Makasih udah mabar")
```

Outputnya

```python
Bocahbegal123, Makasih udah mabar
Orangkokunik1, Makasih udah mabar
Xxidragon, Makasih udah mabar
```

Nah intinya ini fungsinya sama kayak `.sort()`

YAITU ngurutin

### Values

Kan tadi udah `key` sekarang pake `values`

Caranya ya sama aja sih sama bikin `.keys()` tapi kita pake `.values()`

Contoh

```python
user = {
'XxiDragon': 'budi',
'BocahBegal123': 'epan',
'OrangKokUnik1': 'maman'
}

print("Party ku punya nama yaitu:")
for nama in user.values():
  print(nama.title())
```

Gimana? sama bukan?

## List Dictionary

Sekarang kita akan gabungkan Dictionary dengan list

Hah maksudnya?

Ya iya, kita gabungin dua hal itu

Caranya?

```python
user_0 = {'role': 'ksatria', 'level': 80}
user_1 = {'role': 'penyihir', 'level': 89}
user_2 = {'role': 'archer', 'level': 121}

party = [user_0, user_1, user_2]

for player in party:
  print(player)
```

Fungsinya apa kok harus di list gitu?

Fungsinya biar kalian ga nulis satu persatu key dictionary. Jadi lebih EFISIEN

Nah sekarang coba kita bikin for loop pake list kosong dengan nambahin banyak player dengan role serta level

Gimana? Sini praktek dulu, jelasin belakangan

```python
user = []

for user_number in range(30):
  new_user = {'status': 'player', 'role': 'ksatria', 'level': 999}
  user.append(new_user)

for player in user[:5]:
  print(player)
print("...")

print(f"Total semua player yang login adalah {(len(user))}")
```

Hahaha ada beberapa yang mungkin aku lupa ajarin disini

Pertama bisa kita lihat kita pakai `range()` untuk memberi tahu ke python bahwa "Ini nanti lanjut terus sampe 30 oke"

Nah lalu `user[:5]` itu buat bilang "Eh tunjukin aja 5 loop pertama oke"

Lalu ada `len()` yang buat ngitung isi datanya

BTW

Outputnya

```python
{'status': 'player', 'role': 'ksatria', 'level': 999}
{'status': 'player', 'role': 'ksatria', 'level': 999}
{'status': 'player', 'role': 'ksatria', 'level': 999}
{'status': 'player', 'role': 'ksatria', 'level': 999}
{'status': 'player', 'role': 'ksatria', 'level': 999}
...
Total semua player yang login adalah 30
```

Gituuuuuuuuuuuuu

Nahh sekarang kita bakalan coba variasi dikit

```python
user = []

for user_number in range(30):
  new_user = {'status': 'player', 'role': 'ksatria', 'level': 999}
  user.append(new_user)

for player in user[0:3]:
  if player['status'] == 'player':
    player['status'] = 'moderator'
    player['role'] = 'rogue'
    player['level'] = '9999'

for player in user[:5]:
  print(player)
print("...")
```

Outputnya

```python
{'status': 'moderator', 'role': 'rogue', 'level': '9999'}
{'status': 'moderator', 'role': 'rogue', 'level': '9999'}
{'status': 'moderator', 'role': 'rogue', 'level': '9999'}
{'status': 'player', 'role': 'ksatria', 'level': 999}
{'status': 'player', 'role': 'ksatria', 'level': 999}
...
```

Nah simpelnya di situ kalo di Python tahu "oh kalo statusnya itu player, nanti di awal 3 user yang masuk itu harus ku ubah"

Gitu deh

## List di dalam Dictionary

Kita bakal kasih list di dalam sebuah Dictionary

Emang bisa? ya bisa

Gimana?

Gini

```python
user = {
'role': 'rogue',
'jobs': ['lumberjack', 'fisherman']
}

print(f"Selamat datang di kota Lymhurst, Rolemu adalah {user['role']}. Dan pekerjaanmu adalah:")

for job in user['jobs']:
  print(f"\t{job}")
```

Outputnya

```python
Selamat datang di kota Lymhurst, Rolemu adalah rogue. Dan pekerjaanmu adalah:
        lumberjack
        fisherman
```

Nah bisa di lihat kan list berguna lagi dalam Dictionary

Sekarang ada satu pertanyaan... APA itu `\t`

Simpelnya ini mirip `\n` aatau ya newline tetapi ini bikin tab

Jadi di awal kalimatnya ga bakal mojok tappi otomatis ke spasi pake tab

## Dictionary di Dictionary

Materi terakhir soal Dictionary di dalam Dictionary

Jadi bakal ada Dictionary di dalam Dictionary

:V

Langsung saja kita ke contohnya

```python
user = {
        'MAMANFUNGKY': {
            'role': 'ksatria',
            'job': 'fisherman',
            'level': 99,
            },
        'XxiDragon': {
            'role': 'rogue',
            'job': 'lumberjack',
            'level': 90,
            },

        }

for username, user_info in user.items():
    print(f"\nUsername: {username}")
    role_and_job = user_info['role'] + " dan " + user_info['job']
    level = user_info['level']

    print(f"\tRole and Job: {role_and_job.title()}")
    print(f"\tLevel: {level}")
```

Outputnya

```python
sername: MAMANFUNGKY
        Role and Job: Ksatria Dan Fisherman
        Level: 99

Username: XxiDragon
        Role and Job: Rogue Dan Lumberjack
        Level: 90
```

Nah bisa di lihat bahwa disini kita nulis dalam `user` ada dua player yaitu `MAMANFUNGKY` dan `XxiDragon`

Dan akhirnya di print dalam for loop

Di dalam for loop bisa di lihat kita bikin variabel baru yaitu `role_and_job` dan `level`

Ya buat mempermudah dalam program

# Penutup

Wah udah selesai rupanya, baiklah, ucapan penutupnya ga panjang panjang

Cuman

Makasih yang udah baca repo ini dan mendapatkanilmu python dari sini. Semoga ilmunya bermanfaat

ADIOS!
