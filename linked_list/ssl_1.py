# defined a node
class Node:
    def __init__(self, item=None, next=None):
        self.item = item 
        self.next = next

# iterator class to make Sll class iterable        
class SllIterator:
    def __init__(self, start):
        self.current  = start
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data
    
class Sll:
    def __init__(self, start=None):
        self.start = start
    # pass instace to iterator to make iterable
    def __iter__(self):
        return SllIterator(self.start)
        
    def is_empty(self):
        return self.start == None

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' -> ')
            temp = temp.next
        print("Null")
                
    def insert_at_start(self,data):
        n = Node(data,self.start)
        self.start = n

    def insert_at_last(self,data):
        n = Node(data)
        if not self.is_empty():
            temp = self.start 
            while temp.next is not None:
                temp = temp.next 
            temp.next = n
        else:
            self.start = n 

    def search(self,data):
        if self.is_empty():
            print("Linked list is empty")
        temp = self.start 
        while temp.next is not None:
            if temp.item == data:
                return temp
            temp = temp.next 
        return None
    
    def insert_after_reference(self,temp,value):
        if temp is not None:
            n  = Node(value,temp.next)
            temp.next = n
            
    def insert_after_value(self,value,new_value):
        temp = self.search(value)
        if temp is not None:
            n  = Node(new_value,temp.next)
            temp.next = n
        
    def delete_start(self):
        if self.start is not None:
            self.start = self.start.next 
    
    def delete_last(self):
        if self.start is None:
            pass 
        elif self.start.next is None:
            self.start = None
        else: 
            temp = self.start 
            while temp.next.next is not None:
                temp = temp.next 
            temp.next = None

    def delete_item(self,data):
        if self.start is None:
            pass 
        elif self.start.next is None:
            if self.start.item == data:
                self.start = None
        else: 
            temp = self.start 
            if temp.item ==data: 
                self.start  = temp.next 
            else: 
                while temp.next is not None:
                    if temp.next.item == data :
                        temp.next = temp.next.next
                        break
                    temp = temp.next
            
            
            
        
    def get_count(self):
        if self.start is None:
            return 0 
        count  = 1
        temp = self.start
        while temp.next is not None:
            count = count + 1
            temp = temp.next
        return count
    
    def getNth(self, k):
        temp = self.start
        i=1
        while temp is not None:
            if (i == k):
                return temp.item
            temp = temp.next
            i = i+1

mylist = Sll()
mylist.insert_at_start(10)
mylist.insert_at_start(20)
mylist.insert_at_start(30)

mylist.insert_after_reference(mylist.search(20), 25)
mylist.insert_after_value(25,35)

# get count of linked list node
count = mylist.get_count()
print("Count: ",count)

# get item at index of linked list (1 indexing)
index = 3
data = mylist.getNth(index)
print(f"Data at index {index}: {data}")


mylist.print_list()

# mylist.delete_start()
# mylist.delete_last()
# mylist.delete_item(25)
# mylist.print_list()

# # make a class iterable
# for x in mylist:
#     print(x, end=' ')
