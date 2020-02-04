from customer import customerList

cl = customerList()
# d = {'fname':'Testguy':'lname':'test',\
# 'email':'a@a.com','password':'123','subscribed':'1'}
# cl.add(d)
cl.set('fname','Testguy')
cl.set('lname', 'Test')
cl.set('email','a@a.com')
cl.add()
cl.add()

print(cl.data)
print(cl.data[0])
# cl.data[0]['email'] = 'b@b.com'
cl.update(0,'email','b@b.com')
print(cl.data[0]['email'])
