#sample
for i in range(1,20):
    if i%2==0 :
        print("Even ",i)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#

#sample of for loop
prices = [10,20,30]
total = 0
for item in prices:
    total += item
print(f'Total: {total}')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#


#nested for loop

numbers = [5,2,5,2,2]

for x_cnt in numbers:
    outp = ''
    for cnt in range(x_cnt):
        outp += 'x'
    print(outp)


# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#


#for else statement it will finish iterating the range loop and output after finishing it with else

num = [1,2,3,4,5]

for i in num:
    if i % 2 == 0:
        print(i)

else:
    print('Finished Iterating')


#for loop and showing the index of the range
#using the enumerate function to the range value or array
for x,y in enumerate(range(5)):
    print("index: ",x , " value of range: " , y)

#Dictionary Data
#using for loop to print the key and value

customer = {
    "name": "John Smith",
    "age": 30,
    "vefied": True
}

for key, val in customer.items():
    print(f"Key: {key}, Value: {val}")


# using zip function in list to unpack the lists
lst1 = ['one','two','three']
lst2 = ['red','green','blue']
lst3 = ['apple','lime','berry']

#this will work with same structured lists
for num, color, fruit in zip(lst1,lst2,lst3):
    print(f'number: {num} is {color} {fruit}')
