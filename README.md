## Environment

Experiments were run on:
- OS: Ubuntu 20.04
- Python: 3.8
- PyTorch: 1.11.0
- CUDA: 11.3
- GPU: NVIDIA RTX 2080 Ti (11 GB)

Setup:

    conda env create -f environment.yml
    conda activate ga-sar-det

## Dataset Split

SSDD is split into train/val/test with an 8:2 (train:test) ratio, following
the protocol reported in the paper. The exact file lists used are provided
in the `splits/` folder:

- `splits/ssdd_train.txt`
- `splits/ssdd_val.txt`
- `splits/ssdd_test.txt`
- `splits/hrsid_train.txt`
- `splits/hrsid_test.txt`

These splits were generated with a fixed random seed (42). To regenerate an
identical split:

    python tools/make_split.py --image_dir /path/to/images --out_dir splits --ratio 0.8 --seed 42

Using these exact split files is required to reproduce the reported results.

## Reproducibility

All experiments use a fixed random seed of **42**, applied to:

- Python `random`
- NumPy
- PyTorch (CPU & CUDA)
- Dataset splitting

The seed is set explicitly in `train.py` via `set_seed()` before training
starts, and is also recorded in `ga-sar-det.yaml` (`seed: 42`).