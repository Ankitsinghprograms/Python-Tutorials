import json 

#json.loads()

dictionary='{"one":1,"second":2}'
parsed=json.loads(dictionary) 
#parsed function change string any meaningful Thiqng In this example str''
print(parsed)


#json.dumps() 

dictionary={"user1":{"name":"Ankit singh","id":[36363636,1],"online":False},"user2":{"name":"Sumit singh","id":36363663,'online':True}}

p=json.dumps(dictionary,sort_keys=True)

print(p)

d={1:2,3:4,5:6,2:5}

p=json.dumps(d,sort_keys=True)

print(p)


#json.load()

#Same as json.loads() but takes file as an argument