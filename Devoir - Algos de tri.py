def belong(n,t):
    i=0
    while i<len(t):
        if n==t[i]:
            return True
        i=i+1
    return False

def somme(t):
    res=t[0]
    for i in range(len(t)):
        res=res+t[i]
    return res

def PGint(t):
    res=t[0]
    for element in t:
        if element>res:
            res=element
    return res

def my_len(t):
    i=0
    for element in t:
        i=i+1
    return i


def map_double(t):
    res=[0]*len(t)
    for i in range (len(t)):
        res[i]=2*t[i]
    return res

def PPint(t,i,j):
    res=t[i]
    for indice in range(i+1,j+1):
        if t[indice]<res:
            res=t[indice]
    return res

def swap(t,i,j):
    keep=t[i]
    t[i]=t[j]
    t[j]=keep

def remove(t,i):
    res=[0]*(len(t)-1)
    for j in range (len(t)):
        if j<i:
            res[j]=t[j]
        if j>i:
            res[j-1]=t[j]
    return res

def my_selection_sort(t):
    res=[0]*len(t)
    for i in range(len(t)):
        j=index_of_the_smallest(t)
        res=t[j]
        remove(t,j)

def index_of_PP(t,i,j):
  i=0
  j=1
  for elements in t:
      if t[i]<t[j]:
          return i
      else:
          return j

def tri(t):
    for i in range(1, len(t)):
        T=t[i]
        j =i- 1
        while j>=0 and t[j]>T:
            t[j+1]=t[j]
            j=j-1
        t[j+1]= T
    return t

def test_tri():
    t=[2,5,8,12,10]
    return belong(5,t) and not belong(12,t)
    print("test_belong "+str(test_belong()))

def selection_sort_in_place(t):
    for i in range (len(t)):
        s=index_of_PP(t,i,len(t)-1)
        if s>i:
            swap(t,i,s)
    return None

def insert(t,i):
    for current_index in range(i-1,-1,-1):
        if t[current_index] > t[current_index+1]:
            swap(t,current_index,current_index+1)
        else:
            break

def insertion_sort_in_place(t):
    for i in range(1,len(t)):
        insert(t,i)






