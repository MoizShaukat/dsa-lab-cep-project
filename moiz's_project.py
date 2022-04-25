import time


# Time Complexity: O(n)

def find(hash_table, tsize, key):
    for i in range(tsize):
        hash = key % tsize

        if hash_table[hash][0] == key:
            return hash_table[hash]
        else:
            is_found = False
            for j in range(tsize):
                new_hash = (hash + j*j) % tsize
                if hash_table[new_hash][0] == key:
                    is_found = True
                    return hash_table[new_hash]

            if not is_found:
                for j in range(tsize):
                    new_hash = (hash + j) % tsize
                    if hash_table[new_hash][0] == key:
                        return hash_table[new_hash]


def hashing(hash_table, tsize, arr, N):
    for i in range(N):
        hash = arr[i][0] % tsize

        if hash_table[hash] == -1:
            hash_table[hash] = arr[i]
        else:
            is_found = False
            for j in range(tsize):
                new_hash = (hash + j*j) % tsize
                if hash_table[new_hash] == -1:
                    is_found = True
                    hash_table[new_hash] = arr[i]
                    break

            if not is_found:
                for j in range(tsize):
                    new_hash = (hash + j) % tsize
                    if hash_table[new_hash] == -1:
                        is_found = True
                        hash_table[new_hash] = arr[i]
                        break

    #print_array(hash_table, N)


def print_array(arr, N):
    for i in range(N):
        print("employee id: {} ".format(arr[i][0]))
        print("employee name: {} ".format(arr[i][1]))
        print("employee city: {} ".format(arr[i][2]))
        print("employee service category: {} \n".format(arr[i][3]))

# hashing(ht, L, t, N)


def print_sorted_data(arr):
    print('Following is the data of hash table in sorted order\n')
    for i in range(len(arr)):
        print("employee id: {} ".format(arr[i][0]))
        print("employee name: {} ".format(arr[i][1]))
        print("employee city: {} ".format(arr[i][2]))
        print("employee service category: {} \n".format(arr[i][3]))


def _delete(arr, half_arr):
    for i in range(len(arr)):
        if not arr[i][0] % 2 == 0:
            half_arr.append(arr[i])


# print(sorted(ht))
data = []
with open("data_100000.txt", "r") as f:
    lines = f.readlines()
    del lines[0:2]
    for line in lines:
        parsed_line = line.strip().split("\t")
        parsed_line_int = [int(parsed_line[0])]
        parsed_line_int.extend(parsed_line[1:])

        data.append(parsed_line_int)
    # print(len(data))
    # print(len(lines))
    c_time = time.time()
    sorted_data = sorted(data)
    # print_sorted_data(sorted_data)
    print(len(sorted_data))
    d_time = time.time()
    sort_time = (d_time - c_time) * 1000


N = len(data)
L = len(data)
ht = [-1] * N
s_time = time.time()
hashing(ht, L, data, N)
e_time = time.time()
insert_time = (e_time - s_time) * 1000
# print(ht)


idee = int(input('enter the employee Id: '))
x_time = time.time()
item = find(ht, N, idee)
y_time = time.time()
find_time = (y_time - x_time) * 1000
print('\nemployee details against this Id\n{}'.format(item))
# print(ht)
# for l in ht:
#   print(type(l))
# print(ht)

odd_arr = []
l_time = time.time()
_delete(data, odd_arr)
o_time = time.time()
del_time = (o_time - l_time) * 1000
print('\nlength of array after deletion: {}'.format(len(odd_arr)))


'''bla = []
l_time = time.time()
del(ht[int(len(ht)/2):])
o_time = time.time()
del_time = (o_time - l_time) * 1000
print(len(ht))'''


print('\nNumber of records: {}\n'.format(len(data)))
print('Insert                Execution time: {} sec'.format(insert_time))
print('Find                  Execution time: {} sec'.format(find_time))
print('Sorted Traversal      Execution time: {} sec'.format(sort_time))
print('Delete                Execution time: {} sec\n'.format(del_time))
