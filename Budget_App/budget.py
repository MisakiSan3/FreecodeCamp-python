import math

# ************************Class Category*************
class Category:
    
    def __init__(self, name: str):
      
      # Validation for Name
        assert isinstance(name, str), f"This instance attribute should be String"
        self.name = name
        self.ledger = []
    
    def __str__(self):
        
        objDetails = f'{str(self.name).center(30,"*")}\n'
        for x in self.ledger:
            objDetails += str(x.get("description")[:23]).ljust(23) + "{:.2f}".format(x.get("amount")).rjust(7) + "\n"
        objDetails += "Total: " + "{:.2f}".format(self.get_balance())
        return objDetails
        
    
    def deposit(self, amount, description=""):
        if (isinstance(amount,int) or isinstance(amount,float)) and amount > 0: # Initiating the deposit only if amt is > 0
            deposit_dict = dict(amount = amount, description = description)
            self.ledger.append(deposit_dict)
    
    def check_funds(self, amount):
        balance = self.get_balance()
         
        if balance >= amount:
            return True # sufficient funds available
        else:
            return False # Insufficient Funds
           
            
    def withdraw(self, amount, description=""):
        if  (isinstance(amount,int) or isinstance(amount,float)) and amount > 0 and self.check_funds(amount): # Initiating the withdrawal only if 
            # the amount is > 0 and there are sufficient funds
            amount = float("-" + str(amount))
            deposit_dict = dict(amount = amount, description = description)
            self.ledger.append(deposit_dict)
            return True # withdrawal successful
        else:
            return False # Insufficient Funds / Amount <= 0
            
    
    def transfer(self, amount, obj_catetory):
        if isinstance(obj_catetory,Category) and amount > 0 and (isinstance(amount,int) or isinstance(amount,float)): # Initiating the transfer only if 
            # the amount is > 0 and obj_Category is valid
            description = "Transfer to " + obj_catetory.name
            if self.withdraw(amount,description):
                description1 = "Transfer from " + self.name
                obj_catetory.deposit(amount,description1)
                return True # Transfer successful
            else:
                return False # Withdrawal unsuccessful because of insufficient funds
        else:
            return False # Category doesn't exists or amount <= 0
            
    def get_balance(self):
        balance = 0
        for x in self.ledger:
            balance += x.get("amount",0)
        return balance
# *************** end of Class ****************

def create_spend_chart(categories):
    outputStr = "Percentage spent by category\n"
    catPercentage = {}
    if len(categories) > 0:
        withdrawaldict = {}
        totalwithdrawals = 0
        for item in categories:
            withdrawals = 0
            for x in item.ledger:
                withdrawals += float(str(x["amount"])[1:]) if x.get("amount") < 0 else x.get(0, 0)
            if withdrawals > 0:
                totalwithdrawals += withdrawals
                withdrawaldict[item.name] = withdrawals
        for k,v in withdrawaldict.items():
            #checkvalue = round(((v / totalwithdrawals) * 100) / 10) * 10
            checkvalue = math.floor(((v / totalwithdrawals) * 100) / 10) * 10
            if checkvalue >= 0:
               catPercentage[k] = checkvalue
                
    else:
        return "List is empty"
    
    myList1 = []
    for v in catPercentage.values():
        myList1.append(v)
    
    count = 100
    outputStr1 = ""
    while count >= 0:
        if count == 100:
            outputStr1 += f'{count}| {createBar(myList1,count)}\n'
        else:
            outputStr1 +=  f'{str(count).rjust(3)}| {createBar(myList1,count)}\n'
        count -= 10
    
    outputStr1 += "-".rjust(5)
    
    
    keyList = []
    for i in catPercentage.keys():
        outputStr1 += "---"
        keyList.append(i)
    
    outputStr1  += createCatNames(keyList)   
    return outputStr + outputStr1
# ************************************************
def createBar(myList,count):
    myStr = ""
    for i in range(len(myList)):
        if myList[i] < count:
            myStr += "   "
        else:
            myStr += "o  "
    return myStr
# *************************************************
def createCatNames(keyList):
    myStr1 = ""
    max1 = 0
    min1 = 0
    count = 0
    for i in keyList:
        if len(i) > max1:
            count += 1
            max1 = len(i)
            if count == 1:
                min1 = max1
        if len(i) < min1:
            min1 = len(i)
    
    for i in range(max1):
        myStr1 += "\n"
        myStr1 += "     "

        flag1 = 0
        flag2 = 0
        flag3 = 0
        for j in range(len(keyList)):
            if i <= len(keyList[j])-1 and i < min1:
                # if j < len(keyList)-1 :
                    myStr1 += keyList[j][i] + "  "
                # else:
                    # myStr1 += keyList[j][i]
            elif i <= len(keyList[j])-1 and i >= min1:
                if j == 0:
                    myStr1 += keyList[j][i] + "  "
                    flag1 = 1
                elif j == 1:
                    if flag1 == 0:
                        myStr1 += "   " + keyList[j][i] + "  "
                        flag2 = 1
                    else:
                        myStr1 += keyList[j][i] + "  "
                        flag2 = 1
                elif j == 2:
                    if flag1 == 0 and flag2 == 0:
                        myStr1 += "      " + keyList[j][i] + "  "
                        flag3 = 1
                    elif flag1 == 1 and flag2 == 0:
                        myStr1 += "   " + keyList[j][i] + "  "
                        flag3 = 1
                    elif flag2 == 1:
                        myStr1 += keyList[j][i] + "  "
                        flag3 = 1
                elif j == 3:
                    if flag3 == 1:
                        myStr1 += keyList[j][i] + "  "
                    else:
                        if flag1 == 0 and flag2 == 0 and flag3 == 0:
                            myStr1 += "         " + keyList[j][i] + "  "
                        elif flag1 == 1 and flag2 == 0 and flag3 == 0:
                            myStr1 += "      " + keyList[j][i] + "  "
                        elif (flag1 == 0 and flag2 == 1 and flag3 == 0) or (flag1 == 1 and flag2 == 1 and flag3 == 0):
                            myStr1 += "   " + keyList[j][i] + "  "
    return myStr1