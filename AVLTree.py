# 平衡二叉搜索树的维护和旋转
from bst import BitreeNode, BST

# AVL的节点
class AVLNode(BitreeNode):
    def __init__(self, data):
        BitreeNode.__init__(self, data)

class AVLTree(BST):
    def __init__(self, li=None):
        BST.__init__(self, li)


    def rotate_left(self, p, c):
        s2 = c.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        c.lchild = p
        p.parent = c
        p.bf = 0
        c.bf = 0

        return c

    def rotate_right(self,p,c):
        s2 = c.rchild
        p.lchild = s2
        if s2:
            s2.parent = p
        c.rchild = p
        p.parent = c
        p.bf = 0
        c.bf = 0

        return c

    def rotate_right_left(self,p,c):
        g = c.lchild
        s3 = g.rchild
        c.lchild = s3
        if s3:
            s3.parent = c
        g.rchild = c
        c.parent = g

        s2 = g.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        g.lchild = p
        p.parent = g

        # 更新bf
        if g.bf > 0:
            p.bf = -1
            c.bf = 0
        elif g.bf < 0:
            p.bf = 0
            c.bf = 1
        else:
            c.bf = 0
            p.bf = 0

        return g

    def rotate_left_right(self, p, c):
        g = c.rchild
        s2 = g.lchild
        c.rchild = s2
        if s2:
            s2.parent = c
        g.lchild = c
        c.parent = g

        s3 = g.rchild
        p.lchild = s3
        if s3:
            s3.parent = p
        g.rchild = p
        p.parent = g

        # 更新bf
        if g.bf < 0:
            p.bf = 1
            c.bf = 0
        elif g.bf < 0:
            p.bf = 0
            c.bf = -1
        else:
            c.bf = 0
            p.bf = 0

        return g

    #   平衡二叉搜索树的插入与维护
    def insert_no_rec(self,val):
            p = self.root
            if not p:
                self.root = BitreeNode(val)
                return
            while True:
                if val<p.data:
                    if p.lchild:
                        p = p.lchild

                    else:
                        p.lchild = BitreeNode(val)
                        p.lchild.parent = p
                        node = p.lchild
                        break

                elif val>p.data:
                    if p.rchild:
                        p = p.rchild

                    else:
                        p.rchild = BitreeNode(val)
                        p.rchild.parent = p
                        node = p.rchild
                        break
                else:
                    return

            #2 更新bf
            while node.parent:
                if node.parent.lchild == node:  # 传递来自左子树
                    if node.parent.bf < 0:  # 原来bf等于-1,更新后为-2
                        g = node.parent.parent
                        x = node.parent     # 旋转前的子树的根
                        if node.bf > 0:
                            n = self.rotate_left_right(node.parent, node)
                        else:
                            n = self.rotate_left(node.parent, node)

                    elif node.parent.bf > 0:
                        node.parent.bf = 0
                        break
                    else:
                        node.parent.bf = -1
                        node = node.parent
                        continue

                else:   # 传递来自右子树
                    if node.parent.bf > 0:  # 原来bf等于1,更新后为2
                        g = node.parent.parent
                        x = node.parent  # 旋转前的子树的根
                        if node.bf < 0:
                            n = self.rotate_right_left(node.parent, node)
                        else:
                            n = self.rotate_right(node.parent, node)
                        # 把n和g连起来

                    elif node.parent.bf < 0:
                        node.parent.bf = 0
                        break
                    else:
                        node.parent.bf = 1
                        node = node.parent
                        continue
                # 把n和g连起来
                n.parent = g
                if g:
                    if x == g.lchild:
                        g.lchild = n
                    else:
                        g.rchild = n
                    break
                else:
                    self.root = n
                    break


tree = AVLTree([1,3,4,6,2,7])
tree.in_order(tree.root)
tree.insert_no_rec(9)
print("")
tree.in_order(tree.root)






