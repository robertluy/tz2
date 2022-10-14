def _min(sps):
    min_val = sps[0]
    for i in range(1, len(sps)):
        if sps[i] < min_val:
            min_val = sps[i]
    return min_val


def _max(sps):
    max_val = sps[0]
    for i in range(1, len(sps)):
        if sps[i] > max_val:
            max_val = sps[i]
    return max_val


def _sum(sps):
    sumi = 0
    for i in sps:
        sumi += i
    return sumi


def _mult(sps):
    _mult = 1
    for i in range(len(sps)):
        _mult *= sps[i]
    return _mult


if __name__ == '__main__':
    f = open(input('File name:'), 'r')
    sps = list(map(int, f.readline().split()))
    f.close()
    print('Result _min', _min(sps), sep='\n')
    print('Result _max', _max(sps), sep='\n')
    print('Result _msum', _sum(sps), sep='\n')
    print('Result _mult', _mult(sps), sep='\n')
    #проверка скорости при увеличении размера файла осуществлена для функции _sum()