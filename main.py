#!/usr/bin/env python3
"""AI Judge Rich v4: write the 30-day plan to entry.txt.

Pure standard library, deterministic, no network.
The plan is the entry: escrow-first bounty claims plus a sellable
micro-tool, so every paid hour also yields an asset to sell.
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "\n".join(
    [
        "Judge: visible pay beats hoped-for pay. Rule zero: no code until escrow shows. Fiverr, Upwork, Stripe need a human ID; cold mail goes unread.",
        "Live board: make.fun 7 open, ~$3,800 pots, 130 paid places, 5 free; Bountycaster, Dework, Gitcoin, Algora: USDC on merged PRs, escrow first.",
        "Days 1-2: TypeScript kit (auth, webhook, CSV, tests), wallet. $10 credit, $10 gas, $80 reserve.",
        "Claims: max 2, each a tested PR in 24h; 6 drafts, duel pairs twice, send the winner, rework from the provisional rate.",
        "Leg 2: each kit module $19-29 on Gumroad; every paid hour yields a sellable asset.",
        "Math: 14 claims, half paid, 7 x $130 = $910, less 30% disputes ~$640; tools 15 x $19 = $285. Day 30: $100-$20+$925 = ~$1,005. Floor: 3 paid ~$270, tools $0: ~$350.",
        "Kill: below its paid line after 2 tries, drop it; no accepted claim in 5 days, bounties only; under $30/hour 3 days, test-suite fixes.",
        "Edge: a thousand agents pitch promises or chase unpaid work; mine ships finished code first, escrow-paid only.",
    ]
)

# The gate reads exactly these bytes: no trailing newline, pure ASCII.
# One plan, eight lines, 990 characters.
assert PLAN.isascii()
assert 1 <= len(PLAN) <= 1000

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
