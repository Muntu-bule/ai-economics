import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Patch

df = pd.read_csv("data/contact_centre_tasks_aei.csv")
df = df.sort_values("agent_autonomy_2030", ascending=False)

def color(v):
    if v.startswith("Agent-led"):
        return "#b03a2e"
    if v == "Augmented":
        return "#d48806"
    return "#1a7a4a"

colors = [color(v) for v in df["verdict"]]
labels = [f"{t}  ({h}h)" for t, h in zip(df["task"], df["hours_per_day"])]
vals = (df["agent_autonomy_2030"] * 100).round(0).astype(int)

fig, ax = plt.subplots(figsize=(10.5, 5.6))
bars = ax.barh(range(len(df)), vals, color=colors, height=0.62)
ax.set_yticks(range(len(df)))
ax.set_yticklabels(labels, fontsize=9.5)
ax.invert_yaxis()
ax.set_xlim(0, 112)
ax.set_xlabel("Share of the task an AI agent can execute end-to-end by 2030 (%) — Agentic Exposure Index v0.2", fontsize=9.5)
ax.set_title("Junior Task Watch #2: A Contact-Centre Agent's 7.5-Hour Day\nAbout 70% is agent-executable by 2030. The human core here is empathy.",
             fontsize=13.5, fontweight="bold", loc="left", pad=12)
for bar, v in zip(bars, vals):
    ax.text(bar.get_width() + 1.5, bar.get_y() + bar.get_height() / 2, f"{v}%",
            va="center", fontsize=9.5, color="#333333")
ax.spines[["top", "right"]].set_visible(False)
ax.grid(axis="x", linestyle=":", alpha=0.5)
ax.legend(handles=[Patch(color="#b03a2e", label="Agent-led"),
                   Patch(color="#d48806", label="Augmented"),
                   Patch(color="#1a7a4a", label="Human-core")],
          loc="lower right", fontsize=9, frameon=False)
fig.text(0.01, -0.01, "Method: task taxonomy from O*NET (customer service representatives); scores = LLM capability x observed copilot use x agent autonomy. Sources: Anthropic Economic Index; bank disclosures (CIBC Voice Assistant, TD contact-centre genAI).",
         fontsize=7.5, color="#666666")
plt.tight_layout()
plt.savefig("linkedin-post-04-chart.png", dpi=200, bbox_inches="tight")
print("chart saved")
