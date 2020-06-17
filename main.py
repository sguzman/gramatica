import sys
from typing import List
from typing import Dict
from typing import IO
from typing import Tuple


def top(count: Dict[str, int], n: int) -> List[Tuple[str, int]]:
    top_count: List[Tuple[str, int]] = [(k, v) for k, v in count.items()]
    sorted_list: List[Tuple[str, int]] =\
        sorted(top_count, key=lambda t: t[1], reverse=True)

    return sorted_list[:n]


def tally(lists: List[List[str]]) -> Dict[str, int]:
    count: Dict[str, int] = dict()
    for alist in lists:
        for k in alist:
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

    tallied: Dict[str, int] = tally(lists)
    ranked: List[Tuple[str, int]] = top(tallied, 10)

    for line in ranked:
        print(line)


if __name__ == '__main__':
    main()
