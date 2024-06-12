

def find_levenshtein_distance(source, target):
    cache = [[float("inf") for _ in range(len(target)+1)]
             for _ in range(len(source)+1)]
    for i in range(len(target)+1):
        cache[0][i] = i
    for i in range(len(source)+1):
        cache[i][0] = i

    for i in range(1, len(source) + 1):
        for j in range(1, len(target) + 1):
            if source[i - 1] == target[j - 1]:
                cache[i][j] = cache[i - 1][j - 1]
            else:
                cache[i][j] = min(
                    cache[i][j - 1], min(cache[i - 1][j], cache[i - 1][j - 1])) + 1
    return cache[len(source)][len(target)]


if __name__ == "__main__":
    source = 'kitten'
    target = 'sitting'
    print(find_levenshtein_distance(source=source, target=target))
