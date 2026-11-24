"""Post #14 chart — the junior pipeline problem.

Recomputes the three headline figures directly from the published task
CSVs and asserts they match data/post14_pipeline_summary.csv before
drawing anything. No new number, no unscored occupation, no vault material.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

SOURCES = [
    ("Junior Analyst", "Post #2", "data/junior_tasks_aei.csv",
     "Judgment and relationships"),
    ("Contact Centre", "Post #4", "data/contact_centre_tasks_aei.csv",
     "Empathy under pressure"),
    ("Junior Developer", "Post #5", "data/junior_dev_tasks_aei.csv",
     "Design and translation"),
]

rows = []
for occ, post, path, human_label in SOURCES:
    df = pd.read_csv(path)
    hours = df["hours_per_day"].sum()
    pct = 100 * (df["hours_per_day"] * df["agent_autonomy_2030"]).sum() / hours
    rows.append({"occupation": occ, "post": post, "tasks": len(df),
                 "hours_per_day": hours, "agent_executable_pct": round(pct, 2),
                 "human_core_pct": round(100 - pct, 2),
                 "human_core_label": human_label, "source_csv": path})

summary = pd.DataFrame(rows)
expected = pd.read_csv("data/post14_pipeline_summary.csv")
pd.testing.assert_frame_equal(
    summary, expected, check_dtype=False, atol=0.01)
print(summary.to_string(index=False))
print("verified: recomputed figures match post14_pipeline_summary.csv")

agent = summary["agent_executable_pct"]
human = summary["human_core_pct"]

fig, ax = plt.subplots(figsize=(10.5, 5.2))
y = range(len(summary))
ax.barh(y, agent, color="#b03a2e", height=0.55,
        label="Agent-executable by 2030")
ax.barh(y, human, left=agent, color="#1a7a4a", height=0.55,
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
ax.set_title("2027 Conversations #1: The Junior Pipeline Problem\n"
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
plt.savefig("linkedin-post-14-chart.png", dpi=200, bbox_inches="tight")
print("chart saved: linkedin-post-14-chart.png")
