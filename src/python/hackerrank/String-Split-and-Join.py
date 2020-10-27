def split_and_join(line):
    parts = line.split()
    result = "-".join(parts)
    return result

line = input()
result = split_and_join(line)
print(result)