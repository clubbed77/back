s = 'a'
r='t'
s=r

g = ['a','b', 'c']
k = g
g[0]='e'
print (k)


r = 4
if r >=- 2:
    print('R is more than 2')

e = "i`m e 2"
if e == "i`m e":
    print('e is e')

else:
    print('e is not e')

if e == "i`m e":
    print('e is e')

elif e == "i`m e 1":
    print('e is e 1')
else:
    print ("e not e")
 


for a in g:
    print(a)

text_list=[2, 4, 6, 8, 10, 12]



total_sum = 0
for w in text_list:
   
    if w > 8:
        total_sum += w
        print("more than 8", w)
    else:
        print("less or equal 8", w)
print (w)
print (total_sum)

f = True
f = False
print(f)

i = 0
while i < 10:
    
    if i == 2:
        i += 1
        continue
    print (i)
    if i == 6:
        break
    i += 1

print ("ss")

x = [
    [2, 5, 8],
    [10, 12, 13],
]

sum = 0
for y in x: 
    for u in y:
        sum += u
print(sum)

dict_h = {
    "key1": {
        "d":44,
        "f":None,
        "s":{
            8:44,
            9:None,
            10:{"m":["s",7]}
        },
    },
    "key2":{
        "fff1":44,
        "f":None,
        }
}

for h in dict_h.keys():
    print(h)

for h in dict_h.values():
    print(h)

# [(key1, value1), (key2, value2), ....]
for k, h in dict_h.items():
    if k == dict_h.items():
        print(h)

transactions_1 = {
    "1":{
        "add":True,
        "sum":2,
        "person":{
            "name":"Petro",
        }
    },
    "2":{
        "add":True,
        "sum":2,
        "person":{
            "name":"Petro",
            "male":True
        }
    },
    "3":{
        "add":False,
        "sum":2,
        "person":{
            "name":"Petro",
            "male":True
        }
    },
    "3":{
        "add":False,
        "sum":2,
        "person":{
            "name":"Petro",
            "male":True
        }
    }
}

total_amount = 0
for transaction in transactions_1.values():
    if transaction['add'] and "male" in transaction["person"].keys():
        total_amount += transaction["sum"]
print(total_amount)


transactions_homework = [
    {
        "add":True,
        "amount":69,
        "products":[
            "Bread",
            "Масло",
            "Сок",
        ]
    },
    {
        "add":True,
        "amount":30,
        "products":[
            "Сок",
        ]
    },
    {
        "add":True,
        "amount":94,
        "products":[
            "Мука",
            "Bread",
            "Масло",
        ]
    },
    {
        "add":False,
        "amount":24,
        "products":[
            "Конфеты",
            "Bread",
        ]
    },
    {
        "add":True,
        "amount":9,
        "products":[
            "Bread",
            "Шоколад",
            "Гречка",
        ]
    },
    {
        "add":True,
        "amount":91,
        "products":[
            "Апельсин",
            "Гречка",
        ]
    },
    {
        "add":True,
        "amount":84,
        "products":[
            "Помидоры",
            "Сок",
        ]
    },
    {
        "add":False,
        "amount":45,
        "products":[
            "Bread",
            "Гречка",
        ]
    },
    {
        "add":True,
        "amount":9,
        "products":[
            "Лимон",
            "Сок",
        ]
    },
]

total_amount = 0
for transaction in transactions_homework:
    if transaction['add'] and "Bread" in transaction["products"]:
        total_amount += transaction["amount"]
print(total_amount)