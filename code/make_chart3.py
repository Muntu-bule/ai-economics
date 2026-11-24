import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

labels = [
    "Big 5 banks with firm-wide AI copilots",
    "Global top-50 banks reporting realised\nor projected AI value (Evident)",
    "Enterprise genAI pilots with measurable\nP&L impact (MIT NANDA)",
]
vals = [100, 24, 5]
colors = ["#0b3d91", "#d48806", "#b03a2e"]

fig, ax = plt.subplots(figsize=(10, 4.6))
bars = ax.barh(range(len(labels)), vals, color=colors, height=0.58)
ax.set_yticks(range(len(labels)))
ax.set_yticklabels(labels, fontsize=10.5)
ax.invert_yaxis()
ax.set_xlim(0, 118)
ax.set_xlabel("Share (%)", fontsize=10)
ax.set_title("What McKinsey Missed: Deployment Is Not Value\nMcKinsey estimates 200-340B USD of annual AI value potential in banking. The proof so far:",
             fontsize=13.5, fontweight="bold", loc="left", pad=12)
for bar, v in zip(bars, vals):
    ax.text(bar.get_width() + 2, bar.get_y() + bar.get_height() / 2, f"{v}%",
            va="center", fontsize=12, fontweight="bold", color="#333333")
ax.spines[["top", "right"]].set_visible(False)
ax.grid(axis="x", linestyle=":", alpha=0.5)
fig.text(0.01, -0.01, "Sources: McKinsey Global Institute (2023); Evident AI Index 2025-26; MIT Project NANDA (2025); bank disclosures. Chart: What McKinsey Missed #1",
         fontsize=8, color="#666666")
plt.tight_layout()
plt.savefig("linkedin-post-03-chart.png", dpi=200, bbox_inches="tight")
print("chart saved")
