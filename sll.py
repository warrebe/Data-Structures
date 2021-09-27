# Course: CS261 - Data Structures
# Student Name: Benjamin Warren
# Assignment: Singly Linked List
# Description: A Linked list with a back and front sentinel



class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class SLNode:
    """
    Singly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with front and back sentinels
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.head = SLNode(None)
        self.tail = SLNode(None)
        self.head.next = self.tail

        # populate SLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        if self.head.next != self.tail:
            cur = self.head.next.next
            out = out + str(self.head.next.value)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        cur = self.head
        while cur.next != self.tail:
            cur = cur.next
            length += 1
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.head.next == self.tail

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        Adds value to front of list
        :param value: value to add
        :return: None
        """
        temp = self.head.next
        self.head.next = SLNode(value)
        self.head.next.next = temp

    def add_back(self, value: object) -> None:
        """
        Adds value to back of list
        :param value: Value to add
        :return: None
        """
        self.rec_add_back(value, self.head)

    def rec_add_back(self, value: object, current) -> None:
        """
        Recursive function for add_back
        :param value: Value to add
        :param current: Current node
        :return: None
        """
        if current.next is self.tail:
            current.next = SLNode(value)
            current.next.next = self.tail
            return
        current = current.next
        return self.rec_add_back(value, current)

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Inserts value at index in list
        :param index: Index
        :param value: value to add
        :return: None
        """
        self.rec_insert_at_index(index, value, current = self.head, counter = 0)

    def rec_insert_at_index(self, index: int, value: object, current, counter) -> None:
        """
        Recursive function for insert at index
        :param index: index
        :param value: value to add
        :param current: current node
        :param counter: rec counter
        :return: None
        """
        if index == 0:
            self.add_front(value)
            return
        if index < 0:
            raise SLLException
        if index > self.length():
            raise SLLException
        if current.next.value is not None:
            if counter < index:
                current = current.next
                counter += 1
                return self.rec_insert_at_index(index, value, current, counter)
        temp = current.next
        current.next = SLNode(value)
        current.next.next = temp
        return

    def remove_front(self) -> None:
        """
        Remove the node at the front
        :return: None
        """
        if self.is_empty():
            raise SLLException
        self.head.next = self.head.next.next

    def remove_back(self) -> None:
        """
        Remove node at back
        :return: None
        """
        self.rec_remove_back(self.head)

    def rec_remove_back(self, current) -> None:
        """
        Recursive function for remove_back
        :param current: current node
        :return: None
        """
        if self.is_empty():
            raise SLLException
        if current.next.next is self.tail:
            current.next = self.tail
            return
        current = current.next
        return self.rec_remove_back(current)

    def remove_at_index(self, index: int) -> None:
        """
        Removes node at index
        :param index: Index to remove
        :return: None
        """
        self.rec_remove_at_index(index, current = self.head, counter = 0)

    def rec_remove_at_index(self, index: int, current, counter) -> None:
        """
        Recursive function for remove at index
        :param index: Index
        :param current: Current node
        :param counter: Rec counter
        :return: None
        """
        if index == 0:
            self.remove_front()
            return
        if index < 0 or index > (self.length() - 1) or self.is_empty():
            raise SLLException
        if current.next.value is not None:
            if counter < index:
                if current.next.value is None:
                    return
                current = current.next
                counter += 1
                return self.rec_remove_at_index(index, current, counter)
            current.next = current.next.next

    def get_front(self) -> object:
        """
        Gets front node
        :return: Front node
        """
        if self.is_empty():
            raise SLLException
        return self.head.next.value

    def get_back(self)  -> object:
        """
        Gets back Node
        :return: Back node
        """
        return self.rec_get_back(self.head)

    def rec_get_back(self, current):
        """
        Recursive function for get_back
        :param current: current node
        :return: None
        """
        if self.is_empty():
            raise SLLException
        if current.next.next is self.tail:
            return current.next.value
        current = current.next
        return self.rec_get_back(current)

    def remove(self, value: object) -> bool:
        """
        Removes first node containing a certain value
        :param value: value to remove
        :return: Boolean on whether something was removed
        """
        return self.rec_remove(value, self.head)

    def rec_remove(self, value, current):
        """
        Recursive function for remove
        :param value: value to remove
        :param current: current node
        :return: Boolean on whether value was removed
        """
        if current.next == self.tail:
            return False
        if current.next.value == value:
            current.next = current.next.next
            return True
        current = current.next
        return self.rec_remove(value, current)

    def count(self, value: object) -> int:
        """
        Counts occurrence of value
        :param value: value to count
        :return: Number of occurences
        """
        return self.rec_count(value, 0, self.head)

    def rec_count(self, value, counter, current):
        """
        Recursive function for count
        :param value: Value to count
        :param counter: Counted
        :param current: Current node
        :return: count
        """
        if self.length() == 0:
            return 0
        if current != self.tail:
            if current.value == value:
                counter += 1
            current = current.next
            return self.rec_count(value, counter, current)
        return counter

    def slice(self, start_index: int, size: int) -> object:
        """
        Slices list
        :param start_index: start of slice
        :param size: size of slice to make
        :return: new list
        """
        if start_index >= self.length() or start_index < 0 or size < 0:
            raise SLLException
        if start_index + size > self.length():
            raise SLLException
        if size == 0:
            return LinkedList()
        else:
            newLL = LinkedList()
            return self.rec_slice(start_index, size, self.head, 0, newLL)

    def rec_slice(self, start_index, size, current, counter, newLL):
        """
        Recursive function for slice
        :param start_index: index to start slice
        :param size: size of slice
        :param current: current node
        :param counter: count of recursion
        :param newLL: new sliced list to return
        :return: new list
        """
        if start_index < counter < (start_index + size + 1):
            newLL.add_back(current.value)
            if current.next == self.tail:
                return newLL
            current = current.next
            counter += 1
            return self.rec_slice(start_index, size, current, counter, newLL)
        elif counter > start_index + size:
            return newLL
        else:
            current = current.next
            counter += 1
            return self.rec_slice(start_index, size, current, counter, newLL)



if __name__ == '__main__':
    pass

    print('\n# add_front example 1')
    list = LinkedList()
    print(list)
    list.add_front('A')
    list.add_front('B')
    list.add_front('C')
    print(list)


    print('\n# add_back example 1')
    list = LinkedList()
    print(list)
    list.add_back('C')
    list.add_back('B')
    list.add_back('A')
    print(list)


    print('\n# insert_at_index example 1')
    list = LinkedList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            list.insert_at_index(index, value)
            print(list)
        except Exception as e:
            print(type(e))


    print('\n# remove_front example 1')
    list = LinkedList([1, 2])
    print(list)
    for i in range(3):
        try:
            list.remove_front()
            print('Successful removal', list)
        except Exception as e:
            print(type(e))


    print('\n# remove_back example 1')
    list = LinkedList()
    try:
        list.remove_back()
    except Exception as e:
        print(type(e))
    list.add_front('Z')
    list.remove_back()
    print(list)
    list.add_front('Y')
    list.add_back('Z')
    list.add_front('X')
    print(list)
    list.remove_back()
    print(list)


    print('\n# remove_at_index example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6])
    print(list)
    for index in [0, 0, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            list.remove_at_index(index)
            print(list)
        except Exception as e:
            print(type(e))
    print(list)


    print('\n# get_front example 1')
    list = LinkedList(['A', 'B'])
    print(list.get_front())
    print(list.get_front())
    list.remove_front()
    print(list.get_front())
    list.remove_back()
    try:
        print(list.get_front())
    except Exception as e:
        print(type(e))


    print('\n# get_back example 1')
    list = LinkedList([1, 2, 3])
    list.add_back(4)
    print(list.get_back())
    list.remove_back()
    print(list)
    print(list.get_back())


    print('\n# remove example 1')
    list = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(list)
    for value in [7, 3, 3, 3, 3]:
        print(list.remove(value), list.length(), list)


    print('\n# count example 1')
    list = LinkedList([1, 2, 3, 1, 2, 2])
    print(list, list.count(1), list.count(2), list.count(3), list.count(4))


    print('\n# slice example 1')
    list = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = list.slice(1, 3)
    print(list, ll_slice, sep="\n")
    ll_slice.remove_at_index(0)
    print(list, ll_slice, sep="\n")


    print('\n# slice example 2')
    list = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", list)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Slice", index, "/", size, end="")
        try:
            print(" --- OK: ", list.slice(index, size))
        except:
            print(" --- exception occurred.")

