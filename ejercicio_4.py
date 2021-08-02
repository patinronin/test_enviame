import requests
import json

url = 'https://stage.api.enviame.io/api/s2/v2/companies/401/deliveries'

headers = {"Accept": "application/json",
"api-key": "ea670047974b650bbcba5dd759baf1ed",
"Content-Type": "application/json"}

payload = {
  
  "name": "Crear envio",
    "request": {
        "method": "POST",
        "header": [
            {
                "key": "Accept",
                "value": "application/json"
            },
            {
                "key": "api-key",
                "value": "ea670047974b650bbcba5dd759baf1ed"
            },
            {
                "key": "Content-Type",
                "value": "application/json"
            }
        ],
        "body": {
            "mode": "raw",
            "raw": {"shipping_order": {
                "n_packages": "1",
                "content_description": "ORDEN 255826267",
                "imported_id": "255826267",
                "order_price": "24509.0",     
                "weight": "0.98",       
                "volume": "1.0",
                "type": "delivery" },
                "shipping_origin": 
                    { "warehouse_code": "401"  },
                       "shipping_destination":{     
                            "customer":
                             { 
                                "name": "Bernardita Tapia Riquelme",
                                "email": "b.tapia@outlook.com",
                                "phone": "977623070"},
                             "delivery_address": { 
                                 "home_address": {
                                      "place": "Puente Alto",
                                      "full_address": "SAN HUGO 01324, Puente Alto, Puente Alto"}
                                      } 
                                    },   
                                     "carrier": { 
                                         "carrier_code": "blx",
                                        "tracking_number": "" }
                                        }
                                    },
   
    },
}




r = requests.post(url, data=json.dumps(payload), headers=headers)
print(r.content)


with open("response_ejercicio_4.txt","wb") as file:
    file.write(r.content)
