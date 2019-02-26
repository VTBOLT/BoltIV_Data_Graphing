import csv, sys, getopt
import matplotlib.pyplot as plt

def main(argv):
    x=[]
    y=[]
    x.append(input("enter x val: "))
    y.append(input("enter y val: "))
    plt.ion()
    plt.plot(x,y)
    plt.show()
    while 1:
        try:
            plt.plot(x,y)
            plt.autoscale()
            plt.draw()
            x.append(input("enter x val: "))
            y.append(input("enter y val: "))
        except KeyboardInterrupt:
            raise
        

if __name__ == "__main__":
   main(sys.argv[1:])