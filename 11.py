print("Ədədi kub kök altına salan proqram başladılır...")
print("Bir ədəd daxil edin:")
cubius = int(input())
i = 0
while True:
    if i * i * i == cubius:
        print(i)
        break
    i = i + 1
