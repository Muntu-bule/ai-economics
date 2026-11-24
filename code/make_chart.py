import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

banks = ["RBC", "TD", "BMO", "CIBC", "Scotiabank"]
ranks = [3, 10, 20, 21, 30]
signals = [
    "72,000+ staff on AI tools · C\\$700M–1B target by 2027",
    "C\\$195M reported toward C\\$500M combined revenue-and-savings target",
    "90%+ of 53,000 staff on Microsoft Copilot",
    "50,000+ staff on CAI · agentic CAI 2.0 in pilot",
    "Google Cloud / Vertex AI enterprise platform",
]
colors = ["#0b3d91", "#1a7a4a", "#2e6f8e", "#7d3c98", "#b03a2e"]

fig, ax = plt.subplots(figsize=(10, 5.2))
y = range(len(banks))
bars = ax.barh(list(y), ranks, color=colors, height=0.62)
ax.set_yticks(list(y))
ax.set_yticklabels([f"{b}  —  #{r} globally" for b, r in zip(banks, ranks)], fontsize=11)
ax.invert_yaxis()
ax.set_xlim(0, 48)
ax.set_xlabel("Evident AI Index — global rank (lower = more AI-mature)", fontsize=10)
ax.set_title("Canada's Big 5: All Top 30 in the World for AI.\nAlmost None Can Prove the Value Yet.",
             fontsize=14, fontweight="bold", loc="left", pad=14)
for i, (bar, sig) in enumerate(zip(bars, signals)):
    ax.text(bar.get_width() + 0.6, bar.get_y() + bar.get_height() / 2,
            sig, va="center", fontsize=9, color="#333333")
ax.spines[["top", "right"]].set_visible(False)
ax.grid(axis="x", linestyle=":", alpha=0.5)
fig.text(0.01, -0.01, "Sources: Evident AI Index 2026 (Oct 2026 edition); bank disclosures 2025–26. Chart: Big 5 AI Scoreboard #1",
         fontsize=8, color="#666666")
plt.tight_layout()
plt.savefig("linkedin-post-01-chart.png", dpi=200, bbox_inches="tight")
print("chart saved")
