if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    if query_name in student_marks:
        tong = 0
        for i in range(0, 3):
            tong+= student_marks[query_name][i]
        tbc = tong / 3
    print(f'{tbc:.2f}')