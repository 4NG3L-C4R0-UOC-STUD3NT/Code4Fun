def count_substring(string, sub_string):
    result = 0
    for i in range(0, len(string) - len(sub_string) + 1):
        if string[i:i+len(sub_string)] == sub_string:
            result += 1
    return result

if __name__ == '__main__':
    #string = input().strip()
    #sub_string = input().strip()
    string = 'ABCDCDC'
    sub_string = 'CDC'
    
    count = count_substring(string, sub_string)
    print(count)