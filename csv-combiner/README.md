# CSV Combiner

Write a command line program that takes several CSV files as arguments. Each CSV
file (found in the `fixtures` directory of this repo) will have the same
columns. Your script should output a new CSV file to `stdout` that contains the
rows from each of the inputs along with an additional column that has the
filename from which the row came (only the file's basename, not the entire path).
Use `filename` as the header for the additional column.

## Example of Running Program
We can run this program from the command line similar to below, as long as your machine has python installed.

Given two input files named `clothing.csv` and `accessories.csv`.

```
$ python csv_combiner.py ./fixtures/accessories.csv ./fixtures/clothing.csv > combined.csv
```

