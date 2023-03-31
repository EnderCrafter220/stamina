print("Ədədi kvadrat kök altına salan proqram başladılır...")
print("Bir ədəd daxil edin:")
square = int(input())
i = 0
while True:
    if i * i == square:
        print(i)
        break
    i = i + 1
