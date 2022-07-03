class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self,val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self
    
    def print_values(self):
        runner = self.head
        while(runner != None):
            print(runner.val)
            runner = runner.next
        return self

    def add_to_back(self, val):
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self

    def remove_from_front(self):
        new_head = self.head.next
        self.head = new_head
        return self

    def remove_from_back(self):
        temp = self.head
        cur = temp.next
        while (cur != None):
            if(cur.next == None):
                temp.next = None
            temp = cur
            cur = cur.next
        if cur == None:
            self.head = None
        return self
    
  

class SLNode:
    def __init__(self,val):
        self.next = None
        self.val = val


my_list = SList()	# create a new instance of a list
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").remove_from_back().print_values()
# output should be:
# Linked lists
# are
# fun!

