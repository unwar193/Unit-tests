import pytest
from typing import List
from homework6.app.compare_avgs import CompareAvgs

class TestCompareAvgsOfLists():

    def setup_method(self) -> None:
        self.avgs = CompareAvgs()

    def teardown_method(self) -> None:
        print('Calculation done')

    @pytest.fixture
    def list_2(self) -> List[int]:
        """ list_2 is constant. """
        return [1, 2, 3]

    @pytest.fixture
    def empty_list(self):
        """ Empty list. """
        return []

    @pytest.mark.parametrize('list_1, expected', [
        ([10, 20, 30], CompareAvgs.STR_1),
        ([1, 1, 1, 1, 1], CompareAvgs.STR_2),
        ([1, 2, 3], CompareAvgs.STR_3)
    ], ids=['больше первое', 'больше второе', 'равны'])
    def test_compare_avgs(self, list_1, list_2, expected):
        """ Comparing of list averages check. """
        assert self.avgs.compare_avgs(list_1, list_2) == expected

    @pytest.mark.parametrize('num_list', [
        [2, 4, 6, 8, 10],
        [1, 3, 5, 7, 9]
    ])
    def test_calc_avg(self, num_list):
        """ Calculation of list average check. """
        assert self.avgs.calc_avg(num_list) == sum(num_list) / len(num_list)

    def test_calc_avg_null_list(self, empty_list):
        """ Average calculation of empty list check. """
        assert self.avgs.calc_avg(empty_list) is None

    def test_compare_avgs_null_list(self, empty_list, list_2):
        """ Comparing of empty list averages check. """
        with pytest.raises(TypeError):
            self.avgs.compare_avgs(empty_list, list_2)

if __name__ == '__main__':
    pytest.main(['-v'])