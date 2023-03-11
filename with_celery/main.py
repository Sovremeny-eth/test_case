import time
from tasks import fibonacci


def fibonacci_task(value_list):
    result = []
    for i in value_list:
        result.append(fibonacci.delay(i))

    for val in result:
        # or take logger
        while not val.ready():
            time.sleep(1)
            print(f'Task {val.task_id} is not ready')
        print(f'Fibonacci task {val.task_id} -> {val.get()}')


if __name__ == '__main__':
    fibonacci_task([10, 100, 56])
