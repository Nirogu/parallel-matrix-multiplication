# Parallel matrix multiplication

Performance tests for parallel matrix multiplication algorithms.

## Usage

1. Install the required python libraries, found in `requirements.txt`. The following command shows how to do it using `pip`, but `conda` or any package manager can also be used.

```shell
pip install -r requirements.txt
```

2. Build the matrix multiplication executable using `make`.

```shell
cd MatMult
make
```

3. Run the experiments using the launcher.

```shell
cd ..
python launcher.py
```

4. Generate the graphics.

```shell
python graphics.py experiments.csv results.png
```
