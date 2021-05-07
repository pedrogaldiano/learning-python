class Category():
    def __init__(self, c):
        self.category = c
        self.ledger = list()
    
    def __str__(self):
        length = len(self.category)
                    
        temp = int((30-length)/2)
        n =  temp if length <= 30 else 0
        
        title = '*'* n + (self.category).capitalize() + '*'*n
        
        amount_f, amount_s, descr = [], [], []

        for dic in self.ledger:
            for info in dic.values():
                if type(info) is int or type(info) is float:
                    info = float(info)
                    amount_f.append(info)
                    temp = '{0:>7.2f}'.format(info)
                    amount_s.append(temp)
                    
                elif type(info) is str:
                    descr.append(f'{info[:23]:<23}')
        recipe = ''
        for i in range(len(amount_s)):
            recipe = f'{recipe}\n{descr[i]}{amount_s[i]}'
            
            
        botton = '\nTotal: {:.2f}'.format(sum(amount_f))
        
        self.category = (title + recipe + botton)
        
        return self.category
 
    def get_withdraw(self):
        balance = []
        for dictionary in self.ledger:
            for value in dictionary.values():
                if (type(value) is int or type(value) is float) and value < 0:
                    balance.append(value)
                   
        return sum(balance)          
        
    def get_balance(self):
        balance = []
        for dictionary in self.ledger:
            for value in dictionary.values():
                if type(value) is int or type(value) is float:
                    balance.append(value)
                   
        return sum(balance)    


    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True


    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
    
    
    def withdraw(self, amount, description=''):
        if self.check_funds(amount) == False:
            return False

        self.ledger.append({'amount': -(amount), 'description': description})
    
        return True
    

    def transfer(self, amount, department):
        
        if self.check_funds(amount) == False:
            return False
 
        self.withdraw(amount, 'Transfer to ' + (department.category).capitalize())
        department.deposit(amount, 'Transfer from ' + (self.category).capitalize())
        
        return True


def create_spend_chart(categories):
    
    title = 'Percentage spent by category'
    
    max_len, expenditures, departments = [], [], []
    
    for categ in categories:
        expenditures.append(categ.get_withdraw())
        departments.append((categ.category).capitalize())
        max_len.append(len(categ.category))
        
    max_len = int(max(max_len))
    range_expenditures = range(len(expenditures))
    total = sum(expenditures)
    
    for i in range_expenditures:
        expenditures[i] = 10 * int((expenditures[i]/total) * 10)
    
        
    chart = ''
    for i in range(100, -10, -10):
        line = ''
        chart += '\n'
        for k in range_expenditures:
            if expenditures[k] >= i:
                line += 'o  '
            else:
                line += '   '
        chart += f'{str(i).rjust(3)}| {line}'

    dashes = '\n    ' + '---' * len(expenditures) + '-' 

    line =''
    for i in range(max_len):
        x = ''
        for k in range(len(expenditures)):
            try:
                x += f'{departments[k][i]}  '
            except:
                x += '   '    
        
        line += f'\n     {x}'
        
    return f'{title}{chart}{dashes}{line}'