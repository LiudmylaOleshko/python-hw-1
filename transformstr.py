# Ініцілізовано функцію, напишіть в тілі функції логіку яка
# перетворить вхідну строчку за певною логікою.

# Функція приймає на вхід будь яку строчку і виводить в консоль за допомогою функції print()
#  оновлену версію цієї строчки.
# Якщо довжина строчки більша ніж 5 символів -> Потрібно вивести лише перші 5 символів та в кінці додати три точки (...).
# Якщо перша літера строчки U або u (регістр не важливий) -> Вивести всю строчку в Upper Case (верхній регістр)
# Якщо перша літера строчки L або l (регістр не важливий) -> Вивести всю строчку в Lower Case (нижній регістр)
# Якщо жодна умова вище не підходить - вивести строку без змін.
# Декілька умов можуть пересікатись!
# Можна додавати свої тести за прикладом. Потрібно врахувати обробку можливих помилок.

# Наприклад:
#   transformStr('Testing string') - > 'Testi...' (довжина більше 5 символів)
#   transformStr('Lux') - > 'lux' (Починается на L)
#   transformStr('up') - > 'UP' (Починается на U)
#   transformStr('Luxery') - > 'luxer...' (Починается на L + довжина більше 5 символів)

a = input("Enter string :")
# def transformStr(str):
print(a[:5], " ...")

if a[0] == "u":
    print(a.upper())
elif a[0] == "U":
    print(a.upper())
elif a[0] == "l":
    print(a.lower())
elif a[0] == "L":
    print(a.lower())
else:
    print(a)
