class BinarySearchTree:
    def __init__(self,data):
        self.left= None
        self.right= None
        self.data= data


    def add_child(self,data):
        if data == self.data:
            return 
        if data < self.data:
            # add to left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        
        else: 
            # add to righ subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right= BinarySearchTree(data)
        
    def in_order(self):
        elements = []

        if self.left:
            elements += self.left.in_order()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order()

        return elements
    
    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
         # might be in left sub tree
            if self.left: 
                return self.left.search(val)
            else: 
                return False
        if val > self.data: 
            # might be in right sub tree 
            if self.right:
                return self.right.search(val)
            else:
                return False
    def find_max(self):
        if self.right: 
            #return self.data
            return self.right.find_max()
        else: 
            return self.data 
    
    def find_min(self):
        if self.left:  
            return self.left.find_min()
        else: 
            return self.data 
    
    def calculate_sum(self):
        if self.left:
            left_sum = self.left.calculate_sum()
        else:
            left_sum =  0
        if self.right:
            right_sum = self.right.calculate_sum()
        else:
            right_sum = 0
        return  self.data + left_sum + right_sum
    
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self
            



def build_tree(elements):
    root= BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root 

if (__name__ =="__main__"):
    numbers = [17,4,1,20,9,23,18,34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order())
    print(numbers_tree.search(23))
    print(numbers_tree.calculate_sum())
    numbers_tree.delete(20)
    print(numbers_tree.in_order())


    
