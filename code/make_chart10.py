"""Post #10 chart — Scoreboard #4, AI Capex Tracker (Mon 2026-11-16, ~4pm ET).
Act 2 of the Nov 16 double scoreboard; Act 1 is Scoreboard #3 (The Returns Gap) at 8am.
Regenerates byte-identically from data/scoreboard04_capex_tracker.csv.
Chart: the four comparable disclosed tech budgets, native currencies labelled on each bar.
Banks with no comparable total (TD, BMO, Scotiabank, CIBC, Citi, Capital One) are NOT charted —
they are listed as gaps in the post copy and the data-file comments.
Run from ~/workspace/rbc-ai-wages: python3 make_chart10.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/scoreboard04_capex_tracker.csv", comment="#")
print(df[["bank", "currency", "tech_spend_native", "tech_spend_label"]]
      .to_string(index=False))
print("RBC in USD at ~1.40 CAD/USD (approx, scale only):",
      round(6 / 1.40, 2), "-> JPM/RBC ratio ~", round(18 / (6 / 1.40), 1), "x")

banks = ["JPMorgan Chase", "Bank of America", "Wells Fargo", "Royal Bank of Canada"]
values = [18, 12.7, 10, 6]
labels = ["US$18B", "US$~13B", "US$10B+", "C$~6B"]
years = ["2025", "2025", "2026 (floor)", "FY2025"]

fig, ax = plt.subplots(figsize=(10, 5.2))
bars = ax.barh(banks, values, color=["#0b3d91", "#0b3d91", "#7ba0c4", "#d48806"], height=0.55)
for bar, lab, yr in zip(bars, labels, years):
    ax.text(bar.get_width() + 0.4, bar.get_y() + bar.get_height() / 2,
            f"{lab}  ({yr})", va="center", fontsize=11, fontweight="bold", color="#0b3d91")
ax.set_xlim(0, 23)
ax.set_xlabel("Disclosed technology budget, native currency (billion)", fontsize=10)
ax.set_title("Where the money is actually going:\n"
             "the tech budgets behind the AI story",
             fontsize=13.5, fontweight="bold", loc="left", pad=12)
ax.spines[["top", "right"]].set_visible(False)
ax.grid(axis="x", linestyle=":", alpha=0.5)
ax.invert_yaxis()
fig.text(0.01, -0.01,
         "Sources: JPMorgan Investor Day May 2025; BofA Investor Day Nov 5 2025; Wells Fargo disclosure Oct 2026; "
         "RBC investor deck Q3 2026. Currencies as disclosed — no silent conversion (RBC C\\$6B is ~US\\$4.3B at ~1.40). "
         "TD, BMO, Scotiabank, CIBC, Citi and Capital One publish no comparable total — that is the gap, not a zero. "
         "Tech spend is not AI spend: no bank breaks AI out cleanly. Chart: Scoreboard #4.",
         fontsize=7.5, color="#666666")
plt.tight_layout()
plt.savefig("linkedin-post-10-chart.png", dpi=200, bbox_inches="tight")
print("chart saved: linkedin-post-10-chart.png")
