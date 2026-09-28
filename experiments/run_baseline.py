"""Reproducible Prototype 0.2 experiment runner."""

from arfa.simulation import run_episode


def main():
    rows = run_episode()
    print("step,shock,drift,autonomy,safe")
    for r in rows:
        print(f"{r.step},{r.shock:.4f},{r.drift:.4f},{r.autonomy:.4f},{int(r.safe)}")


if __name__ == "__main__":
    main()
