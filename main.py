import multiprocessing


def square (number, return_dict):
    return_dict[number] = number**2


if __name__ == "__main__":
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    process = []
    numbers = [1, 3, 5, 7, 9, 11]
    for i in range(len(numbers)):
        p = multiprocessing.Process(target=square, args=(i, return_dict))
        process.append(p)
        p.start()  # запускам процессы в цикле

    # ожидаем окончания процессов
    for proc in process:
        proc.join()

    for number, squares in return_dict.items():
        print(str(number) + "^2"+" = " + str(squares))