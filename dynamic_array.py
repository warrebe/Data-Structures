# Course: CS261 - Data Structures
# Student Name: Benjamin Warren
# Assignment: Dynamic Array
# Description: Creating a dynamic array data structure

from static_array import *


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.size = 0
        self.capacity = 4
        self.first = 0  # do not use / change this value
        self.data = StaticArray(self.capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self.size) + "/" + str(self.capacity) + ' ['
        out += ', '.join([str(self.data[_]) for _ in range(self.size)])
        return out + ']'

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        return self.data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        self.data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        Changes data array to a new size
        :param new_capacity: New capacity for array
        :return: None
        """
        if new_capacity < 1:
            return
        elif new_capacity < self.size:
            return
        else:
            newArr = StaticArray(new_capacity)
            for _ in range(new_capacity):
                newArr[_] = None
            for _ in range(self.length()):
                newArr[_] = self.get_at_index(_)
            self.data = newArr
            self.capacity = new_capacity

    def append(self, value: object) -> None:
        """
        Appends data array by adding new value at end
        :param value: New value to add
        :return: None
        """
        if self.capacity == self.size:
            self.resize(self.capacity * 2)
        self.data[self.length()] = value
        self.size += 1

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Insert values at specific index in array
        :param index: Place to insert
        :param value: Value to insert at specific index
        :return: None
        """
        if index < 0:
            raise DynamicArrayException
        if index > self.length():
            raise DynamicArrayException
        move = value
        if self.size == self.capacity:
            self.resize(self.capacity * 2)
        self.size += 1
        for _ in range(index, self.length()):
            temp = self.get_at_index(_)
            self.set_at_index(_, move)
            move = temp

    def remove_at_index(self, index: int) -> None:
        """
        Removes an element at a specific index and adjusts array accordingly
        :param index: Place to remove an element in the array
        :return: None
        """
        if index < 0:
            raise DynamicArrayException
        if self.size == 0:
            raise DynamicArrayException
        if index >= self.length():
            raise DynamicArrayException
        if self.capacity > 10:
            if (self.length() * 2) >= 10:
                if self.capacity > self.length() * 4:
                    self.resize(2 * self.length())
            elif self.length() < (self.capacity / 4):
                self.resize(10)
        self.size -= 1
        self.data[index] = None
        newArr = StaticArray(self.capacity)
        index = 0
        for _ in range(self.capacity):
            if self.data[_] is not None:
                newArr[index] = self.data[_]
                index += 1
        self.data = newArr

    def slice(self, start_index: int, size: int) -> object:
        """
        Slices array similarly to pythons built in slice
        :param start_index: Index to begin slice
        :param size: size of new sliced array
        :return: A new dynamic array
        """
        if start_index >= self.length() or start_index < 0 or size < 0 or self.size == 0:
            raise DynamicArrayException
        counter = 0
        for _ in range(start_index, self.length() + 1):
            counter += 1
        if (start_index + size) > self.length():
            raise DynamicArrayException
        newDynArr = DynamicArray()
        for _ in range(start_index, start_index + size):
            newDynArr.append(self.data[_])
        return newDynArr

    def merge(self, second_da: object) -> None:
        """
        Merges data array with another dynamic arrays data
        :param second_da: Second dynamic arrays data to merge with
        :return: None
        """
        for _ in range(second_da.length()):
            self.append(second_da[_])

    def map(self, map_func) -> object:
        """
        Creates new dynamic array derived from original but with map_func applied to all elements
        :param map_func: Function to apply to all elements of original array
        :return: New dynamic array
        """
        newDynArr = DynamicArray()
        for _ in range(self.length()):
            newDynArr.append(map_func(self.data[_]))
        return newDynArr

    def filter(self, filter_func) -> object:
        """
        Filters original dynamic array into a new one using filter_func on all elements
        :param filter_func: Function to filter with
        :return: New dynamic array
        """
        newDynArr = DynamicArray()
        for _ in range(self.length()):
            if filter_func(self.data[_]):
                newDynArr.append(self.data[_])
        return newDynArr

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        Applies reduce function to array, and sums the elements
        :param reduce_func: Function to reduce array with
        :param initializer: Initial value to be summed, value is the first array index if not assigned
        :return: reduced array
        """
        index = 0
        if self.size == 0:
            return initializer
        if initializer is None:
            if self.data[0] is not None:
                initializer = self.data[0]
                index = 1
        if type(initializer) is str:
            reduce = ""
        else:
            reduce = 0
        for _ in range(index, self.length()):
            reduce = reduce_func(reduce, self.data[_])
        initializer += reduce
        return initializer


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.resize(8)
    print(da.size, da.capacity, da.data)
    da.resize(2)
    print(da.size, da.capacity, da.data)
    da.resize(0)
    print(da.size, da.capacity, da.data)


    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)


    print("\n# append - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.append(1)
    print(da.size, da.capacity, da.data)
    print(da)


    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)


    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.size)
    print(da.capacity)


    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)


    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)


    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)


    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.size, da.capacity)
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)


    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.size, da.capacity)
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.size, da.capacity)

    for i in range(14):
        print("Before remove_at_index(): ", da.size, da.capacity, end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.size, da.capacity)


    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)


    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")


    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")


    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)


    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)


    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2

    def square(value):
        return value ** 2

    def cube(value):
        return value ** 3

    def plus_one(value):
        return value + 1

    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))


    print("\n# filter example 1")
    def filter_a(e):
        return e > 10

    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))


    print("\n# filter example 2")
    def is_long_word(word, length):
        return len(word) > length

    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))


    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))


    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))