"""
this program have 2 diferent results in one result the increment of the next range of delivery 
is by 100 km 
and the other result the increment of next range of delivery is the sum of the two past ranges
the reason why this choice is because the time to delivery is extremely large using the increment  the range by 100 km 
 
"""


print("-------------- result 1 ------------")
km_days_to_delivery = [(100,0), (200,1), (300,1), (400,2), (500,3)]

while(km_days_to_delivery[-1][0] < 2000):
    km = km_days_to_delivery[-1][0] + 100
    days = km_days_to_delivery[-1][1] + km_days_to_delivery[-2][1]
    km_days_to_delivery.append((km,days))

for element in km_days_to_delivery:
    print("Number of km: {}  days to delivery: {}".format(element[0], element[1]))


km_days_to_delivery = [(100,0), (200,1), (300,1), (400,2), (500,3)]
print("------------- resutl 2  ----------")

while(km_days_to_delivery[-1][0] < 2000):
    km = km_days_to_delivery[-1][0] +  km_days_to_delivery[-2][0]
    days = km_days_to_delivery[-1][1] + km_days_to_delivery[-2][1]
    km_days_to_delivery.append((km,days))

for element in km_days_to_delivery:
    print("Number of km: {}  days to delivery: {}".format(element[0], element[1]))
