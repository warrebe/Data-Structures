# Course: CS261 - Data Structures
# Student Name: Benjamin Warren
# Assignment: Binary Search Tree
# Description: Implementing a binary search tree


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

    def pop(self) -> object:
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self) -> object:
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

    def dequeue(self) -> object:
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
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value          # to store node's data
        self.left = None            # pointer to root of left subtree
        self.right = None           # pointer to root of right subtree

    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self, start_tree=None) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using in-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "TREE pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # base case
        if not cur:
            return
        # store value of current node
        values.append(str(cur.value))
        # recursive case for left subtree
        self._str_helper(cur.left, values)
        # recursive case for right subtree
        self._str_helper(cur.right, values)

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        Call function for adding value to tree
        :param value: value to add
        :return: None
        """
        return self.rec_add(value, current = self.root)

    def rec_add(self, value, current):
        """
        Recursive add function
        :param value: value to add
        :param current: current node
        :return: None
        """
        if self.root is None:
            self.root = TreeNode(value)
            return
        if value >= current.value:
            if current.right is None:
                current.right = TreeNode(value)
                return
            else:
                current = current.right
        elif value < current.value:
            if current.left is None:
                current.left = TreeNode(value)
                return
            else:
                current = current.left
        return self.rec_add(value, current)

    def contains(self, value: object) -> bool:
        """
        Check to see if tree contains certain value
        :param value: value to check
        :return: Boolean on if value was found
        """
        current = self.root
        while True:
            if self.root is None:
                return False
            elif self.root.value == value:
                return True
            if value >= current.value:
                if current.right is None:
                    return False
                elif current.right.value == value:
                    return True
                else:
                    current = current.right
            else:
                if current.left is None:
                    return False
                elif current.left.value == value:
                    return True
                else:
                    current = current.left

    def get_first(self) -> object:
        """
        returns first node (root)
        :return: Root node
        """
        if self.root is None:
            return None
        return self.root.value

    def remove_first(self) -> bool:
        """
        Removes root value
        :return: Boolean if it was removed
        """
        cur = self.root
        if cur is None:
            return False
        if cur.right is None and cur.left is None:
            self.root = None
            return True
        if (self.root.right is not None) and (self.root.left is None):
            self.root = self.root.right
            return True
        elif self.root.right is not None:
            if self.root.right.left is not None:
                current = self.root.right
                if current.left.left is not None:
                    while current.left.left is not None:
                        current = current.left
                temp = self.root.right
                temp1 = self.root.left
                temp2 = current.left.right
                self.root = current.left
                self.root.right = temp
                self.root.left = temp1
                current.left = temp2
                return True
            else:
                temp = self.root.left
                self.root = self.root.right
                self.root.left = temp
                return True
        elif self.root.left is not None:
            self.root = self.root.left
            return True
        else:
            self.root = None
            return True

    def remove(self, value: object) -> bool:
        """
        Removes specified value
        :param value: Value to remove
        :return: Boolean if it was removed
        """
        cur = self.root
        if cur is None:
            return False
        if cur.right is None and cur.left is None:
            if cur.value is value:
                self.root = None
                return True
            else:
                return False
        if str(self.root.value) is str(value):
            if (self.root.right is not None) and (self.root.left is None):
                self.root = self.root.right
                return True
            elif self.root.right is not None:
                if self.root.right.left is not None:
                    current = self.root.right
                    if current.left.left is not None:
                        while current.left.left is not None:
                            current = current.left
                    temp = self.root.right
                    temp1 = self.root.left
                    temp2 = current.left.right
                    self.root = current.left
                    self.root.right = temp
                    self.root.left = temp1
                    current.left = temp2
                    return True
                else:
                    temp = self.root.left
                    self.root = self.root.right
                    self.root.left = temp
                    return True
            elif self.root.left is not None:
                self.root = self.root.left
                return True
            else:
                self.root = None
                return True
        while True:
            if cur is None:
                return False
            elif value > cur.value:
                print(str(value) + " Is greater than" + str(cur.value))
                if cur.right is None:
                    return False
                else:
                    if str(cur.right.value) is str(value):
                        if (cur.right.right is not None) and (cur.right.left is None):
                            cur.right = cur.right.right
                            return True
                        elif cur.right.right is not None:
                            if cur.right.right.left is not None:
                                current = cur.right.right
                                if current.left.left is not None:
                                    while current.left.left is not None:
                                        current = current.left
                                temp = cur.right.right
                                temp1 = cur.right.left
                                temp2 = current.left.right
                                cur.right = current.left
                                cur.right.right = temp
                                cur.right.left = temp1
                                current.left = temp2
                                return True
                            else:
                                temp = cur.right.left
                                cur.right = cur.right.right
                                cur.right.left = temp
                                return True
                        elif cur.right.left is not None:
                            cur.right = cur.right.left
                            return True
                        else:
                            cur.right = None
                            return True
                    else:
                        cur = cur.right
            elif value < cur.value:
                print(str(value) + " Is less than " + str(cur.value))
                if cur.left is None:
                    print("Hit")
                    return False
                else:
                    if str(cur.left.value) is str(value):
                        if (cur.left.right is not None) and (cur.left.left is None):
                            cur.left = cur.left.right
                            return True
                        elif cur.left.right is not None:
                            if cur.left.right.left is not None:
                                current = cur.left.right
                                if current.left.left is not None:
                                    while current.left.left is not None:
                                        current = current.left
                                temp = cur.left.left
                                temp1 = cur.left.right
                                temp2 = current.left.right
                                cur.left = current.left
                                cur.left.left = temp
                                cur.left.right = temp1
                                cur.left.right.left = temp2
                                return True
                            else:
                                temp = cur.left.left
                                cur.left = cur.left.right
                                cur.left.left = temp
                                return True
                        elif cur.left.left is not None:
                            cur.left = cur.left.left
                            return True
                        else:
                            cur.left = None
                            return True
                    else:
                        cur = cur.left
            else:
                print("Hit end")
                return False

    def pre_order_traversal(self) -> Queue:
        """
        Pre-order traversal function
        :return: Queue of traversal
        """
        newQueue = Queue()
        if self.root is None:
            return newQueue
        elif self.root.left is None:
            if self.root.right is None:
                newQueue.enqueue(self.root)
                return newQueue
        return self.rec_pre_order_traversal(self.root, newQueue)

    def rec_pre_order_traversal(self, cur, newQueue):
        """
        Recursive traversal for pre order
        :param cur: Current node
        :param newQueue: Queue return
        :return: Queue
        """
        if cur is not None:
            newQueue.enqueue(cur)
            self.rec_pre_order_traversal(cur.left, newQueue)
            self.rec_pre_order_traversal(cur.right, newQueue)
        return newQueue

    def in_order_traversal(self) -> Queue:
        """
        In order traversal function
        :return: Queue of traversal
        """
        newQueue = Queue()
        if self.root is None:
            return newQueue
        elif self.root.left is None:
            if self.root.right is None:
                newQueue.enqueue(self.root.value)
                return newQueue
        return self.rec_in_order_traversal(self.root, newQueue)

    def rec_in_order_traversal(self, cur, newQueue):
        """
        Recursive function for in order traversal
        :param cur: Current node
        :param newQueue: Return queue
        :return: queue
        """
        if cur is not None:
            self.rec_in_order_traversal(cur.left, newQueue)
            newQueue.enqueue(cur.value)
            self.rec_in_order_traversal(cur.right, newQueue)
        return newQueue

    def post_order_traversal(self) -> Queue:
        """
        Post order traversal method
        :return: Queue of traversal
        """
        newQueue = Queue()
        if self.root is None:
            return newQueue
        elif self.root.left is None:
            if self.root.right is None:
                newQueue.enqueue(self.root)
                return newQueue
        return self.rec_post_order_traversal(self.root, newQueue)

    def rec_post_order_traversal(self, cur, newQueue):
        """
        Recursive function for traversal
        :param cur: Current node
        :param newQueue: Q=Return queue
        :return: Queue
        """
        if cur is not None:
            self.rec_post_order_traversal(cur.left, newQueue)
            self.rec_post_order_traversal(cur.right, newQueue)
            newQueue.enqueue(cur)
        return newQueue

    def by_level_traversal(self) -> Queue:
        """
        By level traversal method
        :return: Queue of traversal
        """
        newQueue = Queue()
        if self.root is None:
            return newQueue
        elif self.root.left is None:
            if self.root.right is None:
                newQueue.enqueue(self.root)
                return newQueue
        return self.rec_by_level_traversal(self.root, newQueue)

    def rec_by_level_traversal(self, cur, newQueue):
        """
        Recursive function for by level traversal
        :param cur: Current node
        :param newQueue: Queue to return
        :return: Queue
        """
        height = self.rec_height(cur)
        for i in range(1, height + 1):
            self.current_level(cur, i, newQueue)
        return newQueue

    def rec_height(self, cur) -> int:
        """
        Returns the height of the tree by finding the longest subtree (Helper function
        :param cur: Current node
        :return: Height
        """
        if cur is None:
            return 0
        else:
            leftHeight = self.rec_height(cur.left)
            rightHeight = self.rec_height(cur.right)
            if leftHeight > rightHeight:
                return leftHeight + 1
            else:
                return rightHeight + 1

    def current_level(self, cur, level, newQueue):
        """
        Current level for by level traversal reference
        :param cur: Current node
        :param level: level on in tree
        :param newQueue: Queue to return
        :return: Queue
        """
        if cur is None:
            return
        if level == 1:
            newQueue.enqueue(cur.value)
        elif level > 1:
            self.current_level(cur.left, level - 1, newQueue)
            self.current_level(cur.right, level - 1, newQueue)

    def is_full(self) -> bool:
        """
        Checks to see if tree is full
        :return: Boolean
        """
        return self.rec_is_full(self.root)

    def rec_is_full(self, cur):
        """
        Recursive call for is full
        :param cur: Current node
        :return: Boolean
        """
        if cur is None:
            return True
        elif cur.right is None and cur.left is None:
            return True
        if cur.left is not None and cur.right is not None:
            return self.rec_is_full(cur.left) and self.rec_is_full(cur.right)
        return False

    def is_complete(self) -> bool:
        """
        Checks if tree is complete
        :return: Boolean
        """
        return self.rec_is_complete(self.root, 0, self.size())

    def rec_is_complete(self, cur, index, numNodes):
        """
        Recursive call for checking if tree is full
        :param cur: Current node
        :param index: Current index
        :param numNodes: Number of nodes
        :return: Boolean
        """
        if cur is None:
            return True
        if index >= numNodes:
            return False
        return (self.rec_is_complete(cur.left, 2 * index + 1, numNodes)
                    and self.rec_is_complete(cur.right, 2 * index + 2, numNodes))

    def is_perfect(self) -> bool:
        """
        Checks to see if a tree is perfect
        :return: Boolean
        """
        cur = self.root
        depth = 0
        while cur is not None:
            depth += 1
            cur = cur.left
        return self.rec_is_perfect(self.root, depth, 0)

    def rec_is_perfect(self, cur, depth, level):
        """
        recursive call for is perfect
        :param cur: Current node
        :param depth: Depth of tree
        :param level: Current level
        :return: Boolean
        """
        if cur is None:
            return True
        if cur.left is None and cur.right is None:
            return depth == level + 1
        if cur.left is None or cur.right is None:
            return False
        return (self.rec_is_perfect(cur.left, depth, level + 1) and
                self.rec_is_perfect(cur.right, depth, level + 1))

    def size(self) -> int:
        """
        returns size of tree
        :return:
        """
        return self.rec_size(self.root)

    def rec_size(self, cur):
        """
        recursive function to fin size
        :param cur: Current node
        :return: Int of size
        """
        if cur is None:
            return 0
        return 1 + self.rec_size(cur.left) + self.rec_size(cur.right)

    def height(self) -> int:
        """
        Finds height of tree using rec height
        :return: Int of height
        """
        if self.root is None:
            return -1
        elif self.root.right is None and self.root.left is None:
                return 0
        return self.rec_height(self.root) - 1

    def count_leaves(self) -> int:
        """
        Counts number of leaves in tree
        :return: Int of leaves
        """
        return self.rec_count_leaves(self.root)

    def rec_count_leaves(self, cur):
        """
        Counts leaves with recursion
        :param cur: Current node
        :return: Int number of leaves
        """
        if cur is None:
            return 0
        elif cur.left is None and cur.right is None:
            return 1
        else:
            return self.rec_count_leaves(cur.left) + self.rec_count_leaves(cur.right)

    def count_unique(self) -> int:
        """
        Counts unique values in tree
        :return: Int of unique values
        """
        # if self.root is None:
        #     return 0
        # elif self.root.left is None and self.root.right is None:
        #     return 1
        # newQueue = self.in_order_traversal()
        # newTree = BST()
        # while not newQueue.is_empty():
        #     value = newQueue.dequeue()
        #     newTree.add(value)
        # newQueue1 = newTree.in_order_traversal()
        # unique = 0
        # while not newQueue1.is_empty():
        #     unique += 1
        #     value = newQueue1.dequeue()
        #     remove = True
        #     while remove:
        #         remove = newTree.remove(value)
        # return unique
        return 0


# BASIC TESTING - PDF EXAMPLES

if __name__ == '__main__':
    # """ add() example #1 """
    # print("\nPDF - method add() example 1")
    # print("----------------------------")
    # tree = BST()
    # print(tree)
    # tree.add(10)
    # tree.add(15)
    # tree.add(5)
    # print(tree)
    # tree.add(15)
    # tree.add(15)
    # print(tree)
    # tree.add(5)
    # print(tree)
    #
    # """ add() example 2 """
    # print("\nPDF - method add() example 2")
    # print("----------------------------")
    # tree = BST()
    # tree.add(10)
    # tree.add(10)
    # print(tree)
    # tree.add(-1)
    # print(tree)
    # tree.add(5)
    # print(tree)
    # tree.add(-1)
    # print(tree)
    #
    # """ contains() example 1 """
    # print("\nPDF - method contains() example 1")
    # print("---------------------------------")
    # tree = BST([10, 5, 15])
    # print(tree.contains(15))
    # print(tree.contains(-10))
    # print(tree.contains(15))
    #
    # """ contains() example 2 """
    # print("\nPDF - method contains() example 2")
    # print("---------------------------------")
    # tree = BST()
    # print(tree.contains(0))
    #
    # """ get_first() example 1 """
    # print("\nPDF - method get_first() example 1")
    # print("----------------------------------")
    # tree = BST()
    # print(tree.get_first())
    # tree.add(10)
    # tree.add(15)
    # tree.add(5)
    # print(tree.get_first())
    # print(tree)
    #
    """ remove() example 1 """
    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    tree = BST([10, 5, 15])
    print(tree.remove(7))
    print(tree.remove(15))
    print(tree.remove(15))

    """ remove() example 2 """
    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.remove(20))
    print(tree)

    """ remove() example 3 """
    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    tree = BST([10, 5, 20, 18, 12, 7, 27, 22, 18, 24, 22, 30])
    print(tree.remove(20))
    print(tree)
    # comment out the following lines
    # if you have not yet implemented traversal methods
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())

    """ remove_first() example 1 """
    print("\nPDF - method remove_first() example 1")
    print("-------------------------------------")
    tree = BST([20, 5, 7])
    print(tree.remove_first())
    print(tree)

    """ remove_first() example 2 """
    print("\nPDF - method remove_first() example 2")
    print("-------------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7])
    print(tree.remove_first())
    print(tree)

    """ remove_first() example 3 """
    print("\nPDF - method remove_first() example 3")
    print("-------------------------------------")
    tree = BST([10, 10, -1, 5, -1])
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    print(tree.remove_first(), tree)
    #
    # """ Traversal methods example 1 """
    # print("\nPDF - traversal methods example 1")
    # print("---------------------------------")
    # tree = BST([10, 20, 5, 15, 17, 7, 12])
    # print(tree.pre_order_traversal())
    # print(tree.in_order_traversal())
    # print(tree.post_order_traversal())
    # print(tree.by_level_traversal())
    #
    # """ Traversal methods example 2 """
    # print("\nPDF - traversal methods example 2")
    # print("---------------------------------")
    # tree = BST([10, 10, -1, 5, -1])
    # print(tree.pre_order_traversal())
    # print(tree.in_order_traversal())
    # print(tree.post_order_traversal())
    # print(tree.by_level_traversal())
    #
    # """ Comprehensive example 1 """
    # print("\nComprehensive example 1")
    # print("-----------------------")
    # tree = BST()
    # header = 'Value   Size  Height   Leaves   Unique   '
    # header += 'Complete?  Full?    Perfect?'
    # print(header)
    # print('-' * len(header))
    # print(f'  N/A {tree.size():6} {tree.height():7} ',
    #       f'{tree.count_leaves():7} {tree.count_unique():8}  ',
    #       f'{str(tree.is_complete()):10}',
    #       f'{str(tree.is_full()):7} ',
    #       f'{str(tree.is_perfect())}')
    #
    # for value in [10, 5, 3, 15, 12, 8, 20, 1, 4, 9, 7]:
    #     tree.add(value)
    #     print(f'{value:5} {tree.size():6} {tree.height():7} ',
    #           f'{tree.count_leaves():7} {tree.count_unique():8}  ',
    #           f'{str(tree.is_complete()):10}',
    #           f'{str(tree.is_full()):7} ',
    #           f'{str(tree.is_perfect())}')
    # print()
    # print(tree.pre_order_traversal())
    # print(tree.in_order_traversal())
    # print(tree.post_order_traversal())
    # print(tree.by_level_traversal())
    #
    # """ Comprehensive example 2 """
    # print("\nComprehensive example 2")
    # print("-----------------------")
    # tree = BST()
    # header = 'Value   Size  Height   Leaves   Unique   '
    # header += 'Complete?  Full?    Perfect?'
    # print(header)
    # print('-' * len(header))
    # print(f'N/A   {tree.size():6} {tree.height():7} ',
    #       f'{tree.count_leaves():7} {tree.count_unique():8}  ',
    #       f'{str(tree.is_complete()):10}',
    #       f'{str(tree.is_full()):7} ',
    #       f'{str(tree.is_perfect())}')
    #
    # for value in 'DATA STRUCTURES':
    #     tree.add(value)
    #     print(f'{value:5} {tree.size():6} {tree.height():7} ',
    #           f'{tree.count_leaves():7} {tree.count_unique():8}  ',
    #           f'{str(tree.is_complete()):10}',
    #           f'{str(tree.is_full()):7} ',
    #           f'{str(tree.is_perfect())}')
    # print('', tree.pre_order_traversal(), tree.in_order_traversal(),
    #       tree.post_order_traversal(), tree.by_level_traversal(),
    #       sep='\n')

