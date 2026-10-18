# Clustering Clinical Trials

> **Status: archived (2023).** Coursework project, kept for reference and no longer maintained.

Data preparation for clustering clinical-trial records. This repository holds the dataset and the scripts that prepare it; it does not contain the clustering code itself.

## Contents

| Path | What it is |
|---|---|
| `dataset/cart_clinical_trials_txt/` | Raw pipe-delimited exports, one file per table |
| `dataset/cart_clinical_trials_csv/` | The same 47 tables converted to CSV, plus `ctg-studies.csv` (a study-level export from ClinicalTrials.gov) |
| `dataset/txtToCsv.py` | Converts the raw `.txt` files to CSV |
| `dataset/extractAttributes.py` | Reads every CSV header and regenerates `dataset/README.md`, the data dictionary |
| `dataset/README.md` | Generated data dictionary: attributes of every table |

## Re-generate the data dictionary

```bash
python dataset/txtToCsv.py
python dataset/extractAttributes.py
```
