import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/junior_tasks_aei.csv")
df = df.sort_values("agent_autonomy_2030", ascending=False)  # largest first -> top after invert

def color(v):
    if v.startswith("Agent-led"):
        return "#b03a2e"
    if v == "Augmented":
        return "#d48806"
    return "#1a7a4a"

colors = [color(v) for v in df["verdict"]]
labels = [f"{t}  ({h}h)" for t, h in zip(df["task"], df["hours_per_day"])]
vals = (df["agent_autonomy_2030"] * 100).round(0).astype(int)

fig, ax = plt.subplots(figsize=(10.5, 6.0))
bars = ax.barh(range(len(df)), vals, color=colors, height=0.62)
ax.set_yticks(range(len(df)))
ax.set_yticklabels(labels, fontsize=9.5)
ax.invert_yaxis()
ax.set_xlim(0, 112)
ax.set_xlabel("Share of the task an AI agent can execute end-to-end by 2030 (%) — Agentic Exposure Index v0.1", fontsize=9.5)
ax.set_title("Junior Task Watch #1: A First-Year Analyst's 10-Hour Day\nAbout 65% is agent-executable by 2030. The human 35% is judgment + relationships.",
             fontsize=13.5, fontweight="bold", loc="left", pad=12)
for bar, v in zip(bars, vals):
    ax.text(bar.get_width() + 1.5, bar.get_y() + bar.get_height() / 2, f"{v}%",
            va="center", fontsize=9.5, color="#333333")
ax.spines[["top", "right"]].set_visible(False)
ax.grid(axis="x", linestyle=":", alpha=0.5)
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color="#b03a2e", label="Agent-led"),
                   Patch(color="#d48806", label="Augmented"),
                   Patch(color="#1a7a4a", label="Human-core")],
          loc="lower right", fontsize=9, frameon=False)
fig.text(0.01, -0.01, "Method: task taxonomy from O*NET (financial analysts); scores = LLM capability x observed copilot use x agent autonomy. Sources: Anthropic Economic Index; bank disclosures (RBC QuickTakes, CIBC CAI 2.0).",
         fontsize=7.5, color="#666666")
plt.tight_layout()
plt.savefig("linkedin-post-02-chart.png", dpi=200, bbox_inches="tight")

w_agent = (df["hours_per_day"] * df["agent_autonomy_2030"]).sum() / df["hours_per_day"].sum()
w_copilot = (df["hours_per_day"] * df["observed_copilot_use"]).sum() / df["hours_per_day"].sum()
print(f"chart saved | agent-executable share 2030: {w_agent:.1%} | copilot-touched today: {w_copilot:.1%}")
