old_keys = ['number', 'address', 'name', 'longitude', 'latitude']
nu_key = ['number', 'address', 'name', 'longitude', 'latitude', 'zip_code',
          'city']
number = []
address = []
name = []
longitude = []
latitude = []
new_name = []
new_address = []
zipz = []
city = []
zipc = []
city2 = []
final = []
import json
lista_stat = json.loads(open('velib.json').read())
for stat in lista_stat:
    number.append(stat[old_keys[0]])
    address.append(stat[old_keys[1]])
    name.append(stat[old_keys[2]])
    longitude.append(stat[old_keys[3]])
    latitude.append(stat[old_keys[4]])
for i in name:
    new_name.append(i[8:])
for i in address:
    a = i.split(" - ")
    new_address.append(a[0])
    zipc.append(a[1:])
for i in zipc:
    b = (', '.join(i))
    c = b.split(" ")
    zipz.append(c[0])
    city.append(c[1:])
for i in city:
    d = (' '.join(i))
    city2.append(d)
kk = len(number)
for i in range(0, kk):
    dic = {}
    dic[nu_key[0]] = number[i]
    dic[nu_key[1]] = new_address[i]
    dic[nu_key[2]] = new_name[i]
    dic[nu_key[3]] = longitude[i]
    dic[nu_key[4]] = latitude[i]
    dic[nu_key[5]] = zipz[i]
    dic[nu_key[6]] = city2[i]
    final.append(dic)
with open('solution.json', 'w') as soluc:
    json.dump(final, soluc)
soluc.close
