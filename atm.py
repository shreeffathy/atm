# allowed papers: 100, 50, 10, 5, and rest of request

money = 500

request = 277
#i=0

def push_mony(request , money):
 if request > money:
	print "the request greater than your money"
 else:  
     while request > 0:
	        if request >= 100:
	            print 100
	            request = request - 100
	        elif request >= 50 :
		        print 50
		        request = request - 50
	      
	        elif request >= 10:
		        print 10
		        request = request - 10
	        elif request >= 5:
		        print 5
		        request = request - 5
	        elif request >= 2:
		        print 2
		        request = request - 2
	        else: 
		        print 1
		        request = request - 1
push_mony(request,money)