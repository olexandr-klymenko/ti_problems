import re

if __name__ == "__main__":
    comlumns_n, rows_n = (int(el) for el in input().rstrip().split())
    src_matrix = []
    for _ in range(1, comlumns_n):
        src_matrix.append(input())

    # joined_src = "".join(chain.from_iterable(list(zip(*src_matrix))))
    joined_src = "".join([src_matrix[j][i] for i in range(rows_n) for j in range(comlumns_n)])
    pattern = r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])'
    result = re.sub(pattern, " ", joined_src)
    print(result)

