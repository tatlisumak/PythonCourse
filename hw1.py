



import random

class Portfolio:

    def __init__(self,cash=0,stock={},mutual_fund={},bond={},audit_log=[]):
        self.cash = cash
        self.stock = stock
        self.mutual_fund = mutual_fund
        self.bond = bond
        self.audit_log= audit_log
        
           
    def addCash(self,amount):
        self.cash += amount
        self.audit_log.append(f"Cash is added: {amount}")
    
   
    
    def withdrawCash(self,amount):
        self.cash -= amount
        self.audit_log.append(f"Cash is withdrawn: {amount}")
   
   

    def buyStock(self,amount,stock_object):
        
        assert (type(amount) == int),'Stocks can only be bought as integer numbers'
        
        self.amount = amount 
        self.stock_object = stock_object
        
        assert self.cash >= (self.stock_object.price * self.amount),"insufficient cash"
        
        if self.stock_object.ticker not in self.stock.keys():
            self.stock[self.stock_object.ticker] = self.amount
        elif self.stock_object.ticker in self.stock.keys():
            self.stock[self.stock_object.ticker] += self.amount
        
        self.cash -= self.stock_object.price * self.amount

        self.audit_log.append(f"Stock is bought: {stock_object.ticker}, amount: {amount}")

    def sellStock(self,ticker,amount):
        self.amount = amount
        self.ticker = ticker

        self.stock[self.ticker] -= self.amount
        assert self.stock[self.ticker] >= 0,"Insufficient amount of stocks"
        self.cash += (self.stock_object.price*random.uniform(0.5,1.5)) * self.amount

        self.audit_log.append(f"Stock is sold: {ticker}, amount: {amount}")

    def buyMutualFund(self,amount,fund_name):
        self.amount = round(amount,2)
        self.fund_name = fund_name

        assert self.cash >= self.amount,"insufficient cash"

        if self.fund_name.ticker not in self.mutual_fund.keys():
            self.mutual_fund[self.fund_name.ticker] = self.amount
        else:
            self.mutual_fund[self.fund_name.ticker] += self.amount

        self.cash -= self.amount

        self.audit_log.append(f"Mutual fund is bought: {fund_name.ticker}, amount: {amount}")

    def sellMutualFund(self,ticker,amount):
        self.amount = amount
        self.ticker = ticker

        self.mutual_fund[self.ticker] -= self.amount
        assert self.mutual_fund[self.ticker] >= 0,"Insufficient amount of mutual_funds"
        self.cash += (random.uniform(0.9,1.2)) * self.amount

        self.audit_log.append(f"Mutual fund is sold: {ticker}, amount: {amount}")

    def buyBond(self,amount,bond_name):

        self.amount = amount
        self.bond_name = bond_name

        assert self.cash >= self.amount, "insufficient cash"

        if self.bond_name.ticker not in self.bond.keys():
            self.bond[self.bond_name.ticker] = self.amount
        else:
            self.bond[self.bond_name.ticker] += self.amount

        self.cash -= self.amount

        self.audit_log.append(f"Bond is bought: {bond_name.ticker}, amount: {amount}")

    def sellBond(self,ticker,amount):
        self.amount = amount
        self.ticker = ticker

        self.bond[self.ticker] -= self.amount
        assert self.bond[self.ticker] >= 0,"Insufficient amount of mutual_funds"
        self.cash += (random.uniform(0.9,1.2)) * self.amount
        
        self.audit_log.append(f"Bond is sold: {ticker}, amount: {amount}")
    
    def history(self):
        print(self.audit_log)



    def __str__(self):
        
        return (f"cash: {self.cash}, stocks: {self.stock}, mutual_funds: {self.mutual_fund}, bonds: {self.bond}")




class Stock:

    def __init__(self,price,ticker):
        self.price = price
        self.ticker = ticker
        


class MutualFund:

    def __init__(self,ticker): 
        self.ticker = ticker

class Bond:

    def __init__(self,ticker): 
        self.ticker = ticker


        




portfolio = Portfolio()               
portfolio.addCash(300.50)             
print(portfolio.cash)
s = Stock(20, "HFH")                  
portfolio.buyStock(5, s)              
mf1 = MutualFund("BRT")               
mf2 = MutualFund("GHT")               
portfolio.buyMutualFund(10.3, mf1)    
portfolio.buyMutualFund(2, mf2)       
portfolio.history()
print(portfolio)
