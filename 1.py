INVAL=1234
from datetime import datetime
# import pandas as pd
# import numpy as np
# import matplotlib as plt
import socket
from collections import defaultdict
intime=datetime.now()
listofoods=[]
newfoods=[]
orderstack=[]
timestack=defaultdict(float)
def sendorder(ID,item,qnty):
    msg=str(ID)+','+str(item)+','+str(qnty)
    s=socket.socket()
    port=22123
    host=ID
    try:
         s.connect((host,port))
    except Exception as e:
        print "connection failed"
    def send(msg):
        tsent=0
        while tsent<len(msg):
            sent=s.send(msg[tsent:])
            if sent==0:
                raise RuntimeError("Socket Connection Broken")
            tsent+=sent
    send(msg)
def sendmsg(ID,msg):
    s=socket.socket()
    port=22123
    host=ID
    try:
         s.connect((host,port))
    except Exception as e:
        print "connection failed"
    def send(msg):
        tsent=0
        while tsent<len(msg):
            sent=s.send(msg[tsent:])
            if sent==0:
                raise RuntimeError("Socket Connection Broken")
            tsent+=sent
orderfile=["lays,coke","samosa,chai"]
def recvmsg(clID):
    s = socket.socket()
    host = socket.gethostname()
    port = 22122
    s.bind(('', port))
    s.listen(5)
    c, addr = s.accept()
    l=c.recv(1024)
    return l

def getindex(obj):
    ind=0
    for i in listofoods:
        if i.name==obj:
            return ind
        ind+=1
    return ind
def SETORDERS(orderfile):
    l=[]
    for rows in orderfile:
        for i in rows.split(','):
            l.append(i)
            l1.append(i)
    listofoods=set(l1)
    for rows in orderfile:
        for i in rows.split(','):
            listofoods[getindex(i)][alongwith]+=1#.append(i)


    # return set(l)
# listofoods=SETORDERS(orderfile)
class ITEM(object):
    def __init__(self, name,value):
        # super(ITEM, self).__init__(name,value)
        self.name = name
        self.value=value
        self.count=0
        self.alongwith=defaultdict(int)

class client(object):
    def __init__(self,ID):
        self.ID=ID
    def giveorder(self,item,qnty):
        servID=self.ID
        if(searchitem(item,qnty)!=-1 and searchitem(item,qnty)!=-2):
            sendorder(servID,item,qnty)
            print "your order has been placed."
        if(searchitem(item,qnty)==-1):
            print "not enough quantity",qnty-searchitem(item,qnty)
        else:
            print "item not in menu we'll try to include it"

class server(object):
    def __init__(self,ID):
        self.ID=ID
    def recieveorder(self,clID):
        msg=recvmsg(clID).split(',')
        item=msg[1]
        qnty=int(msg[2])
        print "New order recieved from",clID,qnty,",",item.name
        item.count=item.count-qnty
        orderstack.append([clID,item.name,qnty])
        timestack[[clID,item.name,qnty]]=datetime.now()
    def sendnotification(self,clID,msg):
        sendmsg(clID,msg)
    def ordercomplete(self):
        sendnotification(self,clID,"you order is complete!")
def searchitem(name,q):
    for i in listofoods:
        if i.name==name:
            if i.count>=q:
                return 1
            else : return q-i.count
        else :
            return -2

clnt=client("127.0.0.1")
serv=server("127.0.0.1")
while (1):
    print "dfd"
    ordr=raw_input("give your order").split(',')
    if(len(ordr)==1):ordr.append(1)
    clnt.giveorder(ordr[0],int(ordr[1]))
    serv.recieveorder("127.0.0.1")
    if(len(orderstack)):
        if(datetime.now()-stack[orderstack[::-1][0]]>=10):
            serv.sendnotification(orderstack[::-1][0][0],"please collect your order")

    # tmp=ITEM("lays",INVAL)
    # tmp.count+=1;
    # listofoods.append(tmp)
