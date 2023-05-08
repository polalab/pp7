from bubble_sort import bubble_sort
from insert_sort import insert_sort

class TestBubble:

    def test_bubble_sort_1(self):
        # remember about nice name
        case = [4, 6, 2, 90, 2032, 13345, 234535, 243465476865, 239534]
        assert sorted(case) == bubble_sort(case)

    def test_bubble_sort_2(self):
        # remember about nice name
        case = [4]
        assert [4] == bubble_sort(case)

    def test_bubble_sort_3(self):
        # remember about nice name
        case = [4, 453, 2345, 2345, 32]
        assert sorted(case) == bubble_sort(case)

class TestSortInsert:

    def test_insert_sort_1(self):
        case = [6666, 6989, 6074, 6969, 6996, 6699, 6669]
        assert sorted(case) == insert_sort(case)

    def test_insert_sort_2(self):
        case = []
        assert sorted(case) == insert_sort(case)

    def test_insert_sort_3(self):
        case = [3, 3, 2, 1]
        assert sorted(case) == insert_sort(case)
