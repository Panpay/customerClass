class customerList:
    def __init__(self):
        super().__init__(self):
        self.fnl = ['fname','lname','email','password','subscribed']
    def add(self,item):
        self.data.append(item)
        