from argparse import ArgumentParser

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.colors import LogNorm

parser = ArgumentParser(description="Create graphics from the experiments data.")
parser.add_argument(
    "input_file",
    help="CSV file to be read and processed. Should be output of launcher.py",
)
args = parser.parse_args()

input_file = args.input_file
data = pd.read_csv(input_file)
data["Time (secs)"] = data["Time"] * 10**-6

heatmap = data.pivot_table(
    values="Time (secs)", index="Matrix_Size", columns="N_Threads", aggfunc="mean"
)
ax = sns.heatmap(heatmap, norm=LogNorm())
ax.set_title("Time values (in seconds) for every experiment")
plt.savefig("img/size-threads-time.png")
plt.clf()
plt.cla()

ax = sns.lineplot(
    data, x="N_Threads", y="Time (secs)", hue="Matrix_Size", palette="plasma"
)
ax.set_xticks(range(2, 21, 2))
ax.set_xlim(2, 20)
ax.grid(axis="both", which="both", linestyle="--")
ax.set_title("Number of threads vs Time for some matrix sizes")
plt.savefig("img/threads-time.png")
plt.clf()
plt.cla()

data["N_Threads"] = data["N_Threads"].astype(str)
ax = sns.lineplot(
    data, x="Matrix_Size", y="Time (secs)", hue="N_Threads", palette="plasma"
)
ax.grid(axis="both", which="both", linestyle="--")
ax.set_title("Matrix size vs Time for every number of threads")
ax.set_xlim(200, 2000)
plt.savefig("img/size-time.png")
