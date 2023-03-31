print("Ədədlərin qarşılıqlı sadə olub-olmadığını tapan proqram başladılır...")
print("İki ədəd daxil edin:")
dundraff = int(input())
thestaff = int(input())
n = 0
c = []
for i in range(1, dundraff + 1):
    if dundraff % i == 0:
        c.append(i)
for k in range(1, thestaff + 1):
    if thestaff % k == 0:
        if k in c:
            n = n + 1
if n == 1:
    print("Bu ədədlər qarşılıqlı sadə ədədlərdir")
else:
    print("Bu ədədlər qarşılıqlı sadə ədədlər deyil")
