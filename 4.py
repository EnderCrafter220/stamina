print("Ədədin iki eyni cüt rəqəmlərdən ibarət olub-olmadığını tapan proqram başladılır...")
print("Bir ədəd daxil edin:")
a = int(input())
b = []
while a > 0:
    k = a % 10
    a = a // 10
    b.append(k)
if b.count(b[0]) == len(b):
    if b[0] % 2 == 0:
        print("Eyni cüt rəqəmlərdən ibarətdir")
    else:
        print("Eyni tək rəqəmlərdən ibarətdir")
else:
    print("Eyni rəqəmlərdən ibarət deyil")
