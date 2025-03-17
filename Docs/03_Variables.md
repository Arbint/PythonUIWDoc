# Variables

## Variables are used to store data that the program need to use.

### Kinds of variables:

* int
* float
* string
* bool

To create a variable, simply type in the name of the variable and then give it a value with a ```=``` sign.
```py
age = 15 # this is an int
```
```py
height = 6.5 # this is a float 
```

```py
name = "Steve" # this is a string
```
for a string, if you want to put ```"``` inside of the string, use the escape sybol ```\```

```py
stringWithQuote = "string with \" inside"
```
if you need a string with mulitple lines, use ```"""``` around the multiple lines:
```py
"""
this is a multi-line string
here is another line
"""
```

```py
happy = True # this is a bool
```
### Variable Operators
Opeartors are used to do some operation on variables, the one already introduced is the ```=```(assignment) operator, it assign a value to a variable
```py
v1 = 10
```
there is also ```==```(equality) operator. (with 2 = right after the other), it evaluates to a bool based on if the 2 operands are equal or not:

```py
v1 == 10 # evaluates to True because v1's value is 10
```

### Arithmetic Operators
for numbers, here are the common arithmetic operators:
|Operator|Name|Example|
|-------|------|------|
|+|Addition|x+y, x+=y|
|-|Substraction|x-y, x-=y|
|*|Mulitplication|x* y, x*=y|
|/|Division|x/y, x/=y|
|%|Modulus|x%y, x%=y|
|**|Exponentiation|x**y, x ** =y|
|//|Floor Division|x//y, x //=y|

### Order of Operation
the order of operation of and expression follow the same rules in mathmatics, so * and / has higher prority than - and +, for example:
```py
1 + 1 * 2 # evaluates to 3
```
```py
(1 + 1) * 2 # evaluates to 4
```
it is recommend to use ```()``` to enfore the order of operation is not sure. We call anything that can be evaluated to a value like ```(1 + 1) * 2``` an expression.

Other variable types could use the operators above if make common sense:
You can use ```+``` to add 2 strings:
```py
firstName = "Steve"
lastName = "Jobs"
fullName = firstName + " " + lastName
print(fullName)
```
this will print out:
```sh
> Steve Jobs
```
but if you try ```-``` on strings, you will get and error.

Some Variable has their speical operators, for example, ```bool``` variable supports ```and```, ```or```, and ```not``` operator:

```py
hungry = True
happy = not hungry # happy will be False

tired = False
happy = not tired # happy will be True

notHappy = hungry or tired # notHappy will be True

happy = (not hungry) and (not tired) # happy will be False
```