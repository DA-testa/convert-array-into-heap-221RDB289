# python3
# Autors: Gundars Pelle 6. grupa


def build_heap(data):
    swaps = []

    # Creates a heap and heap sort
    # try to achieve  O(n) and not O(n2)

    n = len(data)
    for i in range(n//2,-1,-1):
        while 2*i + 1 <= n-1:
            j = 2*i + 1
            if j + 1 <= n-1 and data[j + 1] < data[j]:
                j += 1

            if data[i] <= data[j]:
                break

            swaps.append((i, j))
            data[i], data[j] = data[j], data[i]
            i = j

    return swaps


def main():

    mode = input()
    if mode.startswith('I'):
        # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))

    elif mode.startswith('F'):
        # input from file
        file_name = input()
        if 'a' not in file_name:
            f = open('tests/'+file_name, 'r')
            lines = f.read().split('\n')
            f.close()

            n = int(lines[0])
            data = list(map(int, lines[1].split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # outputs how many swaps were made,
    # this number should be less than 4n (less than 4*len(data))
    m=len(swaps)
    if m < 4*len(data):
        print(m)

        # outputs all swaps
        for i, j in swaps:
            print(i, j)


if __name__ == "__main__":
    main()
