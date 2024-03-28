import polars as pl
import requests

def run_main():
    dat = pl.read_csv("../Experimenter_3220002w2_Load, Event_1637262682.dat", separator=' ')

    maxTime = dat.get_column("DatTime").max()
    time = dat.get_column("DatTime").min()

    while (time < maxTime):

        time += 0.167

if __name__ == '__main__':
    run_main()