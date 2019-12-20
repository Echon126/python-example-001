import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def with_pandas_read():
    df = pd.read_excel(r"E:\test\pandas.xlsx")
    data = df.head(10000)
    print(data)
    print("获取到所有值:\n{0}".format(data))


def with_pandas_group():
    dates = pd.date_range('20180310', periods=6)
    df = pd.DataFrame(np.random.rand(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
    print(df)


# 读取指定的单行，数据会存在列表里面
# data01 = df.loc[0].values
# print("读取指定行的数据:\n{0}".format(data01))
#
# data02 = df.loc[[1, 2]].values

# print("")

def with_numpy():
    x = np.arange(1, 100)
    y = 2 * x + 5
    plt.title("MatplotLib demo")
    plt.xlabel("x axis caption")
    plt.ylabel("y axis caption")
    plt.plot(x, y)
    plt.show()


if __name__ == "__main__":
    with_pandas_read()
    with_numpy()
