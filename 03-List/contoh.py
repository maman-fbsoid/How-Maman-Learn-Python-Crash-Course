## List
teman = ['budi', 'epan', 'topek', 'maman'] ## <- Ini list
print(teman)

## .append()
teman = ['budi', 'epan', 'topek', 'maman']
teman.append('bambang') ## <- ini metode manambahkan
print(teman)

## del
teman = ['budi', 'epan', 'topek', 'maman']
del teman[1] ## <- ini metode menghapus
print(teman)

## mengubah
teman = ['budi', 'epan', 'topek', 'maman']
teman[2] = 'bambang'
print(teman)

## .insert()
teman = ['budi', 'epan', 'topek', 'maman']
teman.insert(2, 'bambang') ## <- ini metode insert
print(teman)

## .pop()
teman = ['budi', 'epan', 'topek', 'maman']
teman_terbaik = teman.pop(2) ## <- ini metode pop
print(f"\nTeman terbaikku ialah {teman_terbaik.title()}.")

## .remove()

teman = ['budi', 'epan', 'topek', 'maman']
teman_jahat = 'epan'
teman.remove(teman_jahat) ## <- metode remove
print(f"\nTemanku yang paling jahat adalah {teman_jahat.title().}")

## .sort()
makanan = ['mbg', 'indomie', 'ayam goreng', 'baso']
makanan.sort() ## <- metode sort
print(makanan)

## reverse=True
makanan = ['mbg', 'indomie', 'ayam goreng', 'baso']
makanan.sort(reverse=True) ## <- metode sort yang di reverse alias di balik
print(makanan)

## .reverse()
makanan = ['mbg', 'indomie', 'ayam goreng', 'baso']
makanan.reverse()
print(makanan)
