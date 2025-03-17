# Containers
Containers are used to store a collection of values in one variable.

## List
```py
# this is a list
names = ["Ellen", "Carolina", "Leonado"]
```
each one of the element in the list has an index associate with them. the fist item has an index of 0, and the second one has 1, so on and so forth.

so for names the values and their indices are:

|Index|Item|
|---|----|
|0|"Ellen"|
|1|"Carolina"|
|2|"Leonado"|

to access any variable, use the ```[]``` (subscript) operator with the list:
```py
print(names[0]) # prints Ellen
print(names[1]) # prints Carolina
names[2]="Gregory" # changes Leonado to Gregory
print(names[2]) # prints Gregory
```

to get the amount of items in a list, use the ```len()``` function
```py
len(names) # this returns/evaluates to 4
```

you can also get a sub list by using the ```[start:end]``` operator

```py
print(names[0:2]) #prints ["Ellen", "Carolina"]
```
notice the it includes item with index 0, 1, but not 2. the range will include the item of the index on the left side of the ```:```, but exclude the index on the right side of ```:```:
```py
# give a sub list rangeing form index a to index b-1
list[a:b]
```

to add new item to list at the end:
```py
names.append("Steve")
# names now becomes: 
# ["Ellen", "Carolina", "Gregory", "Steve"]
```
to insert a new item to list:
```py
names.insert(1, "Amanda") # insert Amanda bofore index 1
```
to remove an item from list:
```py
names.remove("Amanda") # Amanda will be removed from names
```
2 lists can be added together to a new list that contains the elements of both lists.

```py
listOne = [1,2,3]
listTwo = [4,5,6]
listThree = listOne + listTwo
print(listThree) # prints [1,2,3,4,5,6]
```

## Tuple

```Tuple``` is an inmutale ```list```

to change a tuple, change it to a list first, make the change and then change it back:
```py
newTuple = ("a", 1) # this creates a tuple
listFromNewTuple = list(newTuple) # convert the tuple to list
listFromNewTuple.appen("b") # make changes to list
newTuple = tuple(listFromNewTuple) # convert the list back to tuple 
```
Tuple can also use ```tuple[index]``` and ```len(tuple)``` to access and get the number of elements of a tuple

## Dictionary

a dictionary is just like a realword dictionary, it's a collection of key value pairs.
```py
studentInfo = {"Name": "Steve", "age":20, "level":"sophomore"}
```
in this case, the key value pairs are:
|Key|Value|
|-|-|
|Name|Steve|
|age|20|
|level|sophomore|

to access a value, use the ```[]``` with the ```key```
```py
studentName = studentInfo["Name"] # studentName will be Steve
studentAge = studentInfo["age"] # studentAge will be 20
```
you can also use the ```[]``` with the key to change the value, and use the ```len()``` function to get the number of key value pairs in the dictionary.
to get all the keys in the dictionary:
```py
studentInfo.keys()
```
to get all the values in the dictionary:
```py
studentInfo.values()
```
to remove a key value pair in the dictionary:
```py
del studentInfo["age"] # removes age:20 from the dictionary
```
to add a key value pair, just do
```py
# add grade:"A" as a new key value pair in the dictionary.
studentInfo["grade"] = "A" 
```