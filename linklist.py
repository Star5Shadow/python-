# 链表的实现
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


def creat_linklist_head(li):
    head = Node(li[0])
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head

def creat_linklist_tail(li):
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head

def print_lk(lk):
    while lk:
        print(lk.item, end=",")
        lk = lk.next


lk = creat_linklist_tail([1, 2, 3, 5, 6, 6])
print_lk(lk)