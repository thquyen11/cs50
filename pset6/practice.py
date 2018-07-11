
print("Hello World")

name="Quyen"
print(name)
print("Age is: ", 20+8)

print("no new line ", end="")
print("newline")

groceryList=['Juice', 'Tomatoes','Potatoes','Bananas']
print(groceryList)
groceryList[0]='Green Juice'
print(groceryList)

otherEvents=['Wash Car','Pick up Kids','Cash Check']
todoList=[otherEvents,groceryList]
print(todoList[0][2])

groceryList.append('newAppend')
print(groceryList)
groceryList.pop(0)
print(groceryList)
groceryList.insert(1,'newInsert')
print(groceryList)
groceryList.sort()
print("groceryList sorted: ", groceryList)

del groceryList[0]
print("del the 1st item: ", groceryList)

print(len(todoList))
print("max todoList: ", max(groceryList))

# TUPLES
multi_line_quote=''' Values in a tuple 
 can't change like lists '''
print(multi_line_quote)

piTuple=(3,1,4,1,5,9)

# Convert tuple into a list
newTuple = list(piTuple)







