def minion_game(string):
    # your code goes here
    names = ['Stuart', 'Kevin']
    vowels = ['A', 'E', 'I', 'O', 'U']
    s_points = 0
    k_points = 0
    string = string.upper()

    for i in range(len(string)):
        if s[i] in vowels:
            k_points += len(string) - i
        else:
            s_points += len(string) - i

    if s_points > k_points:
        print('Stuart {}'.format(s_points))
    elif s_points < k_points:
        print('Kevin {}'.format(k_points))
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)