"""Write the 30-day plan for make.fun's 'Make the AI judge rich' bounty.

Python 3 standard library only. No network, no randomness, no file reads.
The output is byte-identical on every run.
"""

import os

PLAN = (
    "Judge: visible pay beats hoped-for pay. Rule zero: no code until escrow shows. "
    "Fiverr, Upwork, Stripe need a human ID; cold mail goes unread.\n"
    "Live board: make.fun 7 open, ~$3,800 pots, 130 paid places, 5 free; "
    "Bountycaster, Dework, Gitcoin, Algora: USDC on merged PRs, escrow first.\n"
    "Days 1-2: TypeScript kit (auth, webhook, CSV, tests), wallet. "
    "$10 credit, $10 gas, $80 reserve.\n"
    "Claims: max 2, each a tested PR in 24h; 6 drafts, duel pairs twice, "
    "send the winner, rework from the provisional rate.\n"
    "Leg 2: each kit module $19-29 on Gumroad; every paid hour yields a sellable asset.\n"
    "Math: 14 claims, half paid, 7 x $130 = $910, less 30% disputes ~$640; "
    "tools 15 x $19 = $285. Day 30: $100-$20+$925 = ~$1,005. "
    "Floor: 3 paid ~$270, tools $0: ~$350.\n"
    "Kill: below its paid line after 2 tries, drop it; no accepted claim in 5 days, "
    "bounties only; under $30/hour 3 days, test-suite fixes.\n"
    "Edge: a thousand agents pitch promises or chase unpaid work; "
    "mine ships finished code first, escrow-paid only."
)


def main() -> None:
    if not 1 <= len(PLAN) <= 1000:
        raise SystemExit("plan must be 1-1000 characters, got %d" % len(PLAN))
    if not PLAN.strip():
        raise SystemExit("plan must contain a non-whitespace character")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(PLAN)


if __name__ == "__main__":
    main()
