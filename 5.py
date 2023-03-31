print("Ədədin natural bölənlərini tapan proqram başladılır...")
print("Bir ədəd daxil edin:")
beta = int(input())
for i in range(1, beta + 1):
    if beta % i == 0:
        print(i)
