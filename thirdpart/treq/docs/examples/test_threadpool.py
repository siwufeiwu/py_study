#!/usr/bin/env python 
import threadpool 
import time,random 
 
def hello(str): 
    #time.sleep(2) 
    return str 
 
def print_result(request, result): 
    print "the result is %s %r" % (request.requestID, result) 
 
data = [ random.randint(1,10) for i in range(20)] 
print data
 
pool = threadpool.ThreadPool(2) 
requests = threadpool.makeRequests(hello, data, print_result) 
[pool.putRequest(req) for req in requests] 
pool.wait() 
