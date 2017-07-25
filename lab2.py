Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a= 'save'
>>> b= 'the'
>>> c= 'plaet'
>>> print("'save' + 'the' + 'planet'")
'save' + 'the' + 'planet'
>>> print(' a +b + c)
      
SyntaxError: EOL while scanning string literal
>>> print(a+b+c)
savetheplaet
>>> a= 'save '
>>> b= 'the '
>>> c= 'planet.'
>>> print(a+b+c)
save the planet.
>>> a= 4
>>> b= 'panda bears'
>>> print(str(a)+b)
4panda bears
>>> b= ' panda bears'
>>> print(str(a)+ b)
4 panda bears
>>> x = water bottle
SyntaxError: invalid syntax
>>> x = water_bottle
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    x = water_bottle
NameError: name 'water_bottle' is not defined
>>> water_bottle = x
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    water_bottle = x
NameError: name 'x' is not defined
>>> x = 'water bottle'
>>> len(x)
12
>>> upper(x)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    upper(x)
NameError: name 'upper' is not defined
>>> NameError: name 'upper' is not defined
SyntaxError: invalid syntax
>>> 
>>> 
>>> lower(x)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    lower(x)
NameError: name 'lower' is not defined
>>> 
>>> x.upper
<built-in method upper of str object at 0x7f4e59ad8530>
>>> x.upper()
'WATER BOTTLE'
>>> x.lower()
'water bottle'
>>> a.capitalize()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a.capitalize()
AttributeError: 'int' object has no attribute 'capitalize'
>>> x.capitalize()
'Water bottle'
>>> x.swapcase()
'WATER BOTTLE'
>>> x.replace('w','p')
'pater bottle'
>>> a="MEET"
>>> b="meet'
SyntaxError: EOL while scanning string literal
>>> b= "meet"
>>> c= "Meat"
>>> a==b
False
>>> a==c
False
>>> b==c
False
>>> a !=b
True
>>> a !=c
True
>>> b !=c
True
>>> 
