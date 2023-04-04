from ting_file_management.priority_queue import PriorityQueue
import pytest

mock = [{"qtd_linhas": 6},
        {"qtd_linhas": 7},
        {"qtd_linhas": 8},
        {"qtd_linhas": 4}]


def test_basic_priority_queueing():
    priority = PriorityQueue()

    priority.enqueue(mock[0])
    priority.enqueue(mock[1])
    priority.enqueue(mock[2])
    priority.enqueue(mock[3])

    assert len(priority) == 4

    valor0 = priority.search(0)
    valor1 = priority.search(1)
    valor2 = priority.search(2)
    print(valor0)

    assert valor0['qtd_linhas'] == 4
    assert valor1['qtd_linhas'] == 6
    assert valor2['qtd_linhas'] == 7

    priority.dequeue()

    valor3 = priority.search(0)
    assert valor3['qtd_linhas'] == 6

    with pytest.raises(IndexError):
        priority.search(10)
