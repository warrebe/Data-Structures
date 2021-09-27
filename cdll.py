# Course: CS261 - Data Structures
# Student Name: Benjamin Warren
# Assignment: Circularly Linked List
# Description: A linked list with only a front sentinel and two pointers


class CDLLException(Exception):
    """
    Custom exception class to be used by Circular Doubly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DLNode:
    """
    Doubly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        self.next = None
        self.prev = None
        self.value = value


class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with sentinel
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.sentinel = DLNode(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate CDLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'CDLL ['
        if self.sentinel.next != self.sentinel:
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.value)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list

        This can also be used as troubleshooting method. This method works
        by independently measuring length during forward and backward
        traverse of the list and return the length if results agree or error
        code of -1 or -2 if thr measurements are different.

        Return values:
        >= 0 - length of the list
        -1 - list likely has an infinite loop (forward or backward)
        -2 - list has some other kind of problem

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """

        # length of the list measured traversing forward
        count_forward = 0
        cur = self.sentinel.next
        while cur != self.sentinel and count_forward < 101_000:
            count_forward += 1
            cur = cur.next

        # length of the list measured traversing backwards
        count_backward = 0
        cur = self.sentinel.prev
        while cur != self.sentinel and count_backward < 101_000:
            count_backward += 1
            cur = cur.prev

        # if any of the result is > 100,000 -> list has a loop
        if count_forward > 100_000 or count_backward > 100_000:
            return -1

        # if counters have different values -> there is some other problem
        return count_forward if count_forward == count_backward else -2

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.sentinel.next == self.sentinel

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        Add value to front of list
        :param value: value to add
        :return: None
        """
        Temp = self.sentinel.next
        self.sentinel.next = DLNode(value)
        self.sentinel.next.prev = self.sentinel
        self.sentinel.next.next = Temp
        Temp.prev = self.sentinel.next

    def add_back(self, value: object) -> None:
        """
        adds value to back of list
        :param value: value to add
        :return: None
        """
        Temp = self.sentinel.prev
        self.sentinel.prev = DLNode(value)
        self.sentinel.prev.next = self.sentinel
        self.sentinel.prev.prev = Temp
        Temp.next = self.sentinel.prev

    def insert_at_index(self, index: int, value: object) -> None:
        """
        inserts value at index
        :param index: index
        :param value: value to insert
        :return: None
        """
        if index == 0:
            self.add_front(value)
            return
        if index < 0 or index > self.length():
            raise CDLLException
        current = self.sentinel
        for _ in range(index):
            current = current.next
            if _ == index - 1:
                Temp = current.next
                current.next = DLNode(value)
                current.next.prev = current
                current.next.next = Temp
                Temp.prev = current.next

    def remove_front(self) -> None:
        """
        removes front node
        :return: None
        """
        if self.length() <= 0:
            raise CDLLException
        self.sentinel.next = self.sentinel.next.next
        self.sentinel.next.prev = self.sentinel

    def remove_back(self) -> None:
        """
        removes back node
        :return: None
        """
        if self.length() <= 0:
            raise CDLLException
        self.sentinel.prev = self.sentinel.prev.prev
        self.sentinel.prev.next = self.sentinel

    def remove_at_index(self, index: int) -> None:
        """
        removes node at index
        :param index: index
        :return: None
        """
        if index == 0:
            self.remove_front()
            return
        if index < 0 or index >= self.length():
            raise CDLLException
        current = self.sentinel
        for _ in range(index):
            current = current.next
            if _ == index - 1:
                current.next = current.next.next
                current.next.prev = current
                return

    def get_front(self) -> object:
        """
        Gets front node
        :return: front node
        """
        if self.length() <= 0:
            raise CDLLException
        return self.sentinel.next.value

    def get_back(self) -> object:
        """
        returns back node
        :return: back node
        """
        if self.length() <= 0:
            raise CDLLException
        return self.sentinel.prev.value

    def remove(self, value: object) -> bool:
        """
        removes a certain node containing value
        :param value: value to remove
        :return: boolean if it was removed
        """
        current = self.sentinel
        for _ in range(self.length()):
            current = current.next
            if current.value == value:
                current.prev.next = current.next
                current.next.prev = current.prev
                return True
        return False

    def count(self, value: object) -> int:
        """
        counts number of occurences of value
        :param value: value to count
        :return: Count of values
        """
        count = 0
        current = self.sentinel
        for _ in range(self.length()):
            current = current.next
            if current.value == value:
                count += 1
        return count

    def swap_pairs(self, index1: int, index2: int) -> None:
        """
        swaps two node using pointer
        :param index1: first node
        :param index2: second node
        :return: None
        """
        if index1 >= self.length() or index1 < 0:
            raise CDLLException
        if index2 >= self.length() or index2 < 0:
            raise CDLLException
        current1 = self.sentinel
        if index1 == 0:
            prev1 = current1
            next1 = current1.next.next
            current1 = current1.next
        else:
            for _ in range(index1):
                current1 = current1.next
                if _ == index1 - 1:
                    prev1 = current1
                    next1 = current1.next.next
                    current1 = current1.next
                    break
        current2 = self.sentinel
        if index2 == 0:
            prev2 = current2
            next2 = current2.next.next
            current2 = current2.next
        else:
            for _ in range(index2):
                current2 = current2.next
                if _ == index2 - 1:
                    prev2 = current2
                    next2 = current2.next.next
                    current2 = current2.next
                    break
        if current1.next == current2:
            temp1 = current2.next
            current2.next = current1
            current1.next = temp1
            temp1.prev = current1
            temp2 = current1.prev
            current2.prev = current1.prev
            current1.prev = current2
            temp2.next = current2
        elif current2.next == current1:
            temp1 = current1.next
            current1.next = current2
            current2.next = temp1
            temp1.prev = current2
            temp2 = current2.prev
            current1.prev = current2.prev
            current2.prev = current1
            temp2.next = current1
        else:
            current1.prev = prev2
            prev2.next = current1
            current1.next = next2
            next2.prev = current1
            current2.prev = prev1
            prev1.next = current2
            current2.next = next1
            next1.prev = current2

    def reverse(self) -> None:
        """
        Reverse circular doubly linked list
        :return: None
        """
        current = self.sentinel.prev
        for _ in range(self.length()):
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.next
        temp = self.sentinel.prev
        self.sentinel.prev = self.sentinel.next
        self.sentinel.next = temp

    def sort(self) -> None:
        """
        Sorts list using bubble sort O(N^2)
        :return: None
        """
        for i in range(self.length()):
            current = self.sentinel.next
            for j in range(0, self.length() - i - 1):
                if current.value > current.next.value:
                    temp = current.next
                    current.next = current.next.next
                    current.next.prev = current
                    temp1 = current.prev
                    current.prev = temp
                    temp.next = current
                    temp.prev = temp1
                    temp.prev.next = temp
                    current = current.prev
                current = current.next

    def rotate(self, steps: int) -> None:
        """
        Rotates list number of steps
        :param steps: Steps to rotate
        :return: None
        """
        if self.length() > 0:
            steps = steps % self.length()
        current = self.sentinel
        if steps == 0:
            return
        elif steps < 0:
            steps = abs(steps)
            for _ in range(steps):
                temp1 = current.prev
                current.prev = current.next
                temp1.next = current.prev
                current.next = current.prev.next
                current.next.prev = current
                current.prev.next = current
                current.prev.prev = temp1
        else:
            for _ in range(steps):
                temp1 = current.next
                current.next = current.prev
                temp1.prev = current.next
                current.prev = current.next.prev
                current.prev.next = current
                current.next.prev = current
                current.next.next = temp1

    def remove_duplicates(self) -> None:
        """
        Removes all numbers of a duplicate chain
        :return: None
        """
        for i in range(self.length()):
            current = self.sentinel.next
            for j in range(0, self.length() - i - 1):
                if current.value == current.next.value:
                    while self.count(current.value) > 0:
                        self.remove(current.value)
                    current = current.prev
                current = current.next

    def odd_even(self) -> None:
        """
        Swaps odd indexes to front of list
        :return: None
        """
        odd = self.sentinel.next
        even = self.sentinel.next.next
        evenFirst = even
        while (1 == 1):
            if odd == self.sentinel or even == self.sentinel or even.next == self.sentinel:
                odd.next = evenFirst
                evenFirst.prev = odd
                break
            odd.next = even.next
            odd.next.prev = odd
            odd = odd.next
            if odd.next == self.sentinel:
                even.next = self.sentinel
                self.sentinel.prev = even
                odd.next = evenFirst
                evenFirst.prev = odd
                break
            even.next = odd.next
            even.next.prev = even
            even = even.next
        return

    def add_integer(self, num: int) -> None:
        """
        adds integer number to list representing another integer
        :param num: Number to add to integer list
        :return: None
        """
        current = self.sentinel.prev
        carry = False
        num = str(num)
        i = 1
        while True:
            if current == self.sentinel:
                temp = self.sentinel.next
                self.sentinel.next = DLNode(0)
                self.sentinel.next.prev = self.sentinel
                self.sentinel.next.next = temp
                temp.prev = self.sentinel.next
                current = current.next
            if carry is True:
                current.value += 1
                carry = False
            if (len(num) - i) >= 0:
                current.value += int(num[len(num) - i])
            if current.value >= 10:
                current.value = current.value % 10
                carry = True
            current = current.prev
            i += 1
            if (carry is False) and (len(num) - i < 0):
                return

