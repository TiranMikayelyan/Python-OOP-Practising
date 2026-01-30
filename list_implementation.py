class List:
    def __init__(self):
        self.capacity = 2  #how many elements can be in the list
        self.size = 0      #how many elemnts are in list
        self.data = [None] * self.capacity #firstly whole array we will append None elements as our capacity is

    def append(self,value):
        if self.size == self.capacity: # if our array hasn't capacity , we will resize it
            self.resize()

        self.data[self.size] = value # when the last stage is okay, the new data will occupy his place in our list
        self.size+=1 # and our pointer will be show the new element
    def resize(self):
        print("Please wait: Resizing ...")

        new_capacity = self.capacity * 2 # the new capacity we give 2 time more
        new_data  = [None] * new_capacity # and append there None for taking memory

        for i in range(self.size): # doing loop for assigning new data to old
            new_data[i] = self.data[i]  # we copy the new datas only pointers not object

        self.data = new_data   # this means that we update old data address to new
        self.capacity = new_capacity # same as the last line
    

    def __getitem__(self, index):
        if index >= self.size: # if index is higher than size the will send a message about index error
            raise IndexError("Index out of range")
        else:
            return self.data[index] #otherwise it will give us the data
        
    def __len__(self):
        return self.size
    
    def __repr__(self):  # This help us to see all the object with correct form , not to see list object at 0x00...
        return str(self.data[:self.size]) # to convert a type to str, because repr method always return string
        

Mylist = List()

for i in range(10):
    Mylist.append(i)

    print(Mylist, "\nsize: ", len(Mylist), "\nCapacity", Mylist.capacity)
