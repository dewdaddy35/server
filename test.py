# Dictionaries

user = {
    "name": "Eric",
    "lastName": "Wells",
    "age": 54,
}
print(user)
#print(type(user))

#print(user["name"]+" "+user["lastName"])

# array but in python this is a list
number = [1,2,3]
#print(number)
number.append(4)

#print(number)
# Length
#print(len(number))#counts items
#print(len(user["name"]))#counts number of characters
#print(len(user))#count number of keys

ages = [32, 74, 20, 69, 52, 26, 31, 77, 43, 73, 51, 57, 19, 79, 40, 34, 27, 23, 21, 44, 53, 55, 24, 36, 41, 47, 78, 46, 68, 75, 49, 83, 61, 60, 29, 56, 67, 17, 70, 81, 87, 38]

def exc1():
    #print all the numbers in ages
    #calculate total sum of th numbers in age
    # count how many number in ages are less than 30

    total = 0
    count = 0
    count2 = 0
    for age in ages:
        total += age
        print(age)
        if age < 30 :
            count += 1
        print(total)
        print("There are "+str(count)+ "numbers that are less than 30")
        if age > 30 and age < 50:
            count2 += 1
        print("There are " + str(count2)+ "numbers that are less than 30 and 50")   



    
    # call the functions
exc1()
