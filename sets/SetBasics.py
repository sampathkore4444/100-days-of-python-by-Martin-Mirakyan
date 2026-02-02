class SetBasics:
    def __init__(self, ele_list):
        self.my_set = set(ele_list)

    def add_element(self, ele):
        if ele is not None:
            self.my_set.add(ele)
            print(f"Element {ele} has been added to the set")
        else:
            raise ValueError("Empty!!")

    def add_multiple_elements(self, ele_list):
        if len(ele_list) > 0:
            self.my_set.update(ele_list)
            print(f"Set has been updated with multiple elements")
        else:
            raise ValueError("List is empty!!")

    def remove_element_with_error(self, ele):
        self.my_set.remove(ele)

        # if ele in self.my_set:
        #     self.my_set.remove(ele)
        #     print(f"Element {ele} has been removed from the set")
        # else:
        #     raise ValueError(
        #         f"Element {ele} has not been found in the set"
        #     )  # without raise also, it throws an error

    def remove_element_without_error(self, ele):
        self.my_set.discard(ele)

    def clear_elements(self):
        self.my_set.clear()
        print(f"set has been cleared!!")

    def union_operation1(self, set2):
        self.my_set = self.my_set.union(
            set2
        )  # Union does Auto conversion other iterables into set

    def union_operation2(self, set2):
        self.my_set = self.my_set | set(
            set2
        )  # Pipe operator does not do auto conversion. so, the iterable must be converted into set before using

    def intersection_operation1(self, set2):
        self.my_set = self.my_set.intersection(
            set2
        )  # intersection does Auto conversion other iterables into set

    def intersection_operation2(self, set2):
        self.my_set = self.my_set & set(
            set2
        )  # Ampersand operator does not do auto conversion. so, the iterable must be converted into set before using

    def difference_operation1(self, set2):
        self.my_set = self.my_set.difference(
            set2
        )  # difference does Auto conversion other iterables into set

    def difference_operation2(self, set2):
        self.my_set = self.my_set - set(
            set2
        )  # Minus operator does not do auto conversion. so, the iterable must be converted into set before using

    def symmetric_difference_operation1(self, set2):
        self.my_set = self.my_set.symmetric_difference(
            set2
        )  # symmetric_difference does Auto conversion other iterables into set

    def symmetric_difference_operation2(self, set2):
        self.my_set = self.my_set ^ set(
            set2
        )  # Exponent operator does not do auto conversion. so, the iterable must be converted into set before using


elements = [1, 2, 2, 3, 4]
setbasics = SetBasics(elements)
print(setbasics.my_set)

setbasics.add_element(5)
print(setbasics.my_set)

additional_elements = [4, 5, 6]
setbasics.add_multiple_elements(additional_elements)
print(setbasics.my_set)

# setbasics.add_element(None)
# print(setbasics.my_set)

# setbasics.add_multiple_elements([])
# print(setbasics.my_set)

setbasics.remove_element_with_error(6)
print(f"After removal with error= {setbasics.my_set}")

setbasics.remove_element_without_error(6)
print(f"After removal without error= {setbasics.my_set}")

# setbasics.remove_element_with_error(6)
# print(f"After removal with error= {setbasics.my_set}")

setbasics.clear_elements()
print("After clearing the set=", setbasics.my_set)


# Union
elements = [1, 2, 2, 3, 4]
setbasics = SetBasics(elements)
print(setbasics.my_set)
setbasics.union_operation1([3, 4, 5, 6])
print("After union operation 1=", setbasics.my_set)
setbasics.union_operation2([3, 4, 5, 6])
print("After union operation 2=", setbasics.my_set)

# Intersection
print(setbasics.my_set)
setbasics.intersection_operation1([3, 4, 5, 6])
print("After intersection operation 1=", setbasics.my_set)
setbasics.intersection_operation2([3, 4, 5, 6])
print("After intersection operation 2=", setbasics.my_set)

# Difference
print(setbasics.my_set)
setbasics.difference_operation1([3, 4, 5])
print("After difference operation 1=", setbasics.my_set)
setbasics.difference_operation2([3, 4, 5])
print("After difference operation 2=", setbasics.my_set)

# Symmetric Difference
print(setbasics.my_set)
setbasics.symmetric_difference_operation1([3, 4, 5])
print("After difference operation 1=", setbasics.my_set)
setbasics.symmetric_difference_operation2([3, 4, 5])
print("After difference operation 2=", setbasics.my_set)
