counter = 0

class Task:
    def __init__(self, Time_Range=None, Subject=None, Description=None ,taskID=None):
        self.taskID = taskID
        self.Time_Range = Time_Range
        self.Subject = Subject
        self.Description = Description
        self.done = False

    def show(self):
        return self.Time_Range, self.Subject, self.Description

class To_Do:
    def __init__(self):
        self.cart = {}

    def add_new_task(self, Time_Range, Subject, Description):
        global counter
        self.cart[counter] = Task(Time_Range, Subject, Description , taskID=counter)
        counter += 1

    def rem(self, id):
        del self.cart[id]

    def show(self):
        return self.cart