# -*- coding: utf-8 -*-
import json


jsonolustur='{"Adi":"serkan","JSoyadi":"Sahin"}'

var=json.loads(jsonolustur) # jsonolustur dosyasını json türüne çeviriyoruz.

print(var["Adi"])
print(var["JSoyadi"])



# Eğerki bizim bi listemiz yada herhangi bir nesnemiz var ise pythonda, bunuda json  datasına çevirmek istediğimiz zaman

jsonDictionary={
    "firstName":"Serkan",
    "lastName":"Sahin"
             } #Örneğin böle bir dictionary imiz var
print(json.dumps(jsonDictionary)) # bu dictionary yi dumps() fonksiyonu ile çevirebiliyoruz. herhangi bir nesneyi json türüne çevirebiliriz.
                                  # ama jsonun asıl yapısı aşşağıdaki konularda mevcuttur.
                                  
# Gerçek JSON datasıyla çalışmak 



# -*- coding: utf-8 -*-

import json
with open("JsonDeneme.json") as data: // dışarıdan bir json datasını çağıracağımız zaman kullanırız. 
    vsd=  json.load(data)
    for x in range(5):
        
        print(vsd[x]["id"]) //jsondaki başlıklar üzerinden ekrana yazdırıyoruz burada.
        print(vsd[x]["address"]["geo"]["lat"])
    
    