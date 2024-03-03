from resources. utils import *

# Lê arquivo de balance
balance = open('balance.txt', 'r', encoding='utf-8').read()
print(type(balance))

result = balance.encode('ascii', 'ignore').decode('utf-8')
print(result)