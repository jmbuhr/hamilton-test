import pandas as pd
from module import N

def dir() -> list[str]:
    dirs = []
    for i in range(N):
        dir = f"data/{i}"
        dirs.append(dir)
    return dirs

def result(dir: list[str]) -> pd.DataFrame:
    frames = []
    for d in dir:
        df = pd.read_csv(f"{d}/data.csv")
        frames.append(df)
    combined = pd.concat(frames, axis=0, ignore_index=True)
    return combined
