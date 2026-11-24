"""Synthesis chart — AEI public launch, "Three Occupations, One Pattern".

Built 2026-11-20 after Mo chose "Synthesis today" (cascades decision).
Reads the same verified summary file as Post #14
(data/post14_pipeline_summary.csv) and asserts the three figures match
the published Task Watch CSVs before drawing anything. No new number,
no unscored occupation, no vault material. The framing differs from
Post #14's chart (the index launch, not the pipeline problem); the
figures are identical.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

summary = pd.read_csv("data/post14_pipeline_summary.csv")
assert len(summary) == 3, "expected exactly the three published occupations"
for _, row in summary.iterrows():
    df = pd.read_csv(row["source_csv"])
    hours = df["hours_per_day"].sum()
    pct = round(100 * (df["hours_per_day"] * df["agent_autonomy_2030"]).sum() / hours, 2)
    assert abs(pct - row["agent_executable_pct"]) < 0.01, row["occupation"]
print(summary.to_string(index=False))
print("verified: figures match the published Task Watch CSVs")

agent = summary["agent_executable_pct"]
human = summary["human_core_pct"]

fig, ax = plt.subplots(figsize=(10.5, 5.2))
y = range(len(summary))
ax.barh(y, agent, color="#1d428a", height=0.55,
        label="Agent-executable by 2030")
ax.barh(y, human, left=agent, color="#b03a2e", height=0.55,
        label="Human-core that remains")
ax.set_yticks(list(y))
ax.set_yticklabels(
    [f"{o} ({p}) — {h}" for o, p, h in
     zip(summary["occupation"], summary["post"], summary["human_core_label"])],
    fontsize=10)
ax.invert_yaxis()
ax.set_xlim(0, 112)
ax.set_xlabel("Share of the occupation's task hours (%) — Agentic Exposure Index v0.3",
              fontsize=9.5)
ax.set_title("The Agentic Exposure Index — the public launch\n"
             "Three junior occupations, one pattern — 65% → 70% → 72% agent-executable by 2030",
             fontsize=13, fontweight="bold", loc="left", pad=12)
for i, (a, h) in enumerate(zip(agent, human)):
    ax.text(a / 2, i, f"{a:.1f}%", ha="center", va="center",
            fontsize=10, color="white", fontweight="bold")
    ax.text(a + h / 2, i, f"{h:.1f}%", ha="center", va="center",
            fontsize=9.5, color="white")
ax.spines[["top", "right"]].set_visible(False)
ax.grid(axis="x", linestyle=":", alpha=0.5)
ax.legend(loc="lower right", fontsize=9, frameon=False)
fig.text(0.01, -0.01,
         "Method: hours-weighted agent-autonomy scores from the "
         "published Task Watch CSVs (Posts #2, #4, #5). No unscored occupation included.",
         fontsize=7.5, color="#666666")
plt.tight_layout()
plt.savefig("linkedin-synthesis-chart.png", dpi=200, bbox_inches="tight")
print("chart saved: linkedin-synthesis-chart.png")
