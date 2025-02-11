from sys import exit


def iter_fact(n: int) -> int:
    fact = 1
    if n == 0 or n == 1:
        return fact
    while n > 0:
        fact *= n
        n -= 1

    return fact


def recurs_fact(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * recurs_fact(n-1)


def main() -> None:
    while True:
        try:
            user_input = input('Enter a number: ')
            if user_input == 'exit':
                print('Thanks for trying my program!')
                exit()

            n = int(user_input)
            print(f'Iterative: {n}! = {iter_fact(n)}')
            print(f'Recursive: {n}! = {recurs_fact(n)}')
        except ValueError:
            print('Invalid input...')
            continue
        except KeyboardInterrupt:
            print('Exiting...')
            exit()


if __name__ == '__main__':
    main()
