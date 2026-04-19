from difflib import Differ

def farqlarni_topish(matn1, matn2):
    differ = Differ()
    farqlar = differ.compare(matn1.splitlines(), matn2.splitlines())
    return farqlar

matn1 = "Bu matn birinchi"
matn2 = "Bu matn ikkinchi"

farqlar = farqlarni_topish(matn1, matn2)

for farq in farqlar:
    print(farq)
```

Kodni ishlatish uchun quyidagilarni amalga oshiring:

1. Matnlarni `matn1` va `matn2` deyalar.
2. `farqlarni_topish` funksiyasiga matnlarni kiritib, natijani `farqlar` deyalar.
3. `farqlar` deyalarining har bir elementini `print` funksiyasidan foydalanib chiqaring.
