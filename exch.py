from binance.client import Client
import json
import requests
# client =Client(api_key=,api_secret=);
exch_info = requests.get('https://api.binance.com/api/v3/exchangeInfo')
print(exch_info)
print(type(exch_info))
# print(exch_info.content)
y = json.loads(exch_info.text)
# y = json.dumps(exch_info)
print(type(y))
print(y)
print("\n\nprinting  dict. keys below:\n\n")
x = y.keys()
print(x)
print("\n\nprinting  dict. values below:\n\n")
z = y['symbols']
print(type(z))
print("---------------------------------------------------------------")
print(len(z))
print(z)
res = []
res.extend(z)
print("-------------------------------------------")
print(res)
print(len(res))
print(type(res))
print(res[0])
# print(res[1])
for d in res[:5]:
    print(d['symbol'])
# print(z[0])
# print(z)
# print(z[0])
# print(type(z[0]))
print("----------------------------------------------------------------------------------------------------------")
# for x, z in y.items():
#     print(x, ":", z)

# print(str)
# print(exch_info['symbols'])
# print(symbols)
# file = 'file1.json'
# with open(file, 'w') as file_object:  # open the file in write mode
#     json.dump(exch_info, file_object)
# data = {

#     'symbol': '',
#     'status': ''
# }

# print(data)
# Find dictionary matching value in list
# result = None
# for sub in y:
#     if sub['symbol'] == 'ETHBTC':
#         res = sub
#         break

# # printing result
# print("The filtered dictionary value is : " + str(result))


def search(name, z):
    return [element for element in z if element['symbol'] == name]


name = input("enter symbol name :")
res = search(name, z)
# print(res)
# print(type(res))

# convert  result to dictionary
print("-----------------------------------------------------------")
dict_res = {}
for d in res:
    dict_res.update(d)

# printing result
print("-----------result :--------", str(dict_res))
print("its baseAsset and  baseAssetPrecision ")
print(dict_res['baseAsset'])
print(dict_res['baseAssetPrecision'])
