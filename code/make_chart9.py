"""Post #9 chart — Scoreboard #3, The Returns Gap (Tue 2026-12-01).
Regenerates byte-identically from data/scoreboard03_returns_gap.csv.
Chart: the disclosure funnel as three shares — use cases disclosing a KPI effect (12%),
use cases disclosing a financial return (~1%), top-50 banks reporting any AI value (12 of 50 = 24%).
Run from repo root: python3 code/make_chart9.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/scoreboard03_returns_gap.csv", comment="#")
vals = {
    "Use cases disclosing\nan operational-KPI effect": 12,
    "Use cases disclosing\na concrete financial return": 1,
    "Top-50 banks reporting\nany AI value (12 of 50)": 24,
}
labels = list(vals.keys())
values = list(vals.values())
print(df[df["metric"].isin(["use_cases_disclosed", "pct_disclosing_kpi_effect",
                            "pct_disclosing_financial_return", "banks_reporting_value"])]
      .to_string(index=False))

fig, ax = plt.subplots(figsize=(10, 5.2))
bars = ax.barh(labels, values, color=["#0b3d91", "#d48806", "#0b3d91"], height=0.55)
for bar, v, raw in zip(bars, values, ["of 1,107 use cases", "of 1,107 use cases", "12 of 50 banks"]):
    ax.text(bar.get_width() + 0.6, bar.get_y() + bar.get_height() / 2,
            f"{v}%  ({raw})", va="center", fontsize=11, fontweight="bold", color="#0b3d91")
ax.set_xlim(0, 32)
ax.set_xlabel("Share (%)", fontsize=10)
ax.set_title("The Returns Gap: 1,107 AI use cases disclosed since 2021 —\n"
             "and almost nobody will put a number on the return",
             fontsize=13.5, fontweight="bold", loc="left", pad=12)
ax.spines[["top", "right"]].set_visible(False)
ax.grid(axis="x", linestyle=":", alpha=0.5)
ax.invert_yaxis()
fig.text(0.01, -0.01,
         "Sources: Evident AI Index 2026 (briefing text + reproduced table); MIT Project NANDA (2025). "
         "TD C\\$195M is AI VALUE in 9 months of FY2026 vs a C\\$200M target — not a return (no spend denominator disclosed). "
         "No CA-vs-US split of the 12 reporting banks is published here: it is not verified. Chart: Scoreboard #3.",
         fontsize=7.5, color="#666666")
plt.tight_layout()
plt.savefig("linkedin-post-09-chart.png", dpi=200, bbox_inches="tight")
print("chart saved: linkedin-post-09-chart.png")
