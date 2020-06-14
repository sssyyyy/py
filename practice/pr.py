#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#수치 식 계산
x=int(input("x값을 입력하세요:"))
y=3*x*x+5*x+3
print("y값은 ",y,"이다.")


# In[ ]:


#원 넓이 둘레
r=int(input("반지름을 입력하세요: "))
pi=3.14
print("원 둘레는 {0}이고 원 넓이는 {1}이다.".format(2*pi*r,r*r*pi))


# In[10]:


#최대값 구하기
str=input("Numbers? ")
nums=[]
for num in str.split():
    nums.append(int(num))#문자열을 숫자로 바꿔야함
nums.sort()
print("max =",max(nums),nums)#자료형이 여러가지 일땐 ,


# In[40]:


#함수 예제
def inc(a,b=1):
    return a+b

def list_add(l1,l2):
    return [a+b for a,b in zip(l1,l2)]
#print(list_add([1,2],[3,4]))
#list(zip([1,2],[3,4]))

def add(*ars):#인자 개수를 정하지 않고 받고 싶을때 사용 list로 취급
    return sum(ars)

def scaled_add(c,*ars):
    return [c*i for i in ars]
#scaled_add(2,1,2,3)

def super_add(*ars,**krs):#dic 예제
    return krs['two']*sum(ars)
super_add(1,6,3,one=1,two=2)


# In[43]:


#파일 import
from math import sin
sin(3.14)


# In[ ]:




