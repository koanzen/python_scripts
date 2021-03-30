from pprint import pprint,pformat #This module pretty prin Dictionary and List, etc.

#Sample of Dictionary data type 
#remember like List is mutable and variables reference to the value of the dictionary as a whole
#any changes in the objects inside the dictionary will not affect the ID of the dictionary
#check the List data type bug.

customer = {
    "name": "John Smith",
    "age": 30,
    "vefied": True
}

print(customer)
print(id(customer),"- id of the unchanged dictionary")

print(customer["name"])

#changing the value of key in the dictionary
customer["name"] = "Ben Smith"
print(customer["name"])

#getting, checking and supplying in key objects in dictionary
#checking
print(customer.get("bdate"), "- Checking the key exist") #This will return None datatype if not exist

print(customer.get("bdate", 0), "- Checking the key exist return 0 if not") #return 0 if key not exist

print(customer.get("color",''), "- Checking the key exist return '' if not") #return '' blank string if key not exist

print(customer,"checking not existing keys")

#assigning default value to none existing key
customer["bdate"] = "July 27 1982"

# OR using the setdefault
#but set default will not change the value of the key if it's already existing
#this is only applicable if key is not existing
customer.setdefault("bday", "July 27 1982")

print(customer, "added not existing key")


#check id of changed dictionary
print(id(customer),"- id after changed dictionary")


#using for loop to print the key and value

for key, val in customer.items():
    print(f"Key: {key}, Value: {val}")



#sample function generating dictionary from string

msg = "It was a bright cold day in April, and the clocks where striking thirteen."

cnt = {}

for chr in msg.upper():
    cnt.setdefault(chr,0)
    cnt[chr] += 1


#print(cnt) #ordinary print
#pprint(cnt) #pretty print the output using the pprint module its like a beautification output


#Or if you want to save it somewhere else we can use pformat in the pprint module to cache the output
fcnt = pformat(cnt)

print(fcnt)



# Other samples

# Creating a list of dictionary
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

d3 = []
d3.append(d1)
d3.append(d2)

print(d3)