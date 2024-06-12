def is_integer(n):
    try:
        if int(n) != n:
            return False
    except ValueError:
        return False
    return True


def evaluate_model(tp: int, fp: int, fn: int) -> float:
    if not is_integer(tp):
        print('tp must be int')
    elif not is_integer(fp):
        print('fp must be int')
    elif not is_integer(fn):
        print('fn must be int')
    else:
        if tp <= 0 or fp <= 0 or fn <= 0:
            print('tp and fp and fn must be greater than zero')
        precision = tp / (tp+fp)
        recall = tp / (tp+fn)
        f1_score = 2 * precision * recall / (precision + recall)
        print('precision is ', precision)
        print('recall is ', recall)
        print('f1_score is ', f1_score)


if __name__ == "__main__":
    evaluate_model(tp=2, fp=3, fn=4)
