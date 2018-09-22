class ATM():
 PAPERS=[100,50,10,5,2,1]
 def __init__(self , balance , bank_name):
  self.balance=balance
  self.bank_name=bank_name
  self.withdrawals_list = []
  
 def withdraw1(self,request):
  print"========================="
  print"Welcome to"+" "+self.bank_name
  print "Current balance"+' '+str(self.balance)
  print"========================="
  balance_total=self.balance - request
  if request > self.balance:
    print"Can't give you all this money !!"
  elif request < 0 :
      print"More than zero plz!"
  else:
      self.take_money(request)
      self.balance=balance_total

 def take_money(self,request):
  for i in ATM.PAPERS:
   while i<=request:
      print("give"+str(i))
      self.withdrawals_list.append(i)
      request -= i
  self.withdrawals_list.append("**")
  

 def show_withdrawals(self):
  sum1=0
  print("****************************************************")
  print("**************************RECEIPT*******************")
  for withdrawal in self.withdrawals_list:
    print(withdrawal)
    if withdrawal != "**":
      sum1 += withdrawal
  print(" the total balance for withdrawals"+' '+"from"+' '+self.bank_name+' = '+str(sum1))


balance1 = 500
balance2 = 1000

atm1 = ATM(balance1,"Smart Bank")
atm2 = ATM(balance2,"Baraka Bank")

atm1.withdraw1(277)
atm1.withdraw1(800)
atm1.withdraw1(200)

atm2.withdraw1(100)
atm2.withdraw1(2000)

atm1.show_withdrawals()
atm2.show_withdrawals()