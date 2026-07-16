# Qualification — Lead Scoring

Score every prospect 0–10 before any outreach. **Score ≥ 6 → Qualified. Score ≥ 8 → HOT** (flag in daily brief, outreach same day, phone-eligible).

---

## Scoring Weights

| Factor | Weight | How to Score |
|--------|--------|--------------|
| **Website need** | 40% | No website: 10 · Social-only: 9 · Broken/dead link: 8 · Outdated (>3 yrs old look, not mobile): 6 · Mediocre but functional: 3 · Recent professional site: 0 |
| **Business vitality** | 30% | Reviews in last 30 days + rating ≥ 4.0: 10 · Active but mixed reviews: 6 · Little recent activity: 3 · Looks dormant: 0 |
| **Reachability** | 20% | Owner name + direct email/phone found: 10 · Business email/phone only: 6 · Contact form or DM only: 3 |
| **Fit & proximity** | 10% | Priority niche + inside radius: 10 · Priority niche, edge of radius: 7 · Secondary niche: 5 |

**Score = (need × .4) + (vitality × .3) + (reachability × .2) + (fit × .1)**, rounded to one decimal.

## Hard Disqualifiers (score 0, stage → Disqualified)

- Any disqualifier in `config.md` (franchise sites, agency-served, BigHeart overlap, <6 mo history)
- No way to contact at all
- Business appears closed

## Priority Order Within a Run

1. HOT leads (≥ 8) — same-day first-touch
2. Overdue follow-ups (next-action date in the past)
3. Qualified leads (6–7.9) — first-touch within quota
4. Everything else waits; the quota exists to keep quality up

## Sanity Checks Before Sending

- Is the "one specific observation" in the lead file actually true? Verify before it goes in an email.
- Did we already contact this business under a different name/location? Check `leads/`.
- Would a reasonable owner find this outreach useful rather than spammy? If not, rewrite or skip.
