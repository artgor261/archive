def main():
    n = int(input("Print N: "))
    tree = list()
    fill_tree(1, n, tree)
    print(tree)


def fill_tree(w, n, tree):
    x = w * 2
    if x <= n:
        fill_tree(x, n, tree)
        tree.append(w)
        if (x + 1) <= n:
            fill_tree(x + 1, n, tree)
    else:
        tree.append(w)


main()
