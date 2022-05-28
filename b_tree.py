class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    def insert(self, val):
        if val < self.val:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        elif val > self.val:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.insert(val)
    def search(self, val):
        if self.left is not None:
            if val < self.left.val:
                self.left.search(val)
            elif val == self.left.val:
                return self.left.val
        if self.right is not None:
            if val > self.right.val:
                self.right.search(val)
            elif val == self.right.val:
                return self.right.val
    def output(self,indentation = 0):
        if self.left:
            self.left.output(indentation + 1)
        for _ in range(indentation):
            print('\t',end='')
        print(self.val)
        if self.right:
            self.right.output(indentation + 1)
    def clear(self):
        self.left = None
        self.right = None
