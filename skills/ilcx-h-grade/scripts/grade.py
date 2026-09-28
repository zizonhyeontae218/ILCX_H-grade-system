#!/usr/bin/env python3
import argparse

def label(score: int) -> str:
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")
    if score == 100:
        return "ILCX 10H grade"
    base = score // 10
    plus = "+" if score % 10 >= 5 else ""
    return f"ILCX {base}H{plus} grade"

def main():
    p = argparse.ArgumentParser(description="Convert an ILCX human-contribution score into an H-grade.")
    p.add_argument("score", type=int, help="integer score from 0 to 100")
    args = p.parse_args()
    print(label(args.score))

if __name__ == "__main__":
    main()
