import os
import random
import argparse


def make_split(image_dir, out_dir, ratio=0.8, seed=42):
    random.seed(seed)
    files = sorted(os.listdir(image_dir))
    random.shuffle(files)

    n_train = int(len(files) * ratio)
    train_files = files[:n_train]
    val_files = files[n_train:]

    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "train.txt"), "w") as f:
        f.write("\n".join(train_files))
    with open(os.path.join(out_dir, "val.txt"), "w") as f:
        f.write("\n".join(val_files))

    print(f"Train: {len(train_files)} | Val: {len(val_files)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image_dir", type=str, required=True)
    parser.add_argument("--out_dir", type=str, default="splits")
    parser.add_argument("--ratio", type=float, default=0.8)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    make_split(args.image_dir, args.out_dir, args.ratio, args.seed)