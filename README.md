
# Xush kelibsiz
# RO'YXAT bo'yicha indekslash

Uy vazifalarini va testlarni avtomatik baholash
- ushbu repozitoriyani **fork** qiling
- vazifalarni yeching
- to‘g‘ri xabar bilan commit qiling

# Muammolar
## List01

  Sizga mevalar ro‘yxati beriladi. Ro‘yxat oxiriga x mevasini qo‘shing va qaytaring.

**Misol 1:**

```Python
Kiritish: fruits = ["apple", "banana"] x = 'kiwi'
Natija: ["apple", "banana", "kiwi"]

```

**Cheklovlar:**

  - 1 <= uzunlik(fruits) <= 10^5

## List02

  Sizga mevalar ro‘yxati beriladi. Ro‘yxatning i indeksiga x mevasini qo‘shing va uni qaytaring.

**Misol 1:**

```Python
Kiritish: fruits = ["apple", "banana"] x = 'kiwi' i=1
Natija: ["apple", "kiwi", "banana"]

```

**Cheklovlar:**

  - 1 <= uzunlik(fruits) <= 10^5
  - 0 <= i < uzunlik(fruits)

## List03

  Sizga fruits1 va fruits2 nomli ikki mevalar ro‘yxati beriladi. fruits2 ni fruits1 ga qo‘shing va natijani qaytaring.

**Misol 1:**

```Python
Kiritish: fruits1 = ["apple", "banana"] fruits2 = ["kiwi", "pear"]
Natija: ["apple", "banana", "kiwi", "pear"]

```

**Cheklovlar:**

  - 1 <= uzunlik(fruits1) <= 10^5
  - 1 <= uzunlik(fruits2) <= 10^5

## List04

  Sizga raqamlar ro‘yxati beriladi. i indeksdagi raqamni o‘chiring va qaytaring.

**Misol 1:**

```Python
Kiritish: numbers = [1, 2, 3, 4, 5] i = 2
Natija: 3

```

**Misol 2:**

```Python
Kiritish: numbers = [4, 7, 3, 2, 8] i = 4
Natija: 8

```

**Cheklovlar:**

  - 1 <= uzunlik(numbers) <= 10^5
  - 0 <= i < uzunlik(numbers)

## List05

  Sizga numbers1 va numbers2 nomli ikkita ro‘yxat beriladi. Birinchi ro‘yxatning oxirgi elementini o‘chirib, uni ikkinchi ro‘yxatning boshiga qo‘shing. Keyin birinchi ro‘yxatni ikkinchisiga birlashtirib, natijani qaytaring.

**Misol 1:**

```Python
Kiritish: numbers1 = [6, 8, 1] numbers2 = [3, 5, 7]
Natija: [6, 8, 1, 3, 5, 7]

```

**Cheklovlar:**

  - 1 <= uzunlik(numbers1) <= 10^5
  - 1 <= uzunlik(numbers2) <= 10^5

## List06

  Sizga Fruits nomli ro‘yxat beriladi, u kamida bitta “apple”ni o‘z ichiga oladi. Ro‘yxatda nechta “apple” borligini aniqlang va qaytaring.

**Misol 1:**

```Python
Kiritish: fruits = ["apple", "banana", "apple", "pear"]
Natija: 2

```

**Misol 2:**

```Python
Kiritish: fruits = ["apple", "banana", "apple", "apple", "apple"]
Natija: 4

```

**Cheklovlar:**

  - 1 <= uzunlik(fruits) <= 10^5

## List07

  Sizga nol va birlardan tashkil topgan ro‘yxat beriladi. Nechta nol borligini aniqlang va qaytaring.

**Misol 1:**

```Python
Kiritish: list1 = [1, 0, 1, 1, 0, 1, 1]
Natija: 2

```

**Misol 2:**

```Python
Kiritish: list1 = [0, 0, 0, 0, 0, 0, 0]
Natija: 7

```

**Cheklovlar:**

  - 1 <= uzunlik(list1) <= 10^5

## List08

  Sizga "fruits" nomli ro‘yxat beriladi, u uzunligi beshta va kamida bitta "apple"ni o‘z ichiga oladi. Ro‘yxatdan “apple”larni olib tashlang va ro‘yxatni qaytaring.

**Misol 1:**

```Python
Kiritish: fruits = ["apple", "banana", "apple", "pear", "apple"]
Natija: ["banana", "pear"]

```

**Misol 2:**

```Python
Kiritish: fruits = ["apple", "apple", "apple", "apple", "kiwi"]
Natija: ["kiwi"]

```

**Cheklovlar:**

  - uzunlik(fruits) == 5

## List09

  Sizga "fruits" nomli ro‘yxat beriladi, u uzunligi beshta va kamida bitta "apple"ni o‘z ichiga oladi. Nechta "apple" borligini aniqlang va ularning indekslarini ro‘yxat shaklida qaytaring.

**Misol 1:**

```Python
Kiritish: fruits = ["apple", "banana", "apple", "pear", "apple"]
Natija: [3, 0, 2, 4]

```

**Misol 2:**

```Python
Kiritish: fruits = ["apple", "apple", "apple", "apple", "kiwi"]
Natija: [4, 0, 1, 2, 3]

```

**Cheklovlar:**

  - uzunlik(fruits) == 5

## List10

  Sizga nol va birlardan tashkil topgan ro‘yxat beriladi. Undagi birlar va nollar sonini hisoblang va ro‘yxat ko‘rinishida qaytaring.

**Misol 1:**

```Python
Kiritish: list1 = [1, 0, 0, 0, 1, 0, 1, 0]
Natija: [3, 5]

```

**Misol 2:**

```Python
Kiritish: list1 = [0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1]
Natija: [4, 7]

```

**Cheklovlar:**

  - 1 <= uzunlik(list1) <= 10^5

# Ogohlantirish
- boshqa yechimlarni yoki har qanday yechimni nusxalamang
- izohlarni o‘chirmang
