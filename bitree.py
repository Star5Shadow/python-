# 二叉树的几种排序输出
from collections import deque

class BitreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


def pre_order(root):
    if root:
        print(root.data, end=",")
        pre_order(root.lchild)
        pre_order(root.rchild)


def in_order(root):
    if root:
        in_order(root.lchild)
        print(root.data, end=",")
        in_order(root.rchild)

def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end=",")


def level_order(root):
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        node = queue.popleft()
        print(node.data, end=",")
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)


a = BitreeNode("a")
b = BitreeNode("b")
c = BitreeNode("c")
d = BitreeNode("d")
e = BitreeNode("e")
e.lchild = a
e.rchild = b
b.rchild = c
b.lchild = d
root = e
level_order(root)