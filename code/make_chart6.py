"""Post #6 chart — Scoreboard #2, The US Edition (Sat 2026-11-28, daily run day 6).
Angle (approved by Mo 2026-11-21, North America angle): eight of the top ten are
North American, up from six in 2023 — and the race is now about who can show the
value, not who adopted first.
Regenerates byte-identically from data/scoreboard02_top10_draft.csv.
Chart: top-10 ranking bars (length = 11 - rank), coloured by headquarters —
US dark blue, Canada gold, other grey-blue — with 2025 ranks and the TD 13->10
and Morgan Stanley 5->9 moves annotated. No dollar figure is charted (TD C$195M
is TD's own disclosure; Evident's $137M restatement stays unprinted).
Run from ~/workspace/rbc-ai-wages: python3 make_chart6.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/scoreboard02_top10_draft.csv", comment="#")
print(df[["rank_2026", "bank", "rank_2025", "change"]].to_string(index=False))

display = {"JPMorganChase": "JPMorgan Chase", "Capital One": "Capital One",
           "RBC": "RBC", "CommBank": "CommBank", "Wells Fargo": "Wells Fargo",
           "UBS": "UBS", "Bank of America": "Bank of America",
           "Citigroup": "Citigroup", "Morgan Stanley": "Morgan Stanley", "TD": "TD"}
country = {"JPMorganChase": "US", "Capital One": "US", "RBC": "CA",
           "CommBank": "AU", "Wells Fargo": "US", "UBS": "CH",
           "Bank of America": "US", "Citigroup": "US", "Morgan Stanley": "US",
           "TD": "CA"}
colours = {"US": "#0b3d91", "CA": "#d48806", "AU": "#7ba0c4", "CH": "#7ba0c4"}

df = df.sort_values("rank_2026")
banks = [display[b] for b in df["bank"]]
values = [11 - r for r in df["rank_2026"]]
cols = [colours[country[b]] for b in df["bank"]]
labels = [f"#{int(r26)}  (2025: #{int(r25)})" for r26, r25 in
          zip(df["rank_2026"], df["rank_2025"])]

fig, ax = plt.subplots(figsize=(10, 5.6))
bars = ax.barh(banks, values, color=cols, height=0.55)
for bar, lab in zip(bars, labels):
    ax.text(bar.get_width() + 0.25, bar.get_y() + bar.get_height() / 2,
            lab, va="center", fontsize=11, fontweight="bold", color="#0b3d91")
ax.set_xlim(0, 12.5)
ax.set_xlabel("Evident AI Index 2026 rank (bar length = 11 - rank)", fontsize=10)
ax.set_title("Eight of the top ten are North American:\n"
             "six US banks, two Canadians — up from six in 2023",
             fontsize=13.5, fontweight="bold", loc="left", pad=12)
ax.spines[["top", "right"]].set_visible(False)
ax.grid(axis="x", linestyle=":", alpha=0.5)
ax.invert_yaxis()
fig.text(0.01, -0.01,
         "Sources: Evident AI Index: Key Findings Report, October 2026, p.4 rankings table + "
         "2023-2026 change table (direct check 2026-11-20). Colours by headquarters: dark blue US, "
         "gold Canada, grey-blue other. TD climbed 13 -> 10; Morgan Stanley fell 5 -> 9. "
         "Average bank score +26% year over year; top-10 spread narrowed 25%. "
         "Only 12 of 50 banks report any realised or projected AI value. Chart: Scoreboard #2.",
         fontsize=7.5, color="#666666")
plt.tight_layout()
plt.savefig("linkedin-post-06-chart.png", dpi=200, bbox_inches="tight")
print("chart saved: linkedin-post-06-chart.png")
print("North American banks in top 10:",
      sum(1 for b in df["bank"] if country[b] in ("US", "CA")),
      "(US:", str(sum(1 for b in df["bank"] if country[b] == "US")),
      "CA:", str(sum(1 for b in df["bank"] if country[b] == "CA")) + ")")
