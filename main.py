import sys
from typing import Dict
from typing import IO
from typing import List
from typing import Tuple


Lexeme = List[str]
Freq = Tuple[Lexeme, int]
WordDict = Dict[Lexeme, int]


# Yield successive n-sized
# chunks from l.
def chunk(alist: Lexeme, n: int) -> Lexeme:
    # looping till length l
    for i in range(0, len(alist), n):
        word: str = alist[i:i+n]

        yield word


def top(count: WordDict, n: int) -> List[Freq]:
    top_count: List[Freq] = []
    for k, v in count.items():
        tup: Freq = (k, v)
        top_count.append(tup)

    sorted_list: List[Freq] =\
        sorted(top_count, key=lambda t: t[1], reverse=True)

    return sorted_list[:n]


def tally(lists: List[Lexeme], n: int) -> WordDict:
    count: WordDict = dict()

    for alist in lists:
        chunky_soup = chunk(alist, n)
        for chunked in chunky_soup:
            for k in chunked:
                if k not in count:
                    count[k] = 1
                else:
                    count[k] = count[k] + 1

    return count


def main() -> None:
    if len(sys.argv) < 2:
        print('No args passed')
        sys.exit(1)

    files: List[str] = sys.argv[1:]
    lists: List[List[str]] = []
    for file in files:
        io: IO = open(file, 'r')
        array: List[str] = list(io.read())
        lists.append(array)

    tallied: Dict[str, int] = tally(lists, 2)
    ranked: List[Tuple[str, int]] = top(tallied, 10)

    for line in ranked:
        print(line)


if __name__ == '__main__':
    main()
