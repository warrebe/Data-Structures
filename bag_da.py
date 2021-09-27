# Course: CS261 - Data Structures
# Student Name: Benjamin Warren
# Assignment:Bag dynamic array
# Description: Creating a Bag dynamic array

from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS CLASS IN ANY WAY
        """
        return self.da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        Adds element to bag
        :param value: Element to add to bag
        :return: None
        """
        self.da.append(value)

    def remove(self, value: object) -> bool:
        """
        Removes one element from bag that matches value
        :param value: element to remove
        :return: Boolean on whether an element was removed
        """
        for _ in range(self.da.length()):
            if value == self.da[_]:
                self.da.remove_at_index(_)
                return True
        return False

    def count(self, value: object) -> int:
        """
        Counts number of elements that match provided value
        :param value: Value to search for
        :return count: Count of elements that match
        """
        count = 0
        for _ in range(self.da.length()):
            if self.da[_] == value:
                count += 1
        return count

    def clear(self) -> None:
        """
        Empties bag by dereferencing the Dynamic Array
        :return: None
        """
        self.da = DynamicArray()

    def equal(self, second_bag: object) -> bool:
        """
        Checks to see if two bags are equivalent
        :param second_bag: Second bag to compare to self
        :return: Boolean on whether they are equivalent or not
        """
        if self.da.length() == second_bag.da.length():
            counter = 0
            try:
                newArr = StaticArray(self.da.length())
                newArr1 = StaticArray(second_bag.da.length())
            except StaticArrayException:
                return True
            for i in range(self.da.length()):
                newArr[i] = self.da[i]
            for j in range(self.da.length()):
                newArr1[j] = second_bag.da[j]
            for i in range(newArr.size()):
                for j in range(newArr1.size()):
                    if newArr[i] == newArr1[j]:
                        counter += 1
                        newArr[i] = "Not Equivalent"
                        newArr1[j] = "equivalence"
            if counter == self.da.length():
                return True
            else:
                return False
        else:
            return False


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)


    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)


    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))


    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)


    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))
