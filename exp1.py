
import matplotlib.pyplot as plt


def impulse():
    x=[i for i in range(-10,20)]
    y=[0 if i!=0 else 1 for i in x]
    plt.stem(x, y)
    plt.show()


def step():
    x=[i for i in range(-10,20)]
    y=[0 if i<0 else 1 for i in x]
    plt.stem(x, y)
    plt.show()

def expo():
    x=[i for i in range(-10,20)]
    y=[0 if i<0 else pow(2,i) for i in x]
    plt.stem(x, y)
    plt.show()

def ramp():
    x=[i for i in range(-10,20)]
    y=[0 if i<0 else i for i in x]
    plt.stem(x, y)
    plt.show()


impulse()
step()
expo()
ramp()
