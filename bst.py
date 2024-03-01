# 二叉搜索树的插入与维护
class BitreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None
        self.bf = 0

class BST:
    def __init__(self, li=None):
        self.root = None
        if li:
            self.root = BitreeNode(li[0])
            for val in li:
                self.insert(self.root, val)

    def query_no_rec(self,val):
        p = self.root
        while p:
            if p.data < val:
                p = p.rchild
            if p.data > val:
                p = p.lchild
            else:
                return p
        return None


    def insert(self, node, val):
        if not node:
            node = BitreeNode(val)
        elif val < node.data:
            node.lchild = self.insert(node.lchild, val)
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert(node.rchild, val)
            node.rchild.parent = node
        return node

    def pre_order(self, root):
        if root:
            print(root.data, end=",")
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    def in_order(self, root):
        if root:
            self.in_order(root.lchild)
            print(root.data, end=",")
            self.in_order(root.rchild)

    def post_order(self, root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end=",")


    def _remove_node_1(self, node):      # node是叶子节点
        if not node.parent:
            self.root = None
        if node == node.parent.lchild:
            node.parent.lchild = None
        else:
            node.parent.rchild = None

    def _remove_node_21(self, node):    # 只有一个左孩子
        if not node.parent:
            self.root = node.lchild
            node.lchild.parent = None
        elif node == node.parent.lchild:
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent
        else:
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    def _remove_node_22(self, node):
        if not node.parent:
            self.root = node.rchild
            node.lchild.parent = None
        elif node == node.parent.lchild:
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        else:
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent

    def delete(self, val):
        if self.root:
            node = self.query_no_rec(val)
            if not node:
                return False
            if not node.lchild and not node.rchild:
                self._remove_node_1(node)
            elif not node.rchild:
                self._remove_node_21(node)
            elif not node.lchild:
                self._remove_node_22(node)
            else:
                min_node = node.rchild
                while min_node.lchild:
                    min_node = min_node.lchild
                node.data = min_node.data
                if min_node.rchild:
                    self._remove_node_22(min_node)
                else:
                    self._remove_node_1(min_node)


# tree = BST([2, 5, 6, 4, 3])
# tree.in_order(tree.root)
# print("")
# tree.delete(4)
# tree.in_order(tree.root)