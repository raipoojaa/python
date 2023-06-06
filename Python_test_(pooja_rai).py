#!/usr/bin/env python
# coding: utf-8

# In[2]:


def do_arithmetic(x,y,op):
  
    x=input('Enter a number')
    y=input('Enter a number')
    op=input('Enter operation')

    if op == '+' or 'add':
      sum = float(x)+float(y)
      print('Sum of x and y is:',sum)

    if op == '-' or 'subtract':
      sub = float(x)- float(y)
      print('Subtraction of x and y is:',sub)

    if op == '*' or 'multiply':
      mul = float(x) * float(y)
      print('Multiplication of x and y is:',mul)

    if op =='/' or 'divide':
      if y == 0:
        print('Division by Zero!')
      else:
        div = float(x) / float(y)
        print('Division of x and y is:',div)   

      if op == '':
        sum = float(x)+float(y)
        print(sum)

      if op != '+'or '-'or '*'or'/' or 'add'or'subtract'or'multiply'or'divide':
          print('Unknown Operation')

do_arithmetic(6,6,'*')


# In[3]:


def sum_of_digits(s):

  s=input('Enter a string ')
  num=[]
  string=[]
  sum=0
  for i in s:
    
    if i.isalpha():
      string.append(i)
    elif i.isalnum():
      num.append(i)  
      sum += int(i)
    elif num == 0:
       print('The sum of digits operation could not detect a digit!')
       print('The returned input letters are: [ALL NONDIGITS HERE]')  
    if s == '':
        print('Empty string entered!!')
  n=num
  n1='+'.join(n)
     
  print(f'The sum of digit operation performs {n1}')
  print(sum)
  print(f'The extracted non-digits are{string}')  
      
sum_of_digits(2)


# In[7]:


def pluralize():
    #word = input()
    d={}
    file=open("C:/Users/Pooja Rajendra Rai/Downloads/pronoun.txt")
    line=file.readlines()
    #print(line)
    d['plural']=input()
    d['status']=''
    #print(d)
    
    if d['plural'] == '':
        d['status'] = 'empty string'
#         print(d)

    elif d['plural'][-1] == 's':
        d['status'] = 'already_in_plural'
#         print(d)

    elif d['plural'][-1] in 'aeiou':
        d['plural']+='s'
        d['status'] = 'success'
        
    elif d['plural'][-1] == 'y':
        d['plural']+='ies'
        d['status'] = 'success'
        
    elif d['plural'][-1] == 'f':
        d['plural']+='ves'
        d['status'] = 'success'
        
    elif d['plural'][-1] == 'sh'or'ch'or'z':
        d['plural']+='s'
        d['status'] = 'success'
        
    elif d['plural'] == 'bd':
        d['plural']+='s'
        d['status'] = 'success'   
        
    for i in line:
       # print(i)
        if d['plural']+"\n" == i:
            d['status'] = 'proper_noun'
#             print(d)
        
    return d
pluralize() 


# In[4]:


import re
def function_renamer(code):

  f = re.compile('\w+_\w+')
  f = f.findall(code)
  f1 = re.compile('\w+ (\w+)')
  f1 = f1.findall(code)

  f += f1
  d = {}

  rename = []
  
  for i in f:
    if '_' in i:
      rename.append(' '.join(i.split('_')).title().replace(' ', ''))
   

  for i,j in zip(f, rename):
    if i == '_':
      newcode = code.replace(i, '_'+j)
    else:
      newcode = code.replace(i, j)
    d.update({i:{'hash':hash(i), 'camelcase':str(j), 'uppercase':j.upper()}})

  print(newcode)
  print(d)  


# In[5]:


function_renamer('''def add_two_numbers(a, b):
    return a + b
    print(add_two_numbers(10, 20))''')


# In[6]:


function_renamer('''def _major_split(*args):
        return (args[:2], args[2:]''')


# In[ ]:


function_renamer('''def CheckTruth(t = True):
        print('t is', t)
        return _major_split([t]*10)

      x, y = _major_split((10, 20, 30, 40, 50))''')

