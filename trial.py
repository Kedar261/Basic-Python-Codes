'''# Problem 1
i/p s = 'abjhafkajhrfk6849684354'
o/p = ['a', 'a', 'a', 'b', 'f', 'f', 'h', 'h', 'j', 'j', 'k', 'k', 'r', '3', '4', '4', '4', '5', '6', '6', '8', '8', '9']
l = []
l1 = []
for i in s:
    if i.isdigit() == True:
        l.append(i)
    else:
        l1.append(i)
l.sort()
l1.sort()
#l1 = "".join(l)
l1.extend(l)
l3 = "".join(l1)
print(l1)







# # Problem 2 tuple f no.s having sum 10 =(9,1),(5,5)
#n = 0
#sum = 10-n
d = {}
for i in range(1,11):
    j = 10-i
    d[i]= j
l = list(d.items())
t = tuple(l)
print(t)



# Problem 3 Type the string in uppercase without using built in uppecase
s = 'alkjafsfdg'
Way of solution 1:
l1 = []
l2 = []
for i in s:
    l1.append(ord(i))
print(l1)
for i in l1:
    l2.append(chr(i-32))
print(l2)

Way of solution 2:
s = 'kedar'
for i in s:
    j = chr(ord(i)-32)
    print(j,end="")





#Problem 4 print first 50 no. without using range
#Way of solution 1
n = 50
i = 0
l = []
while i<=n-1:
    i+= 1
    l.append(i)
    print(i,end=",")
print()
print(l)


#Way of solution 2
n = 5
i = 1
while True:
    print(i)
    i += 1
    if i == n:
        break


#Problem 5
# I/p: t = (('300','3000'),('400','4000'))
# O/p:[300, 3000, 400, 4000]
t = (('300','3000'),('400','4000'))
l = []
for i in t:
    for j in i:
        l.append(int(j))
print(l)

#Problem 6
s = 'One Two Three'
o/p = 'Three Two One


#With for loop
for i in reversed(s.split()):
    print(i,end=" ")
print()

#By indexing (without for loop)
s = 'One Two Three'
s1 = s.split()
print(s1[2],s1[1],s1[0])

def counter():
    i=1
    while(i<=10):
         yield i
         i+=1
    print(i)
c = counter()
print(c)

for i in counter():
         print(i)



s = ' Python is Simple Language Simple Language'
s1 = set(s.split())
print(str(s1))'''


s = ' Python is simple Language Simple Language'
l = list(s.split())
ap = []
for i in l:
    a = len(s.split())
    ap.append(a)
    print(a)




