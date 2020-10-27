if __name__ == "__main__":
    n = int(input())
    array = list(input().split())
    allcond = all([int(x) > 0 for x in array])
    anycond = any([x == x[::-1] for x in array])
    print(all([allcond, anycond]))