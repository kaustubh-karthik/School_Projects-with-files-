# Sorts names by mark
# If students have the same mark, they're sorted by alphabet
with open('marks.txt', 'r') as marks:
    file_len = len(marks.readlines())
    marks.seek(0)
    marks_lines = [marks.readline().split(',') for line in range(file_len)]
    marks_lines = sorted(marks_lines[1:], key=lambda x: [100 - int(x[1]), x[0]])
    print(*sum(marks_lines, []), sep='\n')

'''with open('marks.txt', 'r') as marks:
    file_len = len(marks.readlines())
    marks.seek(0)
    print(*sum(sorted([marks.readline().split(',') for line in range(file_len)][1:], key=lambda x: x[1], reverse=True), []), sep='\n')
'''
