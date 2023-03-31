print("Ədədin bölənlərinin ədədi ortasını tapan proqram başladılır...")
print("Bir ədəd daxil edin:")
defdfe = int(input())
s = 0
n = 0
for i in range(1, defdfe + 1):
    if defdfe % i == 0:
        s = s + i
        n = n + 1
print(s / n)
