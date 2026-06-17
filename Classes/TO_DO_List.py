counter = 0

class Task :
    def __init__(self , Time_Range = None , Subject = None , Description = None , Done = False):
        
        self.Time_Range:str = Time_Range
        self.Subject:str = Subject
        self.Description:str = Description
        self.done = Done
        
    def rem (self) :
        del self
        
    def show (self) :
        return self.Time_Range , self.Subject , self.Description
        
class To_Do :
    def __init__(self):
        self.cart = {}
        
    def add_new_task (self ,Time_Range , Subject , Description , Done):
        Task_ID = counter
        self.cart[Task_ID] = Task(Time_Range , Subject , Description , Done)
        
        counter += 1
        
    def rem (self,id):
        self.cart[id].rem()
        del self.cart[id]
              
    def show (self):
        return self.cart