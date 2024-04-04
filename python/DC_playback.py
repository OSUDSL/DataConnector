import polars as pl
import requests
import time
import tqdm

def run_main():
    dat = pl.read_csv("../Experimenter_3220002w2_Load, Event_1637262682.dat", separator=' ')

    start_time = time.time()
    max_time = dat.get_column("DatTime").max()

    pbar = tqdm.tqdm(total=max_time)
    curr_time = 0

    # make a post request every 0.05 seconds
    while True:
        # access the time elapsed
        prev_time = curr_time
        curr_time = time.time() - start_time
        try:
            df_row = dat.filter(dat.get_column("DatTime") > curr_time).row(0, named=True)
        except pl.exceptions.RowsError:
            break
        velocity = df_row["Velocity"]
        xpos = df_row["XPos"]
        time_to_send = df_row["DatTime"]

        if velocity == None:
            break
        # store the values in a dict
        data = {
            "Velocity": velocity,
            "XPos": xpos,
            "Time": time_to_send
        }
        r = requests.post('http://127.0.0.1:5000/update', json=data)
        pbar.update(curr_time - prev_time)
        time.sleep(0.025)
    pbar.close()

if __name__ == '__main__':
    run_main()