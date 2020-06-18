import sys
from typing import Dict
from typing import IO
from typing import List
from typing import Tuple


# Yield successive n-sized
# chunks from l.
def chunk(alist: str, n: int) -> str:
    # looping till length l
    for i in range(0, len(alist), n):
        word: str = alist[i:i+n]

        yield word


def tally(lists: List[List[str]], n: int) -> Dict[str, int]:
    count: Dict[str, int] = dict()

    for alist in lists:
        chunky_soup = chunk(alist, n)
        for chunked in chunky_soup:
            chunked_str: str = ''.join(chunked)
            if chunked_str not in count:
                count[chunked_str] = 1
            else:
                count[chunked_str] = count[chunked_str] + 1

    return count


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

    tallied: WordDict = tally(lists, 2)
    ranked: List[Tuple[str, int]] = top(tallied, 10)

    for line in ranked:
        print(list(line[0]), line[1])


if __name__ == '__main__':
    main()
