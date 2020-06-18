import sys
from typing import Callable
from typing import Dict
from typing import IO
from typing import List
from typing import Tuple


"""
 Tuple[
 int - len(Lexeme)
 int - frequency
 int - strength
 int - (len(Lexeme) - 1) * frequency
 ]
"""
TupTup = Tuple[int, int, int, int]
TupFin = Tuple[str, int, int, int, int]


# Yield successive n-sized
# chunks from l.
def chunk(alist: str, n: int) -> str:
    # looping till length l
    for i in range(0, len(alist), n):
        word: str = alist[i:i+n]

        yield word


def tally(
        lists: List[List[str]],
        n: int,
        count: Dict[str, TupTup] = dict()
        ) -> Dict[str, TupTup]:

    temp: Dict[str, int] = dict()
    for alist in lists:
        chunky_soup = chunk(alist, n)
        for chunked in chunky_soup:
            chunked_str: str = ''.join(chunked)
            if chunked_str not in temp:
                temp[chunked_str] = 1
            else:
                temp[chunked_str] = temp[chunked_str] + 1

    for k, v in temp.items():
        count[k] = (len(k), v, len(k) * v, (len(k) - 1) * v)


def drop(
        alist: List[TupFin],
        funcs: List[Callable[[TupFin], List[TupFin]]] = List[lambda x: x]
        ) -> List[Tuple[str, int, int, int, int]]:

    alist_filtered: List[TupFin] = []
    for line in alist:
        values: List[bool] = []

        for f in funcs:
            values.append(f(line))

        if all(values):
            alist_filtered.append(line)

    return alist_filtered


def top(count: Dict[str, int], n: int) -> List[Tuple[str, int]]:
    top_count: List[Tuple[str, int]] = []

    for k, v in count.items():
        tup: Tuple[str, int] = (k, v)
        top_count.append(tup)

    sorted_list: List[Tuple[str, int]] =\
        sorted(top_count, key=lambda t: t[1], reverse=True)

    return sorted_list[:n]


def main() -> None:
    if len(sys.argv) < 2:
        print('No args passed')
        sys.exit(1)

    files: Lexeme = sys.argv[1:]
    lists: List[Lexeme] = []
    for file in files:
        io: IO = open(file, 'r')
        array: Lexeme = list(io.read())
        lists.append(array)

    count: Dict[str, int] = dict()
    for i in range(2, 20, 1):
        tally(lists, i, count)

    alist: List[Tuple[str, int, int, int, int]] = []
    for k, v in count.items():
        alist.append((k, v[0], v[1], v[2], v[3]))

    ranked: List[Tuple[str, int]] = top(count, 10)
    for line in ranked:
        print(list(line[0]), line[1])


if __name__ == '__main__':
    main()
