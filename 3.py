print("Ədədin bütün rəqəmlərinin eyni olub-olmadığını tapan proqram başladılır...")
print("Bir ədəd daxil edin:")
preattach = int(input())
b = []
while preattach > 0:
    k = preattach % 10
    preattach = preattach // 10
    b.append(k)
if b.count(b[0]) == len(b):
    print("Ədədin bütün rəqəmləri eynidir")
else:
    print("Ədədin rəqəmlərində fərqlilik var")
