A = [1,1,1,1,1]
point = 0
count = 0
for x in range(len(A)):
    if A[x]==1:
        count +=1
if count==len(A):
    point = 100
        
print(point)

for i in range(5):
    print("hello") #counter

#linked list->>>>>>>>>>>>>>>>>>>>>>>>...................>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class Node:
    def __init__(self, data):
        self.data = data  # Stores the value
        self.next = None  # Points to next node

class LinkedList:
    def __init__(self):
        self.head = None  # First node of the list

    def append(self, data):
        new_node = Node(data)
        if not self.head:        # Empty list
            self.head = new_node
            return
        current = self.head
        while current.next:      # Traverse to end
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()  # Output: 10 -> 20 -> 30 -> None
