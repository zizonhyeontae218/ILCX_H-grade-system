#!/usr/bin/env python3
import argparse


def label(score: int) -> str:
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    if score % 5 != 0:
        raise ValueError("invalid ILCX total: binary category scoring only produces multiples of 5")
    if score == 100:
        return "ILCX 10H grade"
    base = score // 10
    plus = "+" if score % 10 >= 5 else ""
    return f"ILCX {base}H{plus} grade"


def main():
    p = argparse.ArgumentParser(
        description="Convert a valid binary ILCX H-grade total into its canonical label."
    )
    p.add_argument("score", type=int, help="valid ILCX total from 0 to 100 in 5-point increments")
    args = p.parse_args()
    print(label(args.score))


if __name__ == "__main__":
    main()
