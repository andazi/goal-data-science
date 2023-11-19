import datetime

class Diary:
      
    def __init__(self, filename):
        self._filename = filename
        # create new file r append to existing file
        self._diary = open(f"{self._filename}.txt", "w")
        # Title of Entries
        self._diary.write(f"\n\t\t{self._filename}\n\n")
        self._diary.write(f"Date Time \t\t entry \n\n")
        # always close file
        self.close_diary()
        
        self.todos = True
        # while loop that calls self.take_action function
        while self.todos == True:
            self.instruction = input('Enter instruction: add, read, close: \t').lower()
            self.take_action()
            
        
    def add_entry(self,entry):
        self.entry = entry
        # read current time in format (year-month-day, hour:minute)
        self.current_time = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M")
        # opening diary file
        self.open_diary()
        # entries
        self._diary.write(f"{self.current_time}\t {self.entry}\n\n")
        # close file
        self.close_diary()
    def read_diary(self):
        # read file
        self._diary = open(f"{self._filename}.txt", "r")
        print(self._diary.read())
        self.close_diary()
        
    def open_diary(self):
        self._diary =  open(f"{self._filename}.txt", "a")
    def close_diary(self):
        self._diary.close()
        
    def take_action(self):
        # conditonal statement
        if self.instruction == 'add':
            entry = input('Enter you entry: \t')
            self.add_entry(entry)
        if self.instruction == 'read':
            self.read_diary()
        if self.instruction == 'close':
            print(f"\n {self._filename} Diary closed")
            self.todos = False
        #elif self.instruction != 'add' or self.instruction != 'read' or self.instruction != 'close':
            #return 'Incorrect selection \n\n'

jamaica = Diary('Jaja diary')