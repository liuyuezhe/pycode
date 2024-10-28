"""
s,idx="bit",0
while idx<len(s):
    print("循环进行中："+s[idx])
    idx+=1
else:
    s="循环正常结束"
print(s)
"""
"""
for s in "bit":
    for i in range(10):
        print(s,end="")
        if s=="i":
            break
"""
"""
for s in "python":
    if s=="t":
        continue
    print(s,end="")
"""
"""
for s in "python":
    if s=="t":
        break
    print(s,end="")

"""
"""
for s in "python":
    if s=="t":
        continue
    print(s,end="")
else:
    print("正常退出")
"""
"""
for s in "python":
    if s=="t":
        break
    print(s,end="")
else:
    print("正常退出")
"""
"""
ls=list(range(10))
print(ls)
"""
"""
try:
    num=eval(input("请输入一个整数"))
    print(num**2)
except:
    print("输入错误，请输入一个整数")

"""
"""
try:
    num=eval(input("请输入一个整数"))
    print(num**2)
except:
    print("输入错误，请输入一个整数")
"""
"""
def happy():
    print("happy birthday to u")
    print("happy birthday to u")
def happyb(name):
    print("happy birthday,dear {}".format(name))
happy()
happyb("abc")
happy()
"""
"""
f=lambda x,y:x+y
print(f(4,9))
"""
"""
def hl(a,b,c):
    from math import sqrt
    p=(a+b+c)/2
    s=sqrt(p*(p-a)*(p-b)*(p-c))
    return(s)
a=eval(input("请输入第一条边长"))
b=eval(input("请输入第二条边长"))
c=eval(input("请输入第三条边长"))
s=hl(a,b,c)
print("三角形面积是{:.2f}".format(s))
"""
"""
month=input("请输入月份：")
if month in ['1','2','7','8','9']:
    num=eval(input("请输入房间数："))
    if num>20:
        print("优惠为20%")
    else:
       print("优惠为5%")
else:
    num=eval(input("请输入房间数："))
    if num>15:
        print("优惠为30%")
    else:
       print("优惠为10%")
"""
"""
def line(n):
    for l in range(n):
        print("+ - - - - ",end='')
    print('+')
def row(n):
    for i in range(4):
        for l in range(n):
            print("〡        ",end='')
        print('〡')
m=eval(input("请输入行列数"))
for i in range(m):
       line(m)
       row(m)
line(m)
"""
"""
def isodd(n):
    m=n%2;
    if(m==1):
        return(True)
    else:
        return(False)
k=eval(input("请输入一个整数"))
print(isodd(k))
"""
"""
def isnum(n):
    if type(n) in [int,float,complex]:
       return(True)
    else:
        return(False)
k=eval(input("请输入"))
print(isnum(k))
"""
"""
def multi(*a):
    k=1
    for i in a:
        k=i*k
    return k
print(multi(5,6,7))
"""
"""
def isprime(n):
    try:
        k=0
        for i in range(n):
            b=n%(i+1)
            if b==0:
                k=k+1
        if k==2:
            return(True)
        else:
            return(False)
    except NameError:
        print("输入错误")
m=eval(input("请输入:"))
print(isprime(m))
"""
"""
from datetime import datetime as dt
lyz = dt(2003,12,11,20,36,0)

print(lyz.strftime("%Y-%m-%d %H:%M:%S"))
print(lyz.strftime("%Y,%B,%d %H:%M:%S"))
print(lyz.strftime("%Y-%b-%d %H:%M:%S"))
print(lyz.strftime("%Y年%m月%d日 %H时%M分%S秒"))
print(lyz.strftime("%Y-%m-%d %I%p"))
print(lyz.strftime("%Y年%m月%d日 %A"))
print(lyz.strftime("%Y年%m月%d日 %a"))
"""
"""
def f(n):
    if n==0:
        return 1
    else:
        return n*f(n-1)
num=eval(input("请输入一个整数"))
print(f(abs(int(num))))
"""
"""
def r(s):
    if s=='':
        return s
    else:
        return r(s[1:])+s[0]
st=input("请输入一个字符串")
print(r(st))
"""
"""
print(all([1,2,3,4,5]))
print(all([1,2,3,0,5]))
"""
"""
print(id('123abc'))
"""
"""
ls=[2,9,3,6,1]
ls1=list(reversed(ls))
print(ls1)
ls2=sorted(ls)
print(ls2)
ls3=sorted(ls,reverse=True)
print(ls3)
"""
"""
print([1,2,3,4,5,6,7,8,9,0][-5])
"""
"""
print( 'b' in 'ajkhnewjcuwui')
"""
"""
print([1,2,3,4,5,6,7,8,9,0][::-1])
"""
"""
print('ajkhnewkjcukwuki'.index('k'))
"""
"""
print('ajkhnewkjcukwuki'.count('k'))
"""
'''
creature='cat','dog','tiger','human'
print(creature)
color='red','green','blue',creature
print(color[-1][-1])
'''
'''
def f(x):
      return x,x*3
print(f(6))
'''
'''
import math
for x,y in ((1,0),(3,4),(5,12)):
    print(math.hypot(x,y))
'''
'''
print(hash('asd'))
'''
'''
print(hash((1,2,3)))
'''
'''
s={1,2,3,1,2,3}
print(s)
'''
'''
a=set('apple')
print(a)

'''
'''
a=list(('apple','asd','sdf'))
print(a)
'''
'''
st1=set(range(10))
st2=set(range(5,20))
print(st1)
print(st2)
print(st1&st2)
print(st1-st2)
print(st1|st2)
print(st1^st2)
'''
'''
import turtle,datetime


def drawline(draw):

    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)



def drawdigit(d):

    drawline(True) if d in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if d in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if d in [0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if d in [0,2,6,8] else drawline(False)
    turtle.left(90)
    drawline(True) if d in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if d in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if d in [0,1,2,3,4,7,8,9] else drawline(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)


def drawdate(date):

    for i in date:
        drawdigit(eval(i))


def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawdate("20031211")
    turtle.hideturtle()

main()
'''
'''
import turtle,datetime


def drawgap():

    turtle.penup()
    turtle.fd(5)


def drawline(draw):
    drawgap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawgap()
    turtle.right(90)


def drawdigit(d):

    drawline(True) if d in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if d in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if d in [0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if d in [0,2,6,8] else drawline(False)
    turtle.left(90)
    drawline(True) if d in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if d in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if d in [0,1,2,3,4,7,8,9] else drawline(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)


def drawdate(date):

   turtle.pencolor("red")
   for i in date:
        if i=="-":
           turtle.fd(40)
           turtle.pencolor("blue")
           turtle.write("年",font=("Arial",30,"normal"))
           turtle.fd(80)
           turtle.pencolor("red")
        elif i=="=":
            turtle.fd(40)
            turtle.pencolor("blue")
            turtle.write("月",font=("Arial",30,"normal"))
            turtle.fd(80)
            turtle.pencolor("red")
        elif i=="+":
           turtle.fd(40)
           turtle.pencolor("blue")
           turtle.write("日",font=("Arial",30,"normal"))
           turtle.fd(80)
           turtle.pencolor("red")
        else:
            drawdigit(eval(i))


def main():
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-370)
    turtle.pensize(5)
    drawdate(datetime.datetime.now().strftime('%Y-%m=%d+'))
    turtle.hideturtle()

main()
'''
"""
a=('python','bit',123,'good',123)
print(set(a))
"""
'''
k=0
s=0
for i in range(100):
    k=1/((i+1)*(i+2))
    s=s+k
print(s)
'''
"""
s=1
for i in range(n+1):
    k=(i+1)*(i+1)
    s=s*k
    print(i,s)
    if s>100000:
        break
print(n)
"""
"""
while
(x>=100)&(x<=1000)
x%4==2
x%5==3
x%6==0
print(x)
"""
"""
n=1
s=0
while(s<=100000):
    s=s+n*n
    if(s>100000):
        break
    print(s,n)
    n=n+1
"""
"""
x=100
while(x>=100)&(x<=1000):
    if((x%4==2)&(x%5==3)&(x%6==0)):
        print(x)
        x=x+1
    else:
        x=x+1
"""
"""
st={4,6,3,2,"aa","asss",-199}
print(st)
print(st.discard(6))
print(st.remove(6))
"""
"""
ls=[123,"fwsf",[12,"dd"],123]
print(ls[2][1][1])
print(list((234,5464,"sdvd",123)))
print(list("中国是一个伟大的国家"))
"""
"""
x=10
y=x
z=y
print(id(x))
print(id(y))
print(id(z))
"""
"""
ls=[123,"fwsf",[12,"dd"],123]
lt=ls
lt[0]=6
print(ls)
"""
"""
ls=[1,2,3,4,5,6,7,8,9]
print(len(ls[2:]))
lt=['abc']
ls+=lt
print(ls.extend(lt))
"""
"""
ls=[1,2,3,4,5,6,7,8,9]
for i in ls:
    print(i,end="    ")
"""
"""
ls=[1,2,3,4,5,6,7,8,9]
lt=ls
lt.clear()
print(ls)
print(lt)
"""
"""
from math import sqrt
def getnum():
    nums=[]
    sn=input('请输入一个数值')
    while sn!='':
        nums.append(eval(sn))
        sn=input('请输入一个数值')
    return nums
def mean(numbers):
    s=0
    for i in numbers:
        s+=i
    return s/len(numbers)
def dev(numbers,m):
    d=0
    for i in numbers:
        d+=(i-m)**2
    return sqrt(d/(len(numbers)-1))
def median(numbers):
    sn=sorted(numbers)
    size=len(sn)
    if size%2==0:
        med=(sn[size//2-1]+sn[size//2])/2
    else:
        med=sn[size//2]
    return med
def maxs(numbers):
    max=sorted(numbers)[-1]
    return(max)
def mins(numbers):
    min=sorted(numbers)[0]
    return(min)
n=getnum()
m=mean(n)
print("平均值:{:.2f},标准差:{:.2f},中位数:{},最大值:{},最小值:{}".format(m,dev(n,m),median(n),maxs(n),mins(n)))
"""
"""
import jieba
print(jieba.lcut("中国是一个伟大的国家"))
"""
"""
import random
ls1=list("qwertyuiopasdfghjklzxcvbnm")
ls2=list("QWERTYUIOPASDFGHJKLZXCVBNM")
ls=[0,1,2,3,4,5,6,7,8,9]+ls1+ls2
print("10个八位密码为：")
for j in range(10):
    for i in range(8):
        n=random.randint(0,61)
        print(ls[n],end="")
    print(end="   ")
"""
"""
def re(ls):
    if type(ls)==list:
        a=len(ls)
        ls1=ls
        ls=set(ls)
        b=len(ls)
        if a==b:
            print("True")
        else:
            print("False")
            for i in ls:
                if ls1.count(i)==1:
                    continue
                else:
                    print(i)
    else:
        print("输入错误")
ls=[1,2,3,4,5,6,1,9,6,5,7,5,2]
re(ls)
"""
"""
def kkk(str):
    str1=set(str)
    for i in str1:
        a=str.count(i)
        print("字符:",i,"次数:",a)
str=input("请输入一串字符")
kkk(str)
"""
"""
import operator
n=input("请输入一串字符:")
dict={}
for i in n:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
d=sorted(dict.items(),key=operator.itemgetter(1),reverse=True)
print("根value值降序排序:",d)

"""
"""
import jieba
excludes={"什么","一个","我们","你们","如今","说道","知道","姑娘","起来","这里"}
txt = open("C:/Users/84478/Desktop/作业需要/python作业/素材/红楼梦全集.txt", "r", encoding='utf-8').read()
words  = jieba.lcut(txt)    
counts = {}    
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0) + 1
items = list(counts.items())    
items.sort(key=lambda x:x[1], reverse=True) 
for i in range(15):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))
"""
"""
#CalThreeKingdomsV2.py
import jieba
excludes = {"什么","一个","我们","你们","如今","说道","知道","姑娘","起来","这里","出来","众人","那里","自己","一面","只见","两个","没有",
            "怎么","不是","不知","这个","听见","这样","进来","咱们","就是","东西","告诉","袭人","回来","只是","大家","只得"}  
txt = open("C:/Users/84478/Desktop/作业需要/python作业/素材/红楼梦全集.txt", "r", encoding='utf-8').read()
words  = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "王夫人" or word == "凤姐"or word == "太太":  
        rword = "王熙凤"
    elif word == "老太太" or word == "贾母":  
        rword = "贾母"
    elif word == "奶奶":  
        rword = "尤氏"
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
for i in range(10):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))
"""
"""
from math import sqrt
ls=[]
n=0
while n<=100:
    n=eval(input("请输入考试成绩"))
    if n>100:
        break
    ls.append(n)
m=len(ls)
sum=0
for i in ls:
    sum=sum+i
avalue=sum/m
print("均值为",avalue)
sdev=0
for i in ls:
    sdev=sdev+(i-avalue)**2
sq=sqrt(sdev/m)
print("标准差为",round(sq,2))
snum=sorted(ls)
if len(snum)%2==0:
    med=(snum[len(snum)//2-1]+snum[len(snum)//2])/2
else:
    med=snum[len(snum)//2]
print("中位数为",med)
maxa=snum[len(snum)-1]
mina=snum[0]
print("最大值",maxa)
print("最小值",mina)
"""
"""
import jieba
print(jieba.lcut_for_search('中华人民共和国是一个伟大的国家'))
"""
"""
counts={}
txt='''My school life is very colorful.I have many lovely
classmates and teachers.My friend XX is always with me.
We study and play together.We happy every day.After class my
classmates always ask questions each other.And I would love ask
question to my classmates and teachers,they are very helpful.I
most like my English teacher,she is funny and kindful.She always
simle,which makes me very comfortable.I like PE class very much.
In PE class,we can play so many balls together.That is my school
life,my happy and wonderful school life.'''
for ch in '.,\n':
        txt=txt.replace(ch," ")
txt=txt.lower()
txt=txt.split()
for word in txt:
    counts[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
print(items)
"""
'''
ls=['one',1,4,-5,'two',9,3,'three']
ls=ls[::-1]
for l in ls:
    print(l,end=' ')
'''
'''
import math
a=(input("输入数字"))
n=eval(input("重复次数"))
sum=0
for i in range(n):
    m=a*(i+1)
    print(m)
    sum=sum+int(m)
print(sum)
'''
'''

a=[[1,2,3],[4,5,6],[7,8,9]]
b=[3,6,9]
sum=0
for i in range(3):
    for j in range(3):
        sum=sum+b[j]*a[i][j]
print(sum)
'''
'''
import jieba
txt=''''''My school life is very colorful.I have many lovely classmates and teachers.
My friend XX is always with me.We study and play together.We happy every day.After 
class my classmates always ask questions each other.And I would love ask question to
my classmates and teachers,they are very helpful.I most like my English 
teacher,she is funny and kindful.She always simle,which makes me very comfortable.I
like PE class very much.In PE class,we can play so many balls together.
That is my school life,my happy and wonderful school life''''''
txt=txt.lower()
for ch in ',.':
    txt=txt.replace(ch," ")
words=txt.split()
counts={}
for word in words:
    counts[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))
'''
'''
import jieba
txt=''''''云南大学始建于1922年，1923年正式开学，时为私立东陆大学，
1934年更名为省立云南大学，1938年改为国立云南大学，是我国西部边疆最早建立的综
合性大学之一。1937年，著名数学家、教育家熊庆来出任校长，一大批著名学者受
聘到校任教，奠定了学校较高的发展基础和深厚的学术底蕴，开创了云大办学历史上
的第一个辉煌时期。20世纪40年代，云南大学已发展成为一所包括文、法、理、工、农
、医等学科在内，规模较大，在国际上有影响的中国著名大学之一。1946年，《不列颠
百科全书》将云南大学列为中国15所在世界最具影响的大学之一。''''''
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)==1:
        continue
    else:
        counts[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(15):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))
'''
'''
import jieba
txt = open("三国演义.txt","r",encoding='utf-8').read()
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)==1:
        continue
    else:
        counts[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
for i in range(15):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))
'''
'''
txt = open("hamlet.txt", "r").read()
txt = txt.lower()
for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
    txt = txt.replace(ch, " ")  
words  = txt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
for i in range(10):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))
'''
'''
import turtle
turtle.pensize(4)
turtle.pendown()
turtle.seth(30)
for i in range(2):
    turtle.fd(100)
    turtle.right(60)
turtle.right(60)
for i in range(2):
    turtle.fd(100)
    turtle.right(60)
'''
'''
ls=[]
s=0
for i in range(4):
    x=eval(input("请输入评委打分："))
    ls.append(x)
print(ls)
ls.sort()
min=ls.pop(0)
max=ls.pop(-1)
s=sum(ls)
pinjun=s/2
print("平均值:{},最大值:{},最小值:{}".format(pinjun,max,min))
'''
'''
ls=[['zhangsan',98,75,82,69,93],['lisi',67,90,74,83,86],['wangwu',70,62,97,67,81]]
s=0
for i in range(3):
    name=ls[i].pop(0)
    s=sum(ls[i])
    print(name,s,s/5)
'''
'''
studs=[{'number':'103','chinese':'90','math':'95','english':'92'},{'number':'101','chinese':'80','math':'85','english':'82'},{'number':'102','chinese':'70','math':'75','english':'72'}]
doc={}
ls=[]
a=0
for i in range(3):
    a=list(studs[i].values())
    doc.update({a[0]: a[1:4]})
print(doc)
for i in sorted (doc) : 
    print(i, doc[i])
'''
'''
ls = ["综合", "理工", "综合", "综合", "综合", "综合", "综合", "综合", "综合", "综合",\
      "师范", "理工", "综合", "理工", "综合", "综合", "综合", "综合", "综合","理工",\
      "理工", "理工", "理工", "师范", "综合", "农林", "理工", "综合", "理工", "理工", \
      "理工", "综合", "理工", "综合", "综合", "理工", "农林", "民族", "军事"]
ll=set(ls)
ll=list(ll)
doc={}
for i in ll:
    k=0
    for j in ls:
        if i==j:
            k=k+1
        doc.update({i:k})
print(doc)
'''
'''
ls=[('苹果','iPhone 12 Pro'),('海思麒麟','华为Mate40 Pro'),('高通骁龙','vivo NEX 3S'),\
    ('高通骁龙','三星Galaxy Z Fold2'),('海思麒麟','华为Mate30'),\
    ('高通骁龙','OPPO Reno Ace'),('海思麒麟','华为nova 8 Pro'),('高通骁龙','OPPO Reno'),\
    ('高通骁龙','魅族18'),('联发科','OPPO Reno Z'),('三星Exynos','三星GALAXY S7'),\
    ('联发科','OPPO R17'),('三星Exynos','三星Galaxy S10'),('海思麒麟','荣耀30S'),\
    ('海思麒麟','荣耀10'),('三星Exynos','魅族PRO 5'),('三星Exynos','三星GALAXY Note 4'),\
    ('苹果','iPhone XS'),('苹果','iPhone 11'),('联发科','OPPO A9')]
name=[]
doc={}
doc1={}
ll=[]
num=0
for i in ls:
    name.append(i[0])
name=set(name)
name=list(name)
for i in name:
    doc.update({i:""})
    doc1.update({i:""})
for i in name:
    for j in ls:
        if j[0]==i:
            ll.append(j[1])
            num=num+1
    doc1[i]=num
    doc[i]=ll
    ll=[]
    num=0
print(doc)
print(doc1)
doc1= sorted(doc1.items(),key=lambda x:x[1],reverse = True)
print(doc1)
'''
'''
i=1
fi=open("data.txt")
for line in fi:
    line=line.split(',')
    s=0
    n=len(line)
    for course in line:
        items=course.split(':')
        s+=eval(items[1])
    print("第{}个同学的总分是：{},平均分是：{:.2f}".format(i,s,s/n))
    i+=1
fi.close()
'''
'''
ls=[1,1,1,1,1,1,1,1,1,1]
t=1
sum=0
for i in range(len(ls)):
    for j in range(i+1):
        t=(j+1)*t
    ls[i]=t
    t=1
print(ls)
for i in range(len(ls)):
    sum=sum+ls[i]
print(sum)
'''
'''
import random,turtle

def drawLine(draw):
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    turtle.right (90)

def drawChar(char):
    drawLine(True) if char in "2345689AbdEF"else drawLine(False)
    drawLine(True) if char in "013456789Abd"else drawLine(False)
    drawLine(True) if char in "0235689bCdE"else drawLine(False)
    drawLine(True) if char in "0268AbCdEF"else drawLine(False)
    turtle.left(90)
    drawLine(True) if char in "045689AbCEF" else drawLine(False)
    drawLine(True) if char in "02356789ACEF" else drawLine(False)
    drawLine(True) if char in "01234789Ad"else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)

def drawHex (rh):
    for i in rh:
        drawChar(i)#本行可以替换为drawChar(eval(i))吗?为什么?
def randHex():
    s="0123456789AbCdEF"
    rh=""
    for i in range(4):
        rh+=s[random.randint(0, 15)]
    return rh
turtle.setup(400,350,200,200)
turtle.penup()
turtle.fd(-150)
turtle. pensize(5)
drawHex(randHex())
turtle.hideturtle()
'''
'''
import jieba



txt =''''''深度学习的概念源于人工神经网络的研究。含多隐层的多层感知器就是一种深度学习结构。
深度学习通过组合低层特征形成更加抽象的高层表示属性类别或特征，以发现数据的分布式特征表示。
深度学习是机器学习的一个分支，它使用 算法对数据中的高级抽象进行建模。这些方法 基于人工神经网络拓扑结构
，可以扩展到更大 的数据集。深度学习“是包含多级非线性变换的层级机器学习方法”。
深度学习通过组 合低层特征形成更加抽象的高层表示、属性类别或特征，给出数据的分层特征表示。
深度 学习“善于从原始输入数据中挖掘越来越抽象 的特征表示，而这些表示具有良好的泛化能 力”。
阿尔诺·舒巴赫从哲学的视角来理解 深度学习，认为其功能的实现是通过学习获得 的而非基于规则计算，
因此无法获得深度学习 网络如何处理输入的可理解或可形式化的知识，而需要具有人类信任的判断特征，
将深度学 习概念化为“一种它可以‘不依赖解释和说明’ 的判断机器”。笔者根据深度学习的功能和 特点将其定义为:
是一种可以在数据中通过自 我训练，不断提取特征，进而归纳形成抽象的智 能机器模型。
目前深度学习主要分为三大类: 卷积神经网络、反馈深度网络以及双向深度网络。
其中卷积神经网络主要采取一种自底向上的经验 学习训练方法，
而反馈深度网络主要采取一种 自顶向下的与卷积神经网络逆思路的先验学习方法，双向深度网络则是前两种训练方法的结合。
卷积神经网络通常由输入层、若干个交替 设置的卷积层和池化层、全连接层以及输出层 组成。
其中深度学习的特征提取能力主要来自 于卷积层和池化层，相对应视皮层的简单细胞 和复杂细胞的感受野机制。
而学习的关键在于 调整适应数据的网络链路中的权值，使数据能 够在特定的网络结构中经过相应地适应算法得
到较好的训练效果。但由于训练规则不被事先预定，其输出也不知如何获得，因而具有不可解 释性。
引起深度学习不透明性问题的原因是多方面的。曼努埃尔卡拉班塔斯对“意图隐藏”“技术文盲”“认知错配”
三种形式的不透明 性进行认识论分析，指出“认知错配”是最令人 担忧的。事实正是如此，这里涉及是人为还是
技术本身的问题。由于“认知错配”的根本原 因来自于机器本身的技术复杂性，因此最容易 失控; 并且通常来说，
深度学习的网络结构越是 复杂，就表现得越是智能，与之相应地也更加难 以理解和解释。因此在解决“黑盒问题”时，
又 面临着如何解决深度学习的不透明性与其智能 性之间的矛盾的问题。目前许多学者已经提出一些深度学习不
透明性的解决方法，抛开人为 原因，一般分为分解类、折衷类和数学类。但由 于算法的特殊性，如: 极大似然估计算法，
决定 了其难以转化为可理解的规则。 由于深度学习主要是模仿人类学习，其对 数据的处理模式主要是模仿人脑对
信息的处理 模式，因此，从人类认识论角度对深度学习的学 习过程进行分析，是理解深度学习的认识论问题
的一种有效路径。
''''''
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)==1:
        continue
    else:
        rword=word
    counts[rword]=counts.get(rword,0) + 1



items=list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
for i in range(10):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))
'''
'''
from sympy import*
a1=eval(input("请输入总成本函数x二次项的系数"))
b1=eval(input("请输入总成本函数x一次项的系数"))
c1=eval(input("请输入总成本函数常数项的系数"))
a2=eval(input("请输入产品单价"))
print("利润函数为y={}x-({}x^2+{}x+{})".format(a2,a1,b1,c1))
x=Symbol('x')
fx=a2*x-(a1*x*x+b1*x+c1)#利润函数
fx_=diff(fx,x)#利润函数的导数，求最值
x1=int(solve(fx_,x)[0])#x1为求出的最值
fx1=a2*x1-(a1*x1*x1+b1*x1+c1)#x1时的利润
gx=a1*x*x+b1*x+c1#成本函数
gx_=diff(gx,x)#边际成本函数
gx_1=gx_.evalf(subs={x:x1})#边际成本
print("当x={}时，利润最大为{},边际成本为{:.2f}".format(x1,fx1,gx_1))
'''
'''
from sympy import*
t=Symbol('t')
ft=2*t*t*t-5*t*t
ftd=diff(ft,t)
ftdd=diff(ftd,t)
ftdd1=ftdd.evalf(subs={t:2})
print("加速度为：{:.2f}".format(ftdd1))
'''
'''
from sympy import*
t=Symbol('t')
ht=-4.9*t*t+6*t+10#相对水面高度函数
ht_=diff(ht,t)#速度函数
print("相对水面高度函数为",ht,"速度函数为",ht_)
ht_1=abs(ht_.evalf(subs={t:2}))#t=2时的速度
print("在2s时运动员的下降速度为{:.2f}".format(ht_1))
t1=float(solve(ht_,t)[0])#速度为0时的时间
print("运动员跃起后,t={:.2f}s时上升速度为0".format(t1))
t2=float(solve(ht,t)[0])#落水时间
ht_2=abs(ht_.evalf(subs={t:t2}))#落水速度
print("运动员入水刹那速度为{:.2f}".format(ht_2))
'''
'''
from sympy import*
x=Symbol('x')
fx=(400/x)*4+4*x#费用函数
fx_=diff(fx,x)
x1=abs(int(solve(fx_,x)[0]))#每次购买的吨数
fx1=abs(fx.evalf(subs={x:x1}))#总费用
print("每次购买{}吨时，总费用最低为{:.1f}".format(x1,fx1))


from sympy import *

q = Symbol('q')
L = (25 - 0.125 * q) * q - (100 + 4 * q)  # 利润函数
L_ = diff(L, q)
q1 = int(solve(L_, q)[0])  # 所求产量
L1 = L.evalf(subs={q: q1})  # 利润最大值
print("产量为{}时，利润最大为{:.2f}".format(q1, L1))
'''



















