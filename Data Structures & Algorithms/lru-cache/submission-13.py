class LRUCache:
    class Node:
        def __init__(self, key: int, val: int, prev=None, next=None):
            self.val = val
            self.key = key
            self.prev = prev
            self.next = next

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.length = 0
        self.nodeDict = {}

    def get(self, key: int) -> int:
        if key not in self.nodeDict:
            return -1
        
        node = self.nodeDict[key]

        if self.tail == node:
            return node.val
        
        # in end
        if self.head == node:
            # dettach
            self.head = node.next
            node.next.prev = None
            node.next = None

            # attach
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        # in the middle
        else:
            # dettach
            prev = node.prev
            prev.next = node.next
            node.next.prev = prev

            # attach
            node.prev = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node
            
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.nodeDict:
            self.get(key)
            self.nodeDict[key].val = value
        elif self.head is None:
            self.head = self.tail = self.Node(key, value)
            self.nodeDict[key] = self.head
            self.length = 1
        else:
            self.nodeDict[key] = new = self.Node(key, value)

            self.tail.next = new
            new.prev = self.tail
            self.tail = new
            self.length += 1

            if self.length > self.capacity:
                del self.nodeDict[self.head.key]

                self.head.next.prev = None
                self.head = self.head.next
                self.length -= 1
    
    def printList(self, head):
        temp = head
        print("*")
        while temp is not None:
            print(temp.val)
            temp = temp.next
        print("*")