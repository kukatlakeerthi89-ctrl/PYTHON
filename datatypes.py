#data types in python
a= 10
print(type(a))
phone = True
print(phone)
print(type(phone))
b = 10.5
print(type(b))
z = 3+4j
print(z)
print(type(z))
g = "uma"
print(g)
print(type(g))

#list in python
#list is an ordered and changeable collection that can store  multiple values
marks = [80, 90, 75,85]
print(marks)

#accessing elements in a list
marks = [80, 90, 75, 85]

print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])

#change elements in a list
marks = [80, 90, 75]
marks[1] = 100
print(marks)

#add elements to a list
marks = [80, 90, 75]
marks.append(85)
print(marks)

#remove elements from a list
marks = [80, 90, 75]
marks.remove(80)
print(marks)

#insert elements in a list
numbers = [10, 20, 30]
numbers.insert(1, 15)
print(numbers)

#extend elements in a list
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)

#clear elements in a list
numbers = [10, 20, 30]
numbers.clear()
print(numbers)

#index of an element in a list
numbers = [10, 20, 30, 40]
print(numbers.index(30))

#count of an element in a list
numbers = [10, 20, 30, 40, 30,  50]
(numbers.count(30))
print(numbers.count(30))

#sort elements in a list
numbers = [10, 20, 30, 40, 50, 60]
numbers.sort()
print(numbers)

#reverse elements in a list
numbers = [10, 20, 30, 40]
numbers.reverse()
print(numbers)

#copy elements in a list
a = [1, 2, 3]
b = a.copy()
print(b)

#slicing: (start,stop,step) elements in a list
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(numbers[1:4])    
print(numbers[2:])     
print(numbers[::-1])    

#tuples in python
#Tuple is a collection of multiple values that is ordered and cannot be changed after creation
student = ("keerthi", 98, "python")
print(student[0])
print(student[1])
print(student[2])

#access values in a tuple
student = ("Keerthi",17, 85.5, "python")
print(student[0])
print(student[1])
print(student[2])
print(student[3])

#immutable nature of tuples
student = ("keerthi",17,"python")
#this gives an error because tuple is not changed

#tuples are immutable 
numbers = (10, 20, 30, 20)
print(numbers.count(20))

#index elements in a list
numbers = (10, 20, 30, 40)
print(numbers.index(20))

#operators elements in a list
numbers = (10, 20, 30, 40)
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#set in python
#set is a collection of unique values that is unordered and 
numbers = {10, 20, 30, 20, 10}
print(numbers)

#why use set?
#suppose students have selected subjects
subjects = {"Python","Java", "Python", "SQL", "Java"}
print(subjects)

#add values top a set
subject = {"python", "sql"}
subjects.add("java")
print(subjects)

#remove values in a set
subjects = {"java", "python", "SQL"}
subjects.remove("SQL")
print(subjects)

#sets do not allow duplicate values
numbers = {1, 2, 2, 3, 3, 3, 4}
print(numbers)

#dictionaries in python
#dictionaty is a collection of key values that are unordered and mutable
student = {"name": "keerthi",  "marks": 94, "subject": "python" , "age": 18,"course": "aiml"}
print(student.keys())
print(student.values())
print(student.items())

#accessing elements in dictionary
print(student["name"])
print(student["age"])
print(student["course"])

#change values in a dictionary
student["age"] = 18
print(student["age"])

#add new data to a dictionary 
student["city"] = "vijayawada"
print(student)

#remove data 
student.pop("city")
print(student)

#get() returns the values of the specified key
print(student.get("name"))

#update()updates the values of the specified key
student.update({"age":17})

#popitem() removes the last inserted key-value pair
student = {"name": "keerthi","age":17,"course":"python"}
student.popitem()

#set default
student = {"name": "keerthi"}
student.setdefault("age",18)
print(student)

#clear method
student.clear()
print(student)

#copy method
student = {"name":"keerthi","age":17}
new_student = student.copy()
print(new_student)

#order of evaluation(BODMAS)
result = (10+5)*2
print(result)

result = 2+13*2
print(result)

                    


        
