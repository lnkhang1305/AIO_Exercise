import streamlit as st


def edit_distance(target, source):
    cache = [[0] * (len(source)+1) for _ in range(len(target)+1)]
    for i in range(len(target)):
        cache[0][i] = i
    for i in range(len(source)):
        cache[i][0] = i
    
    for i in range(1, len(target) + 1):
        for j in range(1, len(source) + 1):
            if target[i - 1] == source[j - 1]:
                cache[i][j] = cache[i-1][j-1]
            else:
                cache[i][j] = min(cache[i-1][j], min(cache[i][j-1],cache[i-1][j-1])) + 1
    return cache[len(target)][len(source)]


def gen_streamlit():
    