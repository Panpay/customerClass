from customer import customerList

cl = customerList()
d = {'fname':'Testguy':'lname':'test',\
'email':'a@a.com','password':'123','subscribed':'1'}
cl.add(d)
print(cl.data)