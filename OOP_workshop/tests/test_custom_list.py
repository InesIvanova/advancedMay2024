from unittest import TestCase, main

from OOP_workshop.custom_exceptions import IndexOutOfRange, ElementNotPresented, EmptyList
from OOP_workshop.custom_list import CustomList


class CustomListTests(TestCase):
    def setUp(self):
        self.c = CustomList(1, 2, 3)

    def test_init(self):
        self.assertEqual([1, 2, 3], self.c._CustomList__value)

    def test_append(self):
        self.assertEqual([1, 2, 3], self.c._CustomList__value)

        result = self.c.append(5)

        self.assertEqual([1, 2, 3, 5], self.c._CustomList__value)
        self.assertEqual([1, 2, 3, 5], result)
        self.assertEqual(id(result), id(self.c._CustomList__value))

    def test_remove_invalid_index_raises(self):
        self.assertEqual([1, 2, 3], self.c._CustomList__value)

        with self.assertRaises(IndexOutOfRange) as ex:
            self.c.remove(-1)
        self.assertEqual("Invalid index", str(ex.exception))

        with self.assertRaises(IndexOutOfRange) as ex:
            self.c.remove(len(self.c._CustomList__value))
        self.assertEqual("Invalid index", str(ex.exception))
        self.assertEqual([1, 2, 3], self.c._CustomList__value)


    def test_remove(self):
        self.assertEqual([1, 2, 3], self.c._CustomList__value)


        result = self.c.remove(1)

        self.assertEqual(2, result)
        self.assertEqual([1, 3], self.c._CustomList__value)

    def test_get_by_index(self):
        self.assertEqual([1, 2, 3], self.c._CustomList__value)

        self.assertEqual(2, self.c._CustomList__value[1])

        result = self.c.get(1)

        self.assertEqual(2, result)
        self.assertEqual([1, 2, 3], self.c._CustomList__value)

    def test_get_index_by_element_obtains_first_occ(self):
        # Todo test multiple elements
        self.c.append(2)
        self.assertEqual([1, 2, 3, 2], self.c._CustomList__value)


        result = self.c.index(2)

        self.assertEqual(1, result)
        self.assertEqual([1, 2, 3, 2], self.c._CustomList__value)

    def test_invalid_element_raises(self):

        self.assertEqual([1, 2, 3], self.c._CustomList__value)

        self.assertNotIn(5, self.c._CustomList__value)

        with self.assertRaises(ElementNotPresented) as ex:
            self.c.index(5)
        self.assertEqual("Element not presented", str(ex.exception))

        self.assertEqual([1, 2, 3], self.c._CustomList__value)

    def test_invalid_element_final_index_raises(self):
        self.assertEqual([1, 2, 3], self.c._CustomList__value)

        self.assertNotIn(5, self.c._CustomList__value)

        with self.assertRaises(ElementNotPresented) as ex:
            self.c.final_index(5)
        self.assertEqual("Element not presented", str(ex.exception))

        self.assertEqual([1, 2, 3], self.c._CustomList__value)


    def test_final_index(self):
        self.c.append(2)
        self.assertEqual([1, 2, 3, 2], self.c._CustomList__value)

        result = self.c.final_index(2)

        self.assertEqual(3, result)
        self.assertEqual([1, 2, 3, 2], self.c._CustomList__value)

    def test_extend(self):
        self.assertEqual([1, 2, 3], self.c._CustomList__value)

        result = self.c.extend([4, 5])

        self.assertEqual([1, 2, 3, 4, 5], result)

        result = self.c.extend((6, 7))
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], result)

    def test_insert_invalid_index_raises(self):
        self.c.append(2)
        self.assertEqual([1, 2, 3, 2], self.c._CustomList__value)

        with self.assertRaises(IndexOutOfRange) as ex:
            self.c.insert(-1, 2)
        self.assertEqual("Invalid index", str(ex.exception))

        with self.assertRaises(IndexOutOfRange) as ex:
            self.c.insert(len(self.c._CustomList__value), 2)
        self.assertEqual("Invalid index", str(ex.exception))

    def test_insert(self):
        self.c.append(2)
        self.assertEqual([1, 2, 3, 2], self.c._CustomList__value)

        result = self.c.insert(2, 2)
        self.assertEqual([1, 2, 2, 3, 2], self.c._CustomList__value)
        self.assertEqual([1, 2, 2, 3, 2], result)

    def test_pop_no_elements_raises(self):
        self.c._CustomList__value = []
        self.assertEqual([], self.c._CustomList__value)

        with self.assertRaises(EmptyList) as ex:
            self.c.pop()
        self.assertEqual("No elements in the list", str(ex.exception))

    def test_pop(self):
        self.assertEqual([1, 2, 3], self.c._CustomList__value)

        result = self.c.pop()

        self.assertEqual(3, result)
        self.assertEqual([1, 2], self.c._CustomList__value)

    def test_clear(self):
        self.assertEqual([1, 2, 3], self.c._CustomList__value)

        result = self.c.clear()

        self.assertIsNone(result)

        self.assertEqual([], self.c._CustomList__value)

    def test_count(self):
        self.c.append(3)
        self.assertEqual([1, 2, 3, 3], self.c._CustomList__value)

        result = self.c.count(3)

        self.assertEqual(2, result)
        self.assertEqual([1, 2, 3, 3], self.c._CustomList__value)

        result = self.c.count(5)

        self.assertEqual(0, result)
        self.assertEqual([1, 2, 3, 3], self.c._CustomList__value)

    def test_reverse(self):
        self.assertEqual([1, 2, 3], self.c._CustomList__value)

        result = self.c.reverse()

        self.assertEqual([3, 2, 1], result)
        self.assertEqual([1, 2, 3], self.c._CustomList__value)

    def test_copy(self):
        self.assertEqual([1, 2, 3], self.c._CustomList__value)

        result = self.c.copy()

        self.assertNotEqual(id(result), id(self.c._CustomList__value))
        self.assertEqual([1, 2, 3], result)

    def test_size(self):
        self.assertEqual([1, 2, 3], self.c._CustomList__value)

        result = self.c.size()

        self.assertEqual(3, result)

        self.c.clear()
        self.assertEqual([], self.c._CustomList__value)

        result = self.c.size()

        self.assertEqual(0, result)

    def test_add_first(self):
        self.assertEqual([1, 2, 3], self.c._CustomList__value)

        result = self.c.add_first(5)

        self.assertIsNone(result)
        self.assertEqual([5, 1, 2, 3], self.c._CustomList__value)

    def test_dictionize_odd_numbers_of_elements(self):
        self.assertEqual(1, len(self.c._CustomList__value) % 2 )
        self.assertEqual([1, 2, 3], self.c._CustomList__value)

        result = self.c.dictionize()

        self.assertEqual({1: 2, 3: ' '}, result)
        self.assertEqual([1, 2, 3], self.c._CustomList__value)

    def test_dictionize_even_numbers_of_elements(self):
        self.c.append(4)
        self.assertEqual(0, len(self.c._CustomList__value) % 2 )
        self.assertEqual([1, 2, 3, 4], self.c._CustomList__value)

        result = self.c.dictionize()

        self.assertEqual({1: 2, 3: 4}, result)
        self.assertEqual([1, 2, 3, 4], self.c._CustomList__value)

    def test_move(self):
        self.c.append(4)
        self.assertEqual([1, 2, 3, 4], self.c._CustomList__value)

        result = self.c.move(2)

        self.assertEqual([3, 4, 1, 2], result)
        self.assertEqual([1, 2, 3, 4], self.c._CustomList__value)


    def test_sum_with_nums(self):
        self.c.append(5.6)
        self.assertEqual([1, 2, 3, 5.6], self.c._CustomList__value)

        result = self.c.sum()

        self.assertEqual(11.6, result)
        self.assertEqual([1, 2, 3, 5.6], self.c._CustomList__value)

    def test_sum_with_nums_and_iters(self):
        self.c.append("asd")
        self.assertEqual([1, 2, 3, "asd"], self.c._CustomList__value)

        result = self.c.sum()

        self.assertEqual(9, result)
        self.assertEqual([1, 2, 3, "asd"], self.c._CustomList__value)

    def test_overbound(self):
        self.c.append(0)
        self.assertEqual([1, 2, 3, 0], self.c._CustomList__value)

        result = self.c.overbound()

        self.assertEqual(2, result)

        self.c.append("four")
        self.assertEqual([1, 2, 3, 0, "four"], self.c._CustomList__value)

        result = self.c.overbound()
        self.assertEqual(4, result)

    def test_underbound(self):
        self.c._CustomList__value = [7, 4, 6]
        self.assertEqual([7, 4, 6], self.c._CustomList__value)

        result = self.c.underbound()

        self.assertEqual(1, result)

        self.c.append("asd")
        self.assertEqual([7, 4, 6, "asd"], self.c._CustomList__value)

        result = self.c.underbound()
        self.assertEqual(3, result)


if __name__ == "__main__":
    main()