# Course: CS261 - Data Structures
# Student Name: Benjamin Warren
# Assignment: Max Stack Dynamic Array
# Description: Creates a Max Stack ADT

from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class MaxStack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da_val = DynamicArray()
        self.da_max = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "MAX STACK: " + str(self.da_val.length()) + " elements. ["
        out += ', '.join([str(self.da_val[i]) for i in range(self.da_val.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da_val.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da_val.length()

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """
        Pushes value to top of stack (end of dynamic array)
        :param value: Element to add to top
        :return: None
        """
        self.da_val.append(value)
        try:
            if value >= self.da_max[self.da_max.length() - 1]:
                self.da_max.append(value)
        except Exception:
            self.da_max.append(value)

    def pop(self) -> object:
        """
        Removes element from top of stack (end of dynamic array)
        :return: Element removed
        """
        if self.da_val.length() == 0:
            raise StackException
        else:
            ret = self.da_val[self.da_val.length() - 1]
            if ret == self.da_max[self.da_max.length() - 1]:
                self.da_max.remove_at_index(self.da_max.length() - 1)
            self.da_val.remove_at_index(self.da_val.length() - 1)
            return ret

    def top(self) -> object:
        """
        Finds the element at the top of the stack
        :return: element at top of stakc
        """
        if self.da_val.length() == 0:
            raise StackException
        return self.da_val[self.da_val.length() - 1]

    def get_max(self) -> object:
        if self.da_val.length() == 0:
            raise StackException
        return self.da_max[self.da_max.length() - 1]


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# push example 1")
    s = MaxStack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)


    print("\n# pop example 1")
    s = MaxStack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))


    print("\n# top example 1")
    s = MaxStack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)
    

    print('\n# get_max example 1')
    s = MaxStack()
    for value in [1, -20, 15, 21, 21, 40, 50]:
        print(s, ' ', end='')
        try:
            print(s.get_max())
        except Exception as e:
            print(type(e))
        s.push(value)
    while not s.is_empty():
        print(s.size(), end='')
        print(' Pop value:', s.pop(), ' get_max after: ', end='')
        try:
            print(s.get_max())
        except Exception as e:
            print(type(e))

