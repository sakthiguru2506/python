

fruits =['orange','apple','banana']
fruits1 =['banana','kiwi','apple','banana']
print(fruits)

fruits.append("apple")
print(fruits)
fruits.extend(fruits1)
print(fruits)
fruits.insert(3,"mango")
print(fruits)
fruits.remove("apple")
print(fruits)
fruits.pop()
print(fruits)
print("which place have a apple after the 2 index:",fruits.index("apple",0))
print("how many Number of apple inn the  list:",fruits.count("apple"))
fruits.sort()
print("sorted:",fruits)
fruits.reverse()
print("Reverse list:",fruits)
fruits2=fruits.copy()
print("copied list",fruits2)
fruits2.clear()
print("clear function:",fruits2)
