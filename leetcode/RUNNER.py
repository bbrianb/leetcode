import money_2591


def main(function, file_name):
    test_cases = file_name.test_cases
    accuracy = [0, 0]
    for c in test_cases:
        input_data = c['input']
        output = function(*input_data)
        answers = c['output']
        accuracy[0] += int(output in answers)
        accuracy[1] += 1
        print(f'{input_data=}, {output=}, {answers=}, {output in answers=}, {accuracy[0]/accuracy[1]:.3f}')

if __name__ == '__main__':
    file = money_2591
    func = file.Solution().distMoney
    main(func, file)