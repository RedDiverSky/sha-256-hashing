import hashlib
import itertools
import os
import time


# file generation function from project 2
def generate_file(file_name: str, file_size: int):
    with open(file_name + '.txt', 'wb') as file:
        file.write(os.urandom(file_size))


#
# task 1
#

def sha256_file_hash(file_name: str):
    with open(file_name + '.txt', 'rb') as file:
        file_contents = file.read()

    return hashlib.sha256(file_contents).digest()


def md5_file_hash(file_name: str):
    with open(file_name + '.txt', 'rb') as file:
        file_contents = file.read()

    return hashlib.md5(file_contents).digest()


def sha256_hashes_in_1_sec(file_name: str):
    num_of_hashes = 0
    elapsed_time = 0
    start_time = time.time()
    while elapsed_time < 1.0:
        sha256_file_hash(file_name)
        num_of_hashes += 1
        elapsed_time = time.time() - start_time
    print(file_name, "was hashed", num_of_hashes, "times by SHA-256 in 1 sec")


def md5_hashes_in_1_sec(file_name: str):
    num_of_hashes = 0
    elapsed_time = 0
    start_time = time.time()
    while elapsed_time < 1.0:
        md5_file_hash(file_name)
        num_of_hashes += 1
        elapsed_time = time.time() - start_time
    print(file_name, "was hashed", num_of_hashes, "times by MD5 in 1 sec")


def time_for_sha256_collision(file_name: str):
    target_hash = sha256_file_hash(file_name)

    i = 0
    elapsed_time = 0

    while True:
        test_value = i.to_bytes(8, byteorder='big')
        i += 1

        start_time = time.time()
        new_hash = hashlib.sha256(test_value).digest()
        end_time = time.time()
        elapsed_time += end_time - start_time

        if new_hash == target_hash:
            return elapsed_time


def time_for_collision(hash_name: str, file_name: str):
    if hash_name == "sha-256":
        target_hash = sha256_file_hash(file_name)
        hash_func = hashlib.sha256
    elif hash_name == "md5":
        target_hash = md5_file_hash(file_name)
        hash_func = hashlib.md5
    else:
        return

    i = 0
    elapsed_time = 0

    while True:
        test_value = i.to_bytes(8, byteorder='big')
        i += 1

        start_time = time.time()
        new_hash = hash_func(test_value).digest()
        end_time = time.time()
        elapsed_time += end_time - start_time

        if new_hash == target_hash:
            return elapsed_time


#
# task 2
#

def birthday_prefix(num_of_chars: int):
    target_prefix = "11221996"
    i = 0
    elapsed_time = 0

    while True:
        test_value = i.to_bytes(32, byteorder="big")
        i += 1

        start_time = time.time()
        new_hash = hashlib.sha256(test_value).hexdigest()
        end_time = time.time()
        elapsed_time += end_time - start_time

        if new_hash.startswith(target_prefix[:num_of_chars]):
            print("Found first", num_of_chars, "digits in", elapsed_time, "sec")
            print(new_hash)
            return


#
# task 3
#

def lowest_hash_value(strings_to_test, total_time: int):
    elapsed_time = 0
    # strings_to_test = itertools.permutations(string)

    lowest_hash = 'f' * 64

    while elapsed_time < total_time:
        # permutate the string
        string = ''.join(next(strings_to_test))

        # convert string to bytes
        data = bytes(string, 'utf-8')

        start_time = time.time()
        new_hash = hashlib.sha256(data).hexdigest()
        end_time = time.time()

        if new_hash < lowest_hash:
            lowest_hash = new_hash

        elapsed_time += end_time - start_time

    return lowest_hash


def avg_lowest_hash(string: str, total_time: int):
    total_hash_val = 0x00
    strings_to_test = itertools.permutations(string)

    for i in range(10):
        hash_val_str = lowest_hash_value(strings_to_test, total_time)
        hash_val_hex = int(hash_val_str, base=16)
        # print("Trial", i, hex(hash_val_hex))
        total_hash_val += hash_val_hex

    return '0x{:x}'.format(int(total_hash_val / 0x0a))


def main():
    # configure files
    # file_names = ["file0", "file1", "file2", "file3", "file4"]
    # file_sizes = [16, 156, 328, 641, 1000]
    #
    # for index in range(len(file_names)):
    #     generate_file(file_names[index], file_sizes[index])

    # task 1
    # for file_name in file_names:
    #     sha_256_hashes_in_1_sec(file_name)
    #     md5_hashes_in_1_sec(file_name)

    # sha256_collision_time = time_for_collision("sha-256", file_names[0])
    # print("It took", sha256_collision_time, "sec to find a collision for", file_names[0],
    #       "of size", file_sizes[0], "with SHA-256")
    # md5_collision_time = time_for_collision("md5", file_names[0])
    # print("It took", md5_collision_time, "sec to find a collision for", file_names[0], "of size",
    #       file_sizes[0], "with MD5")

    # task 2
    # for i in range(1, 9):
    #     birthday_prefix(i)

    # task 3
    string = "supercalifragilisticexpialidocious"

    lowest_hash_in_10 = avg_lowest_hash(string, 10)
    print("The avg lowest hash value produced in 10 sec was", lowest_hash_in_10)

    lowest_hash_in_20 = avg_lowest_hash(string, 20)
    print("The avg lowest hash value produced in 20 sec was", lowest_hash_in_20)

    lowest_hash_in_30 = avg_lowest_hash(string, 30)
    print("The avg lowest hash value produced in 30 sec was", lowest_hash_in_30)


main()
