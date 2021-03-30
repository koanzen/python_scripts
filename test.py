# Considering Dict as our iterable parameter
import pyperclip as clip

# testing pyperclip
print(clip.paste())

clip.copy('')


# testing lamda with dictionary
iter_Dict = {"Python":0, "CSharp":0, "Java":0}
print(iter_Dict)

map_result =  dict(map(lambda x: (x[0],x[1]+1), iter_Dict.items()))

print(map_result)

##=-=-=-=-=-=-=-=-=

def xfunc(**data):
    a = data['num1']
    b = data['num2']
    return int(a) + int(b)
 
    
print(xfunc(num1=3,num2=5))


print(True > False)
print(True < False)

