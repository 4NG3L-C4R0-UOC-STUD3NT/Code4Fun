def merge_the_tools(string, k):
    subsegments = [string[i:i+k] for i in range(0, len(string), k)]
    for subsegment in subsegments:
        print("".join(dict.fromkeys(subsegment)))

merge_the_tools('AABCAAADA', 3)