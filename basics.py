'''# replace the characters in string
#Example 1
s = 'Python is simple'
s1 = s.replace('i','_').replace('s','i').replace('_','s')
print(s1)
r = s.translate(str.maketrans({'i':'s','s':'i'}))
print(r)
#Example 2
s = '0100111010101012222'
s1 = s.replace('2','_').replace('1','2').replace('0','1').replace('_','0')
print(s1)

# Slicing
s = 'Python is Simple'

print(s[:7])
print(s[1:7:2])
print(s[-1::-1])
print(s[:1:])
# to print length
print(len(s))
#to print word having even length
for i in s.split():
    if len(i)%2==0:
        print(i)
s2=s.split()
n=list(filter(lambda x:len(x)%2==0,s2))
print(n)
s = range(100)
no = list(filter(lambda x:x%2==0,s))
print(no)


m =(x for x in s2 if len(x)%2==0)
print(".......",tuple(m))
num = list(filter(lambda x:len(x)%2==0,s2))
print("...",num)




l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
l[:3] = [1,2,3]
print(l)









'''# tuple f no.s having sum 10 =(9,1),(5,5)
#n = 0
#sum = 10-n
d = {}
for i in range(1,11):
    j = 10-i
    d[i]= j
l = list(d.items())
t = tuple(l)
print(t)




'''s = 'alkjafsfdg'
l1 = []
l2 = []
for i in s:
    l1.append(ord(i))
print(l1)
for i in l1:
    l2.append(chr(i-32))
print(l2)







s = 'kedar'
for i in s:
    j = chr(ord(i)-32)
    print(j,end="")'''


#s = [1,2,3,4,5,...,50]
'''n = 50
i = 0
l = []
while i<=n-1:
    i+= 1
    l.append(i)
    print(i,end=",")
print()
print(l)


n = 5
i = 1
while True:
    print(i)
    i += 1
    if i == n:
        break


t = (('300','3000'),('400','4000'))
#l1 = list(t[0])
#l2 = list(t[1])

#print(l1,l2)
#l = list(t)
#print(l)

l = []
for i in t:
    for j in i:
        l.append(int(j))
print(l)


s = 'One Two Three'
o/p = 'Three Two One


#With for loop
for i in reversed(s.split()):
    print(i,end=" ")
print()

#By indexing (without for loop)
s = 'One Two Three'
s1 = s.split()
print(s1[2],s1[1],s1[0])'''


