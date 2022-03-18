with open('A.txt') as F:
    f = list(map(int, F.readlines()))
    f.pop(0)

    div107Even = []
    div107Odd = []
    even = []
    odd = []

    for x in f:
        if x % 107 == 0:
            if x % 2 == 0:
                div107Even.append(x)
            else:
                div107Odd.append(x)
        else:
            if x % 2 == 0:
                even.append(x)
            else:
                odd.append(x)

    print('div107Even:', max(div107Even))
    print('div107Odd:', max(div107Odd))
    print('even:', max(even))
    print('odd:', max(odd))
    print('')
    print('A:', 94169977)
    print('B:', 963998)
