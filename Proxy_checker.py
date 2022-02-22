import requests

url = "http://httpbin.org/ip"

with open('lista.txt') as lista:
    proxy = lista.readlines()

proxy_list = []

for i in proxy:
    t=i[0:-1]
    proxy_list.append(t)

for i in proxy_list:
    try:
        response = requests.get(url, proxies={'http':'http://'+i, 'https': 'https://'+i}, timeout= 3000)
        print(response.text)
    except:
        print(f"Błędne: {i}")
        pass
print("Koniec")