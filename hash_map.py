# Course: CS261 - Data Structures
# Student Name: Benjamin Warren
# Assignment: Hash Map
# Description: Implementing a Hash Map in python


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Init new HashMap based on DA with SLL for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Return content of hash map t in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    def clear(self) -> None:
        """
        Empties hash map
        :return: None
        """
        for i in range(self.capacity):
            self.buckets[i] = LinkedList()
        self.size = 0

    def get(self, key: str) -> object:
        """
        Gets value associated with key in hash map
        :param key: key to search for
        :return: value associated with key
        """
        hash = self.hash_function(key)
        index = hash % self.capacity
        node = self.buckets[index].contains(key)
        try:
            return node.value
        except AttributeError:
            return None

    def put(self, key: str, value: object) -> None:
        """
        Adds key/value pair to map, updates value associated with key if key already exists
        :param key: Key to add
        :param value: Value associated with key
        :return: None
        """
        hash = self.hash_function(key)
        index = hash % self.capacity
        if self.buckets[index].contains(key):
            node = self.buckets[index].contains(key)
            node.value = value
        else:
            self.buckets[index].insert(key, value)
            self.size += 1
        return

    def remove(self, key: str) -> None:
        """
        Removes key/value pair associated with key
        :param key: Key to remove
        :return: None
        """
        hash = self.hash_function(key)
        index = hash % self.capacity
        if self.buckets[index].contains(key) is not None:
            self.buckets[index].remove(key)
            self.size -= 1
        return

    def contains_key(self, key: str) -> bool:
        """
        Checks hash map to see if it contains a certain key
        :param key: Key to search for
        :return: Boolean on whether it contains key or not
        """
        hash = self.hash_function(key)
        index = hash % self.capacity
        if self.buckets[index].contains(key) is not None:
            return True
        return False

    def empty_buckets(self) -> int:
        """
        Counts number of empty entries in hash map
        :return: Count of empty buckets
        """
        numEmpty = 0
        for i in range(self.capacity):
            if self.buckets[i].head is None:
                numEmpty += 1
        return numEmpty

    def table_load(self) -> float:
        """
        Calculates load factor
        :return: Load factor
        """
        load = self.size / self.capacity
        return load

    def resize_table(self, new_capacity: int) -> None:
        """
        Resizes internal hash table to new capacity by creating a new dynamic array
        :param new_capacity: New capacity of array
        :return: None
        """
        if new_capacity < 1:
            return
        else:
            newDA = DynamicArray()
            for _ in range(new_capacity):
                newDA.append(LinkedList())
            for _ in range(self.capacity):
                if self.buckets[_].head is not None:
                    cur = self.buckets[_].head
                    while cur is not None:
                        hash = self.hash_function(cur.key)
                        index = hash % new_capacity
                        newDA[index].insert(cur.key, cur.value)
                        cur = cur.next
            self.buckets = newDA
            self.capacity = new_capacity
            return

    def get_keys(self) -> DynamicArray:
        """
        Gets all keys in hash map
        :return: New Dynamic array containing just the keys
        """
        print(self)
        newDA = DynamicArray()
        for _ in range(self.capacity):
            print(self.buckets[_])
            if self.buckets[_].head is not None:
                cur = self.buckets[_].head
                while cur is not None:
                    newDA.append(cur.key)
                    cur = cur.next
        return newDA

# BASIC TESTING
if __name__ == "__main__":

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(100, hash_function_1)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 10)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key2', 20)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 30)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key4', 40)
    print(m.empty_buckets(), m.size, m.capacity)


    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.size, m.capacity)


    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(100, hash_function_1)
    print(m.table_load())
    m.put('key1', 10)
    print(m.table_load())
    m.put('key2', 20)
    print(m.table_load())
    m.put('key1', 30)
    print(m.table_load())


    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(m.table_load(), m.size, m.capacity)

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(100, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)


    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(50, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    print(m.size, m.capacity)
    m.put('key2', 20)
    print(m.size, m.capacity)
    m.resize_table(100)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)


    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)


    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(40, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)


    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(10, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))


    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)


    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(30, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))


    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(150, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.size, m.capacity)
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)


    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(50, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')


    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))


    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            result &= m.contains_key(str(key))
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.size, m.capacity, round(m.table_load(), 2))


    print("\nPDF - get_keys example 1")
    print("------------------------")
    m = HashMap(10, hash_function_2)
    for i in range(100, 200, 10):
        m.put(str(i), str(i * 10))
    print(m.get_keys())

    m.resize_table(1)
    print(m.get_keys())

    m.put('200', '2000')
    m.remove('100')
    m.resize_table(2)
    print(m.get_keys())
