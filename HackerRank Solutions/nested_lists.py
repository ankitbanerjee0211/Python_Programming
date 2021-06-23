if __name__ == '__main__':
    marksheet = []
    for _ in range(int(input())):
        marksheet.append([input(), float(input())])
    marks = []
    sec_low_list = []

    length = len(marksheet)
    for i in range(length):
        marks.append(marksheet[i][1])

    second_low = min(marks)

    marks.sort()
    
    for mark in marks:
        if mark > second_low:
            second_low = mark
            break

    for j in range(length):
        if second_low in marksheet[j]:
            sec_low_list.append(marksheet[j][0])

    sec_low_list.sort()

    for name in sec_low_list:
        print(name)

