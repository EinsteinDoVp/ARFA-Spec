"""Minimal deterministic ablation for ARFA Prototype 0.2.

Compares the prototype controller with a fixed-autonomy baseline in the same
synthetic episode. This is a toy experiment, not evidence of real-world safety.
"""

from arfa.simulation import run_episode


def summarize(rows):
    safe = sum(r.safe for r in rows)
    return {"safe_steps": safe, "total_steps": len(rows), "mean_autonomy": sum(r.autonomy for r in rows) / len(rows)}


def fixed_autonomy_baseline(rows, autonomy=0.9, theta=0.25):
    safe = 0
    for r in rows:
        high_drift = r.drift >= theta
        if (not high_drift) or autonomy <= 0.5:
            safe += 1
    return {"safe_steps": safe, "total_steps": len(rows), "mean_autonomy": autonomy}


def main():
    rows = run_episode()
    arfa = summarize(rows)
    fixed = fixed_autonomy_baseline(rows)
    print("controller,safe_steps,total_steps,mean_autonomy")
    print(f"arfa,{arfa['safe_steps']},{arfa['total_steps']},{arfa['mean_autonomy']:.4f}")
    print(f"fixed_0.9,{fixed['safe_steps']},{fixed['total_steps']},{fixed['mean_autonomy']:.4f}")


if __name__ == "__main__":
    main()
