class customerList:
    #this is the assignment
    def __init__(self):
        self.data = []
        self.tempdata = {}
        self.tn = 'customers'
        self.fnl = ['fname','lname','email','password','subscribed']
        self.conn = None
    def connect(self):
        seld.conn = pymysql.connect(host='mysql.clarksonmsda.org', port=3306, user='yuxchen', passwd='Phpmyadmin1', db='yuxchen_is437test', autocommit=True)
    def add(self):
        self.data.append(self.tempdata)
    def set(self,fn,val):
        if fn in self.fnl:
            self.tempdata[fn] = val
        else:
            print('Invalid field: ' + str(fn))
        def update(self,n,fn,val):
            if len(self.data) >= (n + 1) and fn in self.fnl:
                self.data[n][fn] = val
            else:
                print('could not set value at row ' + str(n) + 'col' + str(fn))
    def insert(self,n=0):

        cols = '","'.join(self.fnl)
        cols = '"'+cols+'"'
        vals = ('%,' * len(self.fnl))[:-1]
        tokens = []
        for fieldname in self.fnl:
            tokens.append(self.data[n][fieldname])
        
        sql = 'INSERT INTO `' + self.tn + '+' (+cols)
        #conn = pymysql.connect(host='mysql.clarksonmsda.org', port=3306, user='yuxchen', passwd='Phpmyadmin1', db='yuxchen_is437test', autocommit=True)
        self.connect() 
        cur = conn.cursor(pymysql.cursors.DictCursor)
        print(sql)
        print(tokens)