# create a list to contain the todos
# create a function to add todos
# create a function to remove todos
# create a function to complete todos
# create a function to add todos
# create a list to show completed todos
# create a function to clear list

class Todos():
    
    def __init__(self):
        self.todo_list = []
        self.completed_list = []
        
    # create a function that shows uncompleted todos and their index 
    def show(self):
        print('Todo List')
        print('*' * 100)
        for ind,todo in enumerate(self.todo_list):
            ind += 1
            print(ind, '=>', todo)
        print('*' * 100)    
    # create a function to add todos
    def add(self,todo):
        self.todo = todo
        self.todo_list.append(self.todo)  
        
        # alway show Todo list
       # show()
    
    # create a function to remove todos
    def remove(self,ind):
        self.ind = ind
        if (self.ind <= len(self.todo_list)) and (self.ind >= 0):
            ind -= 1
            self.todo_list.pop(self.ind)
        else:
            print('Todo does not exist')  
            
    # create a function to complete todos
    def complete(self,ind):
        self.ind = ind
        if (self.ind <= len(self.todo_list)) and (self.ind >= 0):
            self.ind -= 1
            print(f'{self.todo_list[self.ind]} =>is now complete')
            self.completed_list.append(self.todo_list[self.ind])
            self.todo_list.pop(self.ind)
        else:
            print('Todo does not exist')
            
    # create a list to show completed todos
    # create a function that shows uncompleted todos and their index 
    def show_complete_todo(self):
        print('Completed Todos')
        print('*' * 100)
        for ind,todo in enumerate(self.completed_list):
            ind += 1
            print(ind, '=>', todo)
        print('*' * 100)
        
chrisTodos = Todos()

chrisTodos.add('Write 62 lines of python code')
chrisTodos.add('Git push my codes to guthub')
chrisTodos.add('Watch kdrama before sleeping')
chrisTodos.add('Cook fanatastic meal')

chrisTodos.show()

chrisTodos.complete(1)

chrisTodos.show()