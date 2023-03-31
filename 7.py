print("Ədədin bölənləri kvadratı cəmini tapan proqram başladılır...")
print("Bir ədəd daxil edin:")
alpha = int(input())
s = 0
for i in range(1, alpha + 1):
    if alpha % i == 0:
        s = s + 1 ** 2
print(s)
