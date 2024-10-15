import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)
    return all_data

if __name__ == '__main__':
    # Список названий файлов с пробелом в имени
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейное чтение файлов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    print(f"Линейный вызов: {time.time() - start_time} секунд")

    # Многопроцессорное чтение файлов
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    print(f"Многопроцессорный вызов: {time.time() - start_time} секунд")
