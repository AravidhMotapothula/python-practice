# Problem: Average Marks
# Given a dictionary of student names and marks, print the
# average marks of a queried student to 2 decimal places.
# Source: HackerRank - Python Dictionaries
if __name__ == '__main__':
    n = int(input())
    d = {}

    for i in range(n):
        line = input().split()
        name = line[0]
        marks = [float(x) for x in line[1:]]
        d[name] = marks

    query_name = input()
    avg = sum(d[query_name]) / len(d[query_name])
    print(f"{avg:.2f}")