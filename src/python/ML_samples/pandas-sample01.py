# https://realpython.com/tutorials/data-science/
# https://github.com/unitedstates/congress-legislators

import pandas as pd
import datetime as dt

# Use 3 decimal places in output display
pd.set_option("display.precision", 3)

# Don't wrap repr(DataFrame) across additional lines
pd.set_option("display.expand_frame_repr", False)

# Set max rows displayed in output to 25
pd.set_option("display.max_rows", 25)

dtypes = {
    "first_name": "category",
    "gender": "category",
    "type": "category",
    "state": "category",
    "party": "category",
}

df = pd.read_csv(
    "data/legislators-historical.csv",
    dtype=dtypes,
    usecols=list(dtypes) + ["birthday", "last_name"],
    parse_dates=["birthday"]
)

df.tail()
df.dtypes

n_by_state = df.groupby("state")["last_name"].count()
n_by_state.head(10)

df.groupby(["state", "gender"])["last_name"].count()

n_by_state_gender = df.groupby(["state", "gender"])["last_name"].count()
type(n_by_state_gender)
n_by_state_gender.index[:5]

df.groupby(["state", "gender"], as_index=False)["last_name"].count()

df.groupby("state", sort=False)["last_name"].count()

by_state = df.groupby("state")
print(by_state)

for state, frame in by_state:
    print(f"First 2 entries for {state!r}")
    print("------------------------")
    print(frame.head(2), end="\n\n")

by_state.groups["PA"]

by_state.get_group("PA")

state, frame = next(iter(by_state))  # First tuple from iterator
state
frame.head(3)

df.groupby("state")["last_name"].count()

frame["last_name"].count()  # Count for state == 'AK'
