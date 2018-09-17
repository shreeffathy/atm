class ATM():
 def __init__(self , balance , bank_name):
  self.balance=balance
  self.bank_name=bank_name
 def withdraw1(self,request):
  print"========================="
  print"Welcome to"+self.bank_name
  print "Current balance"+' '+str(self.balance)
  print"========================="
  balance_total=self.balance - request
  if request > self.balance:
    print"Can't give you all this money !!"
  elif request < 0 :
      print"More than zero plz!"
  else:
       while request > 0:
            if request >= 100:
                request -= 100
                print"give 100"
            elif request >= 50:
                    request -= 50
                    print"give 50"
            elif request >= 10:
                    request -= 10
                    print"give 10"
            elif request >= 5:
                    request -= 5
                    print"give 5"
            elif request >= 2:
                    request -= 2
                    print"give 2"
            else:
                print"give 1"
                request -= 1
  self.balance=balance_total
        
balance1 = 500
balance2 = 1000

atm1 = ATM(balance1,"Smart Bank")
atm2 = ATM(balance2,"Baraka Bank")

atm1.withdraw1(277)
atm1.withdraw1(800)

atm2.withdraw1(100)
atm2.withdraw1(2000)