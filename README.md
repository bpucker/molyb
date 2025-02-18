# Identification and characterization of eukaryotic Mo-insertases

```
Usage:
  python3 calc_pos_conservation.py --in <FILE> --ref <FILE> --out <DIR>
  --in    STR    Input file (alignment)
  --ref   STR    Reference sequence name
  --out   STR    Output file

```

`--in` specifies the full path to the alignment file that serves as input. The alignment format needs to be FASTA.

`--ref` specifies the name of the reference sequence. This string must not contain any special characters.

`--out` specifies the full path to the output file.


```
Usage:
  python3 branch_length_comparison.py --tree <FILE> --groups <FILE> --out <DIR>
  --tree    STR    Input tree file
  --groups  STR    Input sequence group file
  --out     STR    Output folder

```

`--tree` specifies the full path to the input tree file.

`--groups` specifies the full path to the input groups file. TAB-separated text file that contains a sequence ID in the first column and a group ID in the second column.

`--out` specifies the full path to the output folder. This folder will be created if it does not exist already.



# References

This repository.
