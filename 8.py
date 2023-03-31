print("Ədədin bölənləri kubu cəmi tapan proqram başladılır...")
print("Bir ədəd daxil edin:")
bread = int(input())
s = 0
for i in range(1, bread + 1):
    if bread % i == 0:
        s = s + i ** 3
print(s)