if __name__ == '__main__':
    pass

    print('\n# add_front example 1')
    lst = CircularList()
    print(lst)
    lst.add_front('A')
    lst.add_front('B')
    lst.add_front('C')
    print(lst)

    print('\n# add_back example 1')
    lst = CircularList()
    print(lst)
    lst.add_back('C')
    lst.add_back('B')
    lst.add_back('A')
    print(lst)

    print('\n# insert_at_index example 1')
    lst = CircularList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print('\n# remove_front example 1')
    lst = CircularList([1, 2])
    print(lst)
    for i in range(3):
        try:
            lst.remove_front()
            print('Successful removal', lst)
        except Exception as e:
            print(type(e))

    print('\n# remove_back example 1')
    lst = CircularList()
    try:
        lst.remove_back()
    except Exception as e:
        print(type(e))
    lst.add_front('Z')
    lst.remove_back()
    print(lst)
    lst.add_front('Y')
    lst.add_back('Z')
    lst.add_front('X')
    print(lst)
    lst.remove_back()
    print(lst)

    print('\n# remove_at_index example 1')
    lst = CircularList([1, 2, 3, 4, 5, 6])
    print(lst)
    for index in [0, 0, 0, 2, 2, -2]:
        print('Removed at index:', index, ': ', end='')
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))
    print(lst)

    print('\n# get_front example 1')
    lst = CircularList(['A', 'B'])
    print(lst.get_front())
    print(lst.get_front())
    lst.remove_front()
    print(lst.get_front())
    lst.remove_back()
    try:
        print(lst.get_front())
    except Exception as e:
        print(type(e))

    print('\n# get_back example 1')
    lst = CircularList([1, 2, 3])
    lst.add_back(4)
    print(lst.get_back())
    lst.remove_back()
    print(lst)
    print(lst.get_back())

    print('\n# remove example 1')
    lst = CircularList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(lst)
    for value in [7, 3, 3, 3, 3]:
        print(lst.remove(value), lst.length(), lst)

    print('\n# count example 1')
    lst = CircularList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print('\n# swap_pairs example 1')
    lst = CircularList([0, 1, 2, 3, 4, 5, 6])
    test_cases = ((0, 6), (0, 7), (-1, 6), (1, 5),
                  (4, 2), (3, 3), (1, 2), (2, 1))

    for i, j in test_cases:
        print('Swap nodes ', i, j, ' ', end='')
        try:
            lst.swap_pairs(i, j)
            print(lst)
        except Exception as e:
            print(type(e))

    print('\n# swap_pairs example 2')
    lst = CircularList([10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    test_cases = ((10, 0), (0,10))

    for i, j in test_cases:
        print('Swap nodes ', i, j, ' ', end='')
        try:
            lst.swap_pairs(i, j)
            print(lst)
        except Exception as e:
            print(type(e))

    print('\n# reverse example 1')
    test_cases = (
        [1, 2, 3, 3, 4, 5],
        [1, 2, 3, 4, 5],
        ['A', 'B', 'C', 'D']
    )
    for case in test_cases:
        lst = CircularList(case)
        lst.reverse()
        print(lst)

    print('\n# reverse example 2')
    lst = CircularList()
    print(lst)
    lst.reverse()
    print(lst)
    lst.add_back(2)
    lst.add_back(3)
    lst.add_front(1)
    lst.reverse()
    print(lst)

    print('\n# reverse example 3')


    class Student:
        def __init__(self, name, age):
            self.name, self.age = name, age

        def __eq__(self, other):
            return self.age == other.age

        def __str__(self):
            return str(self.name) + ' ' + str(self.age)


    s1, s2 = Student('John', 20), Student('Andy', 20)
    lst = CircularList([s1, s2])
    print(lst)
    lst.reverse()
    print(lst)
    print(s1 == s2)

    print('\n# reverse example 4')
    lst = CircularList([1, 'A'])
    lst.reverse()
    print(lst)

    print('\n# sort example 1')
    test_cases = (
        [1, 10, 2, 20, 3, 30, 4, 40, 5],
        ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
        [(1, 1), (20, 1), (1, 20), (2, 20)]
    )
    for case in test_cases:
        lst = CircularList(case)
        print(lst)
        lst.sort()
        print(lst)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    for steps in [1, 2, 0, -1, -2, 28, -100]:
        lst = CircularList(source)
        lst.rotate(steps)
        print(lst, steps)

    print('\n# rotate example 2')
    lst = CircularList([10, 20, 30, 40])
    for j in range(-1, 2, 2):
        for _ in range(3):
            lst.rotate(j)
            print(lst)

    print('\n# rotate example 3')
    lst = CircularList()
    lst.rotate(10)
    print(lst)

    print('\n# remove_duplicates example 1')
    test_cases = (
        [1, 2, 3, 4, 5], [1, 1, 1, 1, 1],
        [], [1], [1, 1], [1, 1, 1, 2, 2, 2],
        [0, 1, 1, 2, 3, 3, 4, 5, 5, 6],
        list("abccd"),
        list("005BCDDEEFI")
    )

    for case in test_cases:
        lst = CircularList(case)
        print('INPUT :', lst)
        lst.remove_duplicates()
        print('OUTPUT:', lst)

    print('\n# odd_even example 1')
    test_cases = (
        [1, 2, 3, 4, 5], list('ABCDE'),
        [], [100], [100, 200], [100, 200, 300],
        [100, 200, 300, 400],
        [10, 'A', 20, 'B', 30, 'C', 40, 'D', 50, 'E']
    )

    for case in test_cases:
        lst = CircularList(case)
        print('INPUT :', lst)
        lst.odd_even()
        print('OUTPUT:', lst)

    print('\n# add_integer example 1')
    test_cases = (
      ([1, 2, 3], 10456),
      ([], 25),
      ([2, 0, 9, 0, 7], 108),
       ([9, 9, 9], 9_999_999),
    )
    for list_content, integer in test_cases:
       lst = CircularList(list_content)
    print('INPUT :', lst, 'INTEGER', integer)
    lst.add_integer(integer)
    print('OUTPUT:', lst)
