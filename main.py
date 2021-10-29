import pandas as pd
import matplotlib.pyplot as plt


def main():
    data = pd.read_table("DS8.txt", " ")
    x = data.iloc[:, 0:1]
    y = data.iloc[:, 1:2]

    plt.figure(1, figsize=(5.4, 9.6), dpi=100)
    plt.scatter(y, x)
    plt.savefig('Result.png')
    plt.show()


if __name__ == '__main__':
    main()
