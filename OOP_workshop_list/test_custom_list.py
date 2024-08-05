from unittest import TestCase, main

from OOP_workshop_list.custom_list import CustomList


class TestCustomList(TestCase):
    def setUp(self):
        self.cl = CustomList(5, 16, 17.5, "asd")
    def test_init(self):
        c = CustomList(5, 16, 17.5, "asd")
        self.assertEqual(c._CustomList__data, [5, 16, 17.5, "asd"])

    def test_add_element_appends_it_to_the_end_returns_whole_list(self):
        self.assertEqual(len(self.cl._CustomList__data), 4)
        self.assertEqual(self.cl._CustomList__data, [5, 16, 17.5, "asd"])

        result = self.cl.append(100)

        self.assertEqual(len(self.cl._CustomList__data), 5)
        self.assertEqual(self.cl._CustomList__data, [5, 16, 17.5, "asd", 100])
        expected_id_in_memory = id(self.cl._CustomList__data)
        self.assertEqual(result, self.cl._CustomList__data)
        self.assertEqual(expected_id_in_memory, id(result))

    def test_remove_removes_the_element_on_the_given_index_returns_element(self):
        self.cl.append(5)
        self.assertEqual([5, 16, 17.5, "asd", 5], self.cl._CustomList__data)

        index = 0
        result = self.cl.remove(index)
        self.assertEqual([16, 17.5, "asd", 5], self.cl._CustomList__data)
        self.assertEqual(5, result)

    def test_remove_invalid_index_raises(self):
        invalid_index_values = [len(self.cl._CustomList__data), -(len(self.cl._CustomList__data) +1)]
        for index in invalid_index_values:
            index = len(self.cl._CustomList__data)
            with self.assertRaises(IndexError) as ex:
                self.cl.remove(index)

        self.assertEqual("Index is not in range.", str(ex.exception))

    def test_get_invalid_index_raises(self):
        invalid_index_values = [len(self.cl._CustomList__data), -(len(self.cl._CustomList__data) + 1)]
        for index in invalid_index_values:
            index = len(self.cl._CustomList__data)
            with self.assertRaises(IndexError) as ex:
                self.cl.get(index)

        self.assertEqual("Index is not in range.", str(ex.exception))

    def test_get_index_returns_element(self):
        self.assertEqual(self.cl._CustomList__data, [5, 16, 17.5, "asd"])

        result = self.cl.get(0)

        self.assertEqual(self.cl._CustomList__data, [5, 16, 17.5, "asd"])
        self.assertEqual(5, result)

    def test_extend_extends_all_elements_at_the_end_Of_the_list(self):
        self.assertEqual(4, len(self.cl._CustomList__data))
        self.assertEqual([5, 16, 17.5, "asd"],self.cl._CustomList__data)

        result = self.cl.extend([100, 200, 300])

        self.assertEqual(7, len(self.cl._CustomList__data))
        self.assertEqual([5, 16, 17.5, "asd", 100, 200, 300],self.cl._CustomList__data)

        self.assertEqual(id(self.cl._CustomList__data), id(result))
        self.assertEqual(self.cl._CustomList__data, result)

    def test_insert_inserts_value_returns_list(self):
        self.assertEqual(4, len(self.cl._CustomList__data))
        self.assertEqual([5, 16, 17.5, "asd"],self.cl._CustomList__data)

        result = self.cl.insert(0, 100)

        self.assertEqual(5, len(self.cl._CustomList__data))
        self.assertEqual([100, 5, 16, 17.5, "asd"],self.cl._CustomList__data)

        self.assertEqual(self.cl._CustomList__data, result)
        self.assertEqual(id(self.cl._CustomList__data), id(result))

    def test_insert_invalid_index_raises(self):
        self.assertEqual(4, len(self.cl._CustomList__data))
        self.assertEqual([5, 16, 17.5, "asd"], self.cl._CustomList__data)

        with self.assertRaises(IndexError) as ex:
            self.cl.insert(len(self.cl._CustomList__data), 100)
        self.assertEqual("Index is not in range.", str(ex.exception))

        self.assertEqual(4, len(self.cl._CustomList__data))
        self.assertEqual([5, 16, 17.5, "asd"], self.cl._CustomList__data)

    def test_pop_removes_last_element(self):
        self.assertEqual(4, len(self.cl._CustomList__data))
        self.assertEqual([5, 16, 17.5, "asd"], self.cl._CustomList__data)

        result = self.cl.pop()

        self.assertEqual(3, len(self.cl._CustomList__data))
        self.assertEqual([5, 16, 17.5], self.cl._CustomList__data)

        self.assertEqual("asd", result)

    def test_pop_empty_list(self):
        self.cl._CustomList__data.clear()
        self.assertEqual([], self.cl._CustomList__data)

        with self.assertRaises(IndexError) as ex:
            self.cl.pop()

        self.assertEqual("pop from empty list", str(ex.exception))
        self.assertEqual([], self.cl._CustomList__data)

    def test_clear_removes_all_values_from_list(self):
        self.assertEqual(4, len(self.cl._CustomList__data))
        self.assertEqual([5, 16, 17.5, "asd"], self.cl._CustomList__data)

        result = self.cl.clear()

        self.assertEqual(0, len(self.cl._CustomList__data))
        self.assertEqual([], self.cl._CustomList__data)

        self.assertIsNone(result)

    def test_index_returns_first_occurrence_of_element(self):
        self.cl.append(5)
        self.assertEqual([5, 16, 17.5, "asd", 5], self.cl._CustomList__data)

        result = self.cl.index(5)

        self.assertEqual(0, result)
        self.assertEqual([5, 16, 17.5, "asd", 5], self.cl._CustomList__data)

    def test_index_no_such_element_raises(self):
        self.assertEqual([5, 16, 17.5, "asd"], self.cl._CustomList__data)

        with self.assertRaises(ValueError) as ex:
            self.cl.index(100)
        self.assertEqual("Element is not in the list", str(ex.exception))

    def test_count_returns_count(self):
        self.cl.append(5)
        self.assertEqual([5, 16, 17.5, "asd", 5], self.cl._CustomList__data)

        result = self.cl.count(5)
        self.assertEqual(2, result)

        self.assertEqual([5, 16, 17.5, "asd", 5], self.cl._CustomList__data)

    def test_count_returns_0_if_element_is_not_there(self):
        self.assertEqual([5, 16, 17.5, "asd"], self.cl._CustomList__data)

        result = self.cl.count(100)

        self.assertEqual(0, result)
        self.assertEqual([5, 16, 17.5, "asd"], self.cl._CustomList__data)

    def test_reverse_returns_elements_in_reverse_order_list_is_unchanged(self):
        self.assertEqual([5, 16, 17.5, "asd"], self.cl._CustomList__data)

        result = self.cl.reverse()

        self.assertEqual(["asd", 17.5, 16, 5], result)
        self.assertEqual([5, 16, 17.5, "asd"], self.cl._CustomList__data)

        self.assertNotEqual(id(self.cl._CustomList__data), id(result))

    def test_copy_returns_copy_of_the_list(self):
        self.assertEqual([5, 16, 17.5, "asd"], self.cl._CustomList__data)

        result = self.cl.copy()

        self.assertEqual([5, 16, 17.5, "asd"], result)
        self.assertEqual([5, 16, 17.5, "asd"], self.cl._CustomList__data)
        self.assertNotEqual(id(self.cl._CustomList__data), id(result))

    def test_size_returns_length(self):
        self.assertEqual([5, 16, 17.5, "asd"], self.cl._CustomList__data)
        self.assertEqual(4, len(self.cl._CustomList__data))

        result = self.cl.size()

        self.assertEqual(4, result)
        self.assertEqual([5, 16, 17.5, "asd"], self.cl._CustomList__data)

        self.cl.clear()
        self.assertEqual([], self.cl._CustomList__data)
        self.assertEqual(0, len(self.cl._CustomList__data))

        result = self.cl.size()
        self.assertEqual(0, result)

        self.assertEqual([], self.cl._CustomList__data)
        self.assertEqual(0, len(self.cl._CustomList__data))

    def test_add_first_adds_as_first_element(self):
        self.assertEqual([5, 16, 17.5, "asd"], self.cl._CustomList__data)

        result = self.cl.add_first(100)

        self.assertIsNone(result)
        self.assertEqual([100, 5, 16, 17.5, "asd"], self.cl._CustomList__data)

    def test_dictionize_even_nums(self):
        self.assertEqual([5, 16, 17.5, "asd"], self.cl._CustomList__data)

        result = self.cl.dictionize()

        self.assertEqual({5: 16, 17.5: "asd"}, result)

        self.assertEqual([5, 16, 17.5, "asd"], self.cl._CustomList__data)

    def test_dictionize_odd_nums(self):
        self.cl.append(100)
        self.assertEqual([5, 16, 17.5, "asd", 100], self.cl._CustomList__data)

        result = self.cl.dictionize()

        self.assertEqual({5: 16, 17.5: "asd", 100: " "}, result)

        self.assertEqual([5, 16, 17.5, "asd", 100], self.cl._CustomList__data)

    def test_move_n_elements_are_moved_to_the_end(self):
        self.assertEqual([5, 16, 17.5, "asd"], self.cl._CustomList__data)

        result = self.cl.move(2)

        self.assertEqual([17.5, "asd", 5, 16,], result)
        self.assertEqual([17.5, "asd", 5, 16,], self.cl._CustomList__data)

    def test_move_bigger(self):
        self.assertEqual([5, 16, 17.5, "asd"], self.cl._CustomList__data)
        result = self.cl.move(5)

        self.assertEqual([5, 16, 17.5, "asd"], self.cl._CustomList__data)

    def test_sum(self):
        self.assertEqual([5, 16, 17.5, "asd"], self.cl._CustomList__data)

        expected_result = sum([5, 16, 17.5]) + len("asd")
        result = self.cl.sum()

        self.assertEqual(expected_result, result)
        self.assertEqual([5, 16, 17.5, "asd"], self.cl._CustomList__data)

    def test_overbound_returns_biggest_or_longest_element(self):
        self.assertEqual([5, 16, 17.5, "asd"], self.cl._CustomList__data)

        result = self.cl.overbound()

        self.assertEqual(2, result)
        self.assertEqual([5, 16, 17.5, "asd"], self.cl._CustomList__data)

        self.cl.append("a"*18)
        result = self.cl.overbound()
        self.assertEqual(4, result)
        self.assertEqual([5, 16, 17.5, "asd", "a"*18], self.cl._CustomList__data)

    def test_underbound_returns_smallest_or_longest_element(self):
        self.assertEqual([5, 16, 17.5, "asd"], self.cl._CustomList__data)

        result = self.cl.underbound()

        self.assertEqual(3, result)
        self.assertEqual([5, 16, 17.5, "asd"], self.cl._CustomList__data)

        self.cl.append("a"*18)
        self.cl.remove(3)
        self.assertEqual([5, 16, 17.5, "a"*18], self.cl._CustomList__data)

        result = self.cl.underbound()
        self.assertEqual(0, result)
        self.assertEqual([5, 16, 17.5, "a"*18], self.cl._CustomList__data)



if __name__ == "__main__":
    main()