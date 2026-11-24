# Big 5 AI Economics — Open Research

Independent, data-first research on what generative and agentic AI is doing to jobs, tasks, and wages in Canadian banking — built so **anyone can verify every number**.

Each LinkedIn post in the series has a folder under `posts/` containing the post text, the chart, the exact data file behind the chart, and the code that generated it. If a number is in a post, it is in this repo — or it doesn't go in the post.

## Series — daily run Nov 23–Dec 6, 2026, then Mon/Wed/Fri

| Post | Title | Headline result |
|---|---|---|
| 01 | Big 5 AI Scoreboard #1 | All Big 5 in the global top 30 for AI; only 12 of 50 banks report AI value |
| 02 | Junior Task Watch #1 — Analyst | ~65% of a junior analyst's task content is agent-executable by 2030 |
| 03 | What the Big Five Missed #1 | Deployment is not value: the five consultancies promise value, 24% report it, 5% of pilots prove P&L |
| 04 | Junior Task Watch #2 — Contact Centre | ~70% agent-executable by 2030 |
| 05 | Junior Task Watch #3 — Developer | ~72% agent-executable by 2030 |
| 06 | Scoreboard #2 US Edition | 8 of the top 10 are North American, up from 6 in 2023 |
| 09 | Scoreboard #3: The Returns Gap | 1,107 use cases; only 12 of 50 banks report value |
| 10 | Scoreboard #4: The Capex Tracker | Tech budgets vs AI spend — the value can't be tracked from capex alone |
| 14 | 2027 Conversations #1: The Junior Pipeline Problem | 65% / 70% / 72% — one pattern across three junior occupations |
| Synthesis | Three Occupations, One Pattern | The AEI public launch — not one of the fourteen; slot TBD after the run |

Scope: banking, starting with Canada's Big 5 and expanding to North America's top 10. Word rule: every post body is 99 words or fewer, or exactly 132 — never 100–131, never above 132.

## Method (public summary)

Task-level exposure is scored with an **Agentic Exposure Index**: for each task in an occupation's day, we combine (a) LLM capability, (b) observed copilot use in the economy, and (c) agent autonomy — the share of the task an AI agent can execute end-to-end without a human. Task taxonomies come from O*NET; observed-use data comes from the Anthropic Economic Index; bank figures come from public disclosures and the Evident AI Index. All sources, with access dates, are in `SOURCES.md`.

## Reproduce everything

```
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python code/make_chart.py        # Post 01 — and make_chart2.py … make_chart6.py, make_chart9.py, make_chart10.py, make_chart14.py, make_chart_synthesis.py for the rest
```

## License

Code: MIT. Data compiled from public sources — see `SOURCES.md` for provenance and original licenses (notably: Anthropic Economic Index datasets are published under MIT).

*Independent research. Not investment advice. Not affiliated with any bank, Anthropic, or Evident.*
