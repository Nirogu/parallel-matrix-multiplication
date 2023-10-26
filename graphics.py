from argparse import ArgumentParser

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

parser = ArgumentParser(description="Create graphics from the experiments data.")
parser.add_argument(
    "input_file",
    help="CSV file to be read and processed. Should be output of launcher.py",
)
parser.add_argument("output_file", help="File where graphic will be saved.")
args = parser.parse_args()

data = pd.read_csv(args.input_file)
data["N_Threads"] = data["N_Threads"].astype(str)
data["Time (secs)"] = data["Time"] * 10**-6
ax = sns.lineplot(
    data, x="Matrix_Size", y="Time (secs)", hue="N_Threads", palette="plasma"
)
ax.grid(axis="both", which="both", linestyle="--")
ax.set_title("Matrix size vs Time for every number of threads")
ax.set_xlim(200, 2000)
plt.savefig(args.output_file)
