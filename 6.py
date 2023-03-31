print("Ədədin sadə vəya mürəkkəb olduğunu hesablayan proqram başladılır...")
print("Bir ədəd daxil edin:")
alice = int(input())
n = 0
for i in range(1, alice + 1):
    if alice % i == 0:
        n = n + 1
if n > 2:
    print("Bu mürəkkəb ədəddir")
else:
    print("Bu mürəkkəb ədəd deyil")
