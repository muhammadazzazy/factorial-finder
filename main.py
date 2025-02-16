from sys import exit


def iter_fact(n: int) -> int:
    fact: int = 1
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
    exit_message: str = 'Exiting program...'
    print('Welcome to The Factorial Finder!')
    while True:
        try:
            user_input: str = input('Enter a number: ')
            if user_input == 'exit':
                print(exit_message)
                exit()

            n: int = int(user_input)
        except ValueError:
            print('Please enter valid input...')
            continue
        except KeyboardInterrupt:
            print(exit_message)
            exit()

        print(f'Iterative: {n}! = {iter_fact(n)}')

        print(f'Recursive: {n}! = {recurs_fact(n)}')


if __name__ == '__main__':
    main()
