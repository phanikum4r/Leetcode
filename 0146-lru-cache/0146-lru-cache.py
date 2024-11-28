# class Node:
#     def __init__(self,key):
#         self.val=key
#         self.prev=None
#         self.next=None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache=OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key]=value
        if len(self.cache)>self.capacity:
            self.cache.popitem(0)
        
    
    # using double linked list
    
    # def __init__(self, capacity: int):
    #     self.capacity = capacity
    #     self.dic = {}
    #     self.head = ListNode(-1, -1)
    #     self.tail = ListNode(-1, -1)
    #     self.head.next = self.tail
    #     self.tail.prev = self.head

    # def get(self, key: int) -> int:
    #     if key not in self.dic:
    #         return -1

    #     node = self.dic[key]
    #     self.remove(node)
    #     self.add(node)
    #     return node.val

    # def put(self, key: int, value: int) -> None:
    #     if key in self.dic:
    #         old_node = self.dic[key]
    #         self.remove(old_node)

    #     node = ListNode(key, value)
    #     self.dic[key] = node
    #     self.add(node)

    #     if len(self.dic) > self.capacity:
    #         node_to_delete = self.head.next
    #         self.remove(node_to_delete)
    #         del self.dic[node_to_delete.key]

    # def add(self, node):
    #     previous_end = self.tail.prev
    #     previous_end.next = node
    #     node.prev = previous_end
    #     node.next = self.tail
    #     self.tail.prev = node

    # def remove(self, node):
    #     node.prev.next = node.next
    #     node.next.prev = node.prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)