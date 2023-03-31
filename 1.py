print("Ədədin bölənlərinin sayını tapan proqram başladılır...")
print("Bir ədəd daxil edin:")
s = 0
b = int(input())
for i in range(1, b + 1):
    if b % i == 0:
        s = s + 1
print(s)
