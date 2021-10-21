'''s = 'hello kedar call me on this number:9087635212'

for i in s.split(':'):
    if i.isdigit()== True:

        print("Final number is: ",i)
s1 = 'Abhinandan'
s2 = 'khade'
l1 =list(s1)
l2=list(s2)

for i in l1,l2:
    l3 = l1[::]+l2[::]


s = 'Shubham Pawar'
s1 =  s.replace(" ","")
print(s1[::2])
print(s1[1::2])

s = 'Shubham Pawar'
s1 =  list(s.replace(" ",""))
print(list(filter(lambda x:len(s)%2==2),s))

n = int(input("Enter no. of rows:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            print(1,end="")
        else:
            print(0,end="")

    print()

s = 'Anupama Rindhe'
s1 = s.split(" ")
l = list(s1)
sm = set(s)
sm1 = set(l[0])
sm2 = set(l[1])
l1 = {'A','a','e','i','o','u'}
print("Vowels in Anupama",sm1.intersection(l1))
print("Vowels in Rindhe",sm2.intersection(l1))
print("Actual vowels in both",sm.intersection(l1))

l = int(input('Enter lower range limit'))
u = int(input('Enter upper range limit'))
for i in range(l+1,u+1):
    if i%5==0:
        print(i)

s = 'ajuber'
l = list(s)
print(l)
k = int(input('Enter key:'))
for k in l:
    l1= str(ord(k))
    print(k)
    print(chr(ord(k)))









s = 'kedar pin:415311 and house is:5454'
l = list(s)
print(l)
for i in l:
    if i.isdigit()== True:
        print(i,end="")
print()



n = int(input("Enter the no."))
sq = n*n
cu = n*n*n
print('addition',n+sq+cu)


s = 'ahsdlfjgk15642378'
ls = list(s)
print(ls)
for i in ls:
    if i.isdigit()== True:
        d = list(i)
        print(d.sort())'''

