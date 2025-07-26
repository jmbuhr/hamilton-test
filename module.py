from hamilton.htypes import Parallelizable, Collect
import pandas as pd

N = 130
n = 10000

def dir() -> Parallelizable[str]:
    for i in range(N):
        dir = f"data/{i}"
        yield dir

def one_frame(dir: str) -> pd.DataFrame:
    df = pd.read_csv(f"{dir}/data.csv")
    return df

def result(one_frame: Collect[pd.DataFrame]) -> pd.DataFrame:
    combined = pd.concat(one_frame, axis=0, ignore_index=True)
    return combined
