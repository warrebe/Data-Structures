# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        Adds element to heap
        :param node: element to add to heap
        :return: None
        """
        if self.is_empty():
            self.heap.append(node)
            return
        else:
            self.heap.append(node)
            index = (self.heap.length() - 1 - 1) // 2
            if self.heap[self.heap.length() - 1] < self.heap[index]:
                temp = self.heap[index]
                self.heap[index] = self.heap[self.heap.length() - 1]
                self.heap[self.heap.length() - 1] = temp
                if index == 0:
                    return
                else:
                    while index >= 1:
                        newNode = index
                        index = (index - 1) // 2
                        parent = self.heap[index]
                        if self.heap[newNode] < parent:
                            self.heap[index] = self.heap[newNode]
                            self.heap[newNode] = parent
                        else:
                            return

    def get_min(self) -> object:
        if self.is_empty():
            raise MinHeapException
        else:
            return self.heap[0]

    def remove_min(self) -> object:
        if self.is_empty():
            raise MinHeapException
        else:
            remove = self.heap[0]
            self.heap[0] = self.heap[self.heap.length() - 1]
            self.heap.pop()
            index = 0
            if self.is_empty():
                return remove
            while True:
                if not self.is_empty():
                    index1 = (2 * index + 1)
                    index2 = (2 * index + 2)
                    try:
                        self.heap[index1]
                    except DynamicArrayException:
                        try:
                            self.heap[index2]
                        except DynamicArrayException:
                            return remove
                    try:
                        if self.heap[index1] < self.heap[index2]:
                            child = index1
                        elif self.heap[index1] == self.heap[index2]:
                            child = index1
                        else:
                            child = index2
                    except DynamicArrayException:
                        child = index1
                    if self.heap[index] > self.heap[child]:
                        temp = self.heap[child]
                        self.heap[child] = self.heap[index]
                        self.heap[index] = temp
                        index = child
                    else:
                        return remove

    def build_heap(self, da: DynamicArray) -> None:
        self.heap = DynamicArray()
        for i in range(da.length()):
            self.heap.append(None)
        index = (da.length() - 2) // 2
        loop = True
        while index >= 0 and ((index * 2 + 1) < (da.length() - 1)):
            print(index)
            if not loop:
                if self.heap[index] < self.heap[index * 2 + 1]:
                    if self.heap[index] < self.heap[index * 2 + 2]:
                        index += 1
                        continue
            if da[index * 2 + 1] > da[index * 2 + 2]:
                child = index * 2 + 2
                if da[child] < da[index]:
                    self.heap[index] = da[child]
                    self.heap[index * 2 + 2] = da[index]
                    self.heap[index * 2 + 1] = da[index * 2 + 1]
                else:
                    self.heap[index] = da[index]
                    self.heap[index * 2 + 2] = da[index * 2 + 2]
                    self.heap[index * 2 + 1] = da[index * 2 + 1]
            else:
                child = index * 2 + 1
                if da[child] < da[index]:
                    self.heap[index] = da[child]
                    self.heap[index * 2 + 1] = da[index]
                    self.heap[index * 2 + 2] = da[index * 2 + 2]
                else:
                    self.heap[index] = da[index]
                    self.heap[index * 2 + 2] = da[index * 2 + 2]
                    self.heap[index * 2 + 1] = da[index * 2 + 1]
            if loop:
                index -= 1
            if index < 0:
                loop = False
                index = 0
            if not loop:
                index += 1

# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)


    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())


    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())


    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)
