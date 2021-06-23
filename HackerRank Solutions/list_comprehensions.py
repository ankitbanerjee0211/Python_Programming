from itertools import permutations
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])
    # main_list = []
    # num = max(x, y, z)
    # for i in range(num + 1):
    #     same = [i, i, i]
    #     main_list.append(same)
    #     for k in range(num + 1):
    #         for j in range(3):
    #             if i == 0:
    #                 two_same = [0, 0, 0]
    #             else:
    #                 two_same = [i, i, i]
    #             two_same[j] = k
    #             if two_same not in main_list:
    #                 main_list.append(two_same)
    # s = ''
    # for z in range(num + 1):
    #     s += str(z)

    # perm_list = permutations(s)
    # for perm in perm_list:
    #     temp_list = []
    #     for letter in perm:
    #         temp_list.append(int(letter))
    #     main_list.append(temp_list)

    # del_list = []
    # for element in main_list:
    #     if sum(element) == n or len(element) == 2:
    #         del_list.append(element)
    
    # for item in del_list:
    #     if item in main_list:
    #         main_list.remove(item)

    # print(main_list)
