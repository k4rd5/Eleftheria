class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    def display(self, list_=[], level=1):
        if self.left:
            level -= 1
            list_.append([])
            self.left.display(list_[level])
            level += 1
        list_.append(self.data)
        if self.right:
            level += 1
            list_.append([])
            self.right.display(list_[level])
            level -= 1

        return list_


root = Node(10)
root.left = Node(9)
root.left.left = Node(7)
root.left.right = Node(6)
root.left.left.left = Node(3)
root.right = Node(8)
root.right.left = Node(5)
root.right.right = Node(4)
print(root.display())
