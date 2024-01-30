from typing import TypeAlias
# Tuples: TypeAlias = list[tuple[str, int]]

type Tuples = list[tuple[str, int]]
type GenTuples[T] = list[T] | list[tuple[T, int]]
IntOrStr: TypeAlias = int | str
type IntOrStr2 = int | str

def do_action(items: Tuples) -> None:
    pass

def do_action_2[T](items: GenTuples[T]) -> None:
    pass

def main() -> None:
    do_action([('A', 1), ('B', 2)])
    # do_action([10, 20])

    do_action_2([10, 20, 30])
    do_action_2([('A', 1), ('B', 2)])

    print(isinstance(20, IntOrStr))
    print(isinstance('ala', IntOrStr))
    print(isinstance(12.3, IntOrStr))

    print(isinstance(20, IntOrStr2))
    print(isinstance('ala', IntOrStr2))
    print(isinstance(12.3, IntOrStr2))

if __name__ == '__main__':
    main()
