class Todos():
    
    def __init__(self):
        self.todo_list = []
        self.completed_list = []
        print("Todo List ==> choose from various options below")

        self.actions = {
            "1" : 'add',
            "2" : 'remove',
            "3" : 'completed',
            "4" : 'show todos',
            "5" : 'show completed todo',
            "6" : 'exit'
        }
        print("Select specific number for action")
        for i in self.actions:
            print(i, self.actions[i])
        
        self.action = input("Enter action    ")
        
        # setActions loop
        while self.action != "6":
            
            self.setActions()
            for i in self.actions:
                print(i, self.actions[i])
            self.action = input("Enter action    ")
        
    # create a function that shows uncompleted todos and their index 
    def show(self):
        
        print('______TODO LISTS______')
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
        self.show()
    
    # create a function to remove todos
    def remove(self,ind):
        self.ind = ind
        if (self.ind <= len(self.todo_list)) and (self.ind >= 0):
            ind -= 1
            self.todo_list.pop(self.ind)
        else:
            print('Todo does not exist')  
        
        # show Todo List
        self.show()
            
    # create a function to complete todos
    def complete(self,ind):
        self.ind = ind
        if (self.ind <= len(self.todo_list)) and (self.ind >= 0):
            self.ind -= 1
            print(self.todo_list[self.ind], " => Mark as complete")
            self.completed_list.append(self.todo_list[self.ind])
            self.todo_list.pop(self.ind)
        else:
            print('Todo does not exist')
            
    # create a list to show completed todos
    # create a function that shows uncompleted todos and their index 
    def show_complete_todo(self):
        print('____Completed Todos_____')
        print('*' * 100)
        if len(self.completed_list) > 0:
            for ind,todo in enumerate(self.completed_list):
                ind += 1
                print(ind, '=>', todo)
        else:
            print('NO COMPLETED TODOS')
        print('*' * 100)
        
    def setActions(self):
     
        self.choice = self.actions[self.action]

        # issue here, need to read more on class on how to call a method inside a class
        if self.choice == self.actions['1']:
            addTodo = input('Write Todo:  ')
            self.add(addTodo)
        elif self.choice == self.actions['2']:
            self.show()
            removeTodo = int(input('Enter index of Todo to remove:    '))
            self.remove(removeTodo)
        elif self.choice == self.actions['3']:
            completeTodo = int(input('Enter index of todo you have completed:   '))
            self.complete(completeTodo)
        elif self.choice == self.actions['4']:
            self.show()
        elif self.choice == self.actions['5']:    
            self.show_complete_todo()
        else:
            print('Choose from 1 to 5')
        

oncscript = Todos()
