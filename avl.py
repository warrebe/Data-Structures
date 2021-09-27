# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:


import random


class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty stack based on Python list """
        self._data = []

    def push(self, value: object) -> None:
        """ Add new element on top of the stack """
        self._data.append(value)

    def pop(self):
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self):
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"


class Queue:
    """
    Class implementing QUEUE ADT.
    Supported methods are: enqueue, dequeue, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """ Initialize empty queue based on Python list """
        self._data = []

    def enqueue(self, value: object) -> None:
        """ Add new element to the end of the queue """
        self._data.append(value)

    def dequeue(self):
        """ Remove element from the beginning of the queue and return its value """
        return self._data.pop(0)

    def is_empty(self):
        """ Return True if the queue is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"


class TreeNode:
    """
    AVL Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Initialize a new AVL node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0

    def __str__(self):
        return 'AVL Node: {}'.format(self.value)


# noinspection PyDefaultArgument,PyTypeChecker
class AVL:
    def __init__(self, start_tree=None) -> None:
        """
        Initialize a new AVL tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate AVL with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of AVL in human-readable form using pre-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "AVL pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if cur:
            values.append(str(cur.value))
            self._str_helper(cur.left, values)
            self._str_helper(cur.right, values)

    def is_valid_avl(self) -> bool:
        """
        Perform pre-order traversal of the tree. Return False if there
        are any problems with attributes of any of the nodes in the tree.

        This is intended to be a troubleshooting 'helper' method to help
        find any inconsistencies in the tree after the add() or remove()
        operations. Review the code to understand what this method is
        checking and how it determines whether the AVL tree is correct.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        s = Stack()
        s.push(self.root)
        while not s.is_empty():
            node = s.pop()
            if node:
                # check for correct height (relative to children)
                l = node.left.height if node.left else -1
                r = node.right.height if node.right else -1
                if node.height != 1 + max(l, r):
                    return False

                if node.parent:
                    # parent and child pointers are in sync
                    if node.value < node.parent.value:
                        check_node = node.parent.left
                    else:
                        check_node = node.parent.right
                    if check_node != node:
                        return False
                else:
                    # NULL parent is only allowed on the root of the tree
                    if node != self.root:
                        return False
                s.push(node.right)
                s.push(node.left)
        return True

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        Call function for adding value to tree
        :param value: value to add
        :return: None
        """
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self.rec_add(value, self.root)

    def rec_add(self, value, current):
        """
        Recursive function for adding values to tree
        :param value: value to add
        :param current: current node in tree
        :return: None
        """
        if value < current.value:
            if current.left is None:
                current.left = TreeNode(value)
                current.left.parent = current
                self.inspect_insertion(current.left)
            else:
                self.rec_add(value, current.left)
        if value > current.value:
            if current.right is None:
                current.right = TreeNode(value)
                current.right.parent = current
                self.inspect_insertion(current.right)
            else:
                self.rec_add(value, current.right)

    def remove(self, value: object) -> bool:
        """
        Removes specified value
        :param value: Value to remove
        :return: Boolean if it was removed
        """
        if self.root.value is value:
            if self.root.height == 0:
                self.root = None
                return True
        return self.remove_node(self.find(value))

    def remove_node(self, node):
        """
        Recursive function for removing a node
        :param node: Current node
        :return: Boolean on whether it was removed
        """
        if node is None or self.find(node.value) is None:
            return False
        def min_value(node):
            """
            Finds the leftmost child of the right subtree of node
            :param node: Given node
            :return: mivVal
            """
            current = node
            while current.left is not None:
                current = current.left
            return current
        def num_children(node):
            """
            Gives number of children of a given node
            :param node: Node to check
            :return: Number of children of node
            """
            num_children = 0
            if node.left is not None:
                num_children += 1
            if node.right is not None:
                num_children += 1
            return num_children
        parentNode = node.parent
        childNode = num_children(node)
        if childNode == 0:
            if parentNode is not None:
                if parentNode.left is node:
                    parentNode.left = None
                else:
                    parentNode.right = None
        if childNode == 1:
            if node.left is not None:
                child = node.left
            else:
                child = node.right
            if parentNode is not None:
                if parentNode.left is node:
                    parentNode.left = child
                else:
                    parentNode.right = child
            else:
                self.root = child
            child.parent = parentNode
        if childNode == 2:
            successor = min_value(node.right)
            node.value = successor.value
            self.remove_node(successor)
            return True
        if parentNode is not None:
            parentNode.height = 1 + max(self.get_height(parentNode.left), self.get_height(parentNode.right))
            self.inspect_deletion(parentNode)
        return True

    def find(self, value):
        """
        Finds node containing value
        :param value: Value to find
        :return: Found node
        """
        if self.root is not None:
            return self.rec_find(value, self.root)
        else:
            return None

    def rec_find(self, value, current):
        """
        Recursive call for find
        :param value: value to find
        :param current: node found
        :return:
        """
        if value == current.value:
            return current
        elif value < current.value and current.left is not None:
            return self.rec_find(value, current.left)
        elif value > current.value and current.right is not None:
            return self.rec_find(value, current.right)

    def inspect_insertion(self, current, path = Stack()):
        """
        Check function after inserting value to see if balancing is needed
        :param current: current node
        :param path: path of checked nodes for balancing(stack)
        :return: None
        """
        if current.parent is None:
            return
        path.push(current)
        leftHeight = self.get_height(current.parent.left)
        rightHeight = self.get_height(current.parent.right)
        if abs(leftHeight - rightHeight) > 1:
            path.push(current.parent)
            self.balance(path.pop(), path.pop(), path.pop())
            return
        newHeight = 1 + current.height
        if newHeight > current.parent.height:
            current.parent.height = newHeight
        self.inspect_insertion(current.parent, path)

    def inspect_deletion(self, current):
        """
        Check function after removing value to see if balancing is needed
        :param current: current node
        :return: None
        """
        if current is None:
            return
        leftHeight = self.get_height(current.left)
        rightHeight = self.get_height(current.right)
        if abs(leftHeight - rightHeight) > 1:
            y = self.taller_child(current)
            x = self.taller_child(y)
            self.balance(current, y, x)
        self.inspect_deletion(current.parent)

    def balance(self, z, y, x):
        """
        Balancing function based on canvas exploration module
        :param z: Z node
        :param y: Y node
        :param x: X node
        :return: None
        """
        if y is z.left and x is y.left:
            self.right_rotation(z)
        elif y is z.left and x is y.right:
            self.left_rotation(y)
            self.right_rotation(z)
        elif y is z.right and x is y.right:
            self.left_rotation(z)
        elif y is z.right and x is y.left:
            self.right_rotation(y)
            self.left_rotation(z)

    def right_rotation(self, z):
        """
        Function for performing right rotation of node group
        :param z: Z node for rotation centering
        :return: None
        """
        subRoot = z.parent
        y = z.left
        leaf = y.right
        y.right = z
        z.parent = y
        z.left = leaf
        if leaf is not None:
            leaf.parent = z
        y.parent = subRoot
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is z:
                y.parent.left = y
            else:
                y.parent.right = y
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

    def left_rotation(self, z):
        """
        Function for performing left rotation of node group
        :param z: Z node for rotation centering
        :return: None
        """
        subRoot = z.parent
        y = z.right
        leaf = y.left
        y.left = z
        z.parent = y
        z.right = leaf
        if leaf is not None:
            leaf.parent = z
        y.parent = subRoot
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is z:
                y.parent.left = y
            else:
                y.parent.right = y
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

    @staticmethod
    def get_height(current):
        """
        Gets height of current node, if not a node returns -1
        :param current: node to return
        :return: node height
        """
        if current is None:
            return -1
        return current.height

    def taller_child(self, current):
        """
        Function for removing node, returns tallest child node of a node
        :param current: parent node
        :return: Tallest child
        """
        left = self.get_height(current.left)
        right = self.get_height(current.right)
        if left >= right:
            return current.left
        else:
            return current.right

# ------------------- BASIC TESTING -------- ---------------------------------


if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (34, 16, 30, 78, 50, 82, 48, 62),  # RR
    )
    for case in test_cases:
        avl = AVL(case)
    avl.remove(30)
    avl.remove(82)
    print(avl.root)


    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),   # RR, RR
        (10, 20, 30, 50, 40),   # RR, RL
        (30, 20, 10, 5, 1),     # LL, LL
        (30, 20, 10, 1, 5),     # LL, LR
        (5, 4, 6, 3, 7, 2, 8),  # LL, RR
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        avl = AVL(case)
        print('INPUT  :', case)
        print('RESULT :', avl)

    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        avl = AVL()
        for value in case:
            avl.add(value)
        if not avl.is_valid_avl():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')

    # print("\nPDF - method remove() example 1")
    # print("-------------------------------")
    # test_cases = (
    #     ((1, 2, 3), 1),  # no AVL rotation
    #     ((1, 2, 3), 2),  # no AVL rotation
    #     ((1, 2, 3), 3),  # no AVL rotation
    #     ((50, 40, 60, 30, 70, 20, 80, 45), 0),
    #     ((50, 40, 60, 30, 70, 20, 80, 45), 45),  # no AVL rotation
    #     ((50, 40, 60, 30, 70, 20, 80, 45), 40),  # no AVL rotation
    #     ((50, 40, 60, 30, 70, 20, 80, 45), 30),  # no AVL rotation
    # )
    # for tree, del_value in test_cases:
    #     avl = AVL(tree)
    #     print('INPUT  :', avl, "DEL:", del_value)
    #     avl.remove(del_value)
    #     print('RESULT :', avl)
    #
    # print("\nPDF - method remove() example 2")
    # print("-------------------------------")
    # test_cases = (
    #     ((50, 40, 60, 30, 70, 20, 80, 45), 20),  # RR
    #     ((50, 40, 60, 30, 70, 20, 80, 15), 40),  # LL
    #     ((50, 40, 60, 30, 70, 20, 80, 35), 20),  # RL
    #     ((50, 40, 60, 30, 70, 20, 80, 25), 40),  # LR
    # )
    # for tree, del_value in test_cases:
    #     avl = AVL(tree)
    #     print('INPUT  :', avl, "DEL:", del_value)
    #     avl.remove(del_value)
    #     print('RESULT :', avl)
    #
    # print("\nPDF - method remove() example 3")
    # print("-------------------------------")
    # case = range(-9, 16, 2)
    # avl = AVL(case)
    # for del_value in case:
    #     print('INPUT  :', avl, del_value)
    #     avl.remove(del_value)
    #     print('RESULT :', avl)
    # print(avl.is_valid_avl())
    #
    # print("\nPDF - method remove() example 4")
    # print("-------------------------------")
    # case = range(0, 34, 3)
    # avl = AVL(case)
    # for _ in case[:-2]:
    #     print('INPUT  :', avl, avl.root.value)
    #     avl.remove(avl.root.value)
    #     print('RESULT :', avl)
    #     print(avl.is_valid_avl())
    #
    # print("\nPDF - method remove() example 5")
    # print("-------------------------------")
    # for _ in range(100):
    #     case = list(set(random.randrange(1, 20000) for _ in range(900)))
    #     avl = AVL(case)
    #     for value in case[::2]:
    #         avl.remove(value)
    #     if not avl.is_valid_avl():
    #         raise Exception("PROBLEM WITH REMOVE OPERATION")
    # print('remove() stress test finished')
