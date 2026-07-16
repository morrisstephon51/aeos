# LBOS Ops — How AXIS Coordinates This Daily

The system runs on one command: `/outreach`. Everything else is what that command does, in order.

---

## Daily Run (the `/outreach` loop)

1. **Read config** — `config.md` (quotas, niches, floors, thresholds)
2. **Triage the pipeline** — scan `leads/*.md`:
   - Overdue next-actions first (dates in the past)
   - Sequence touches due today (Day 3 / 7 / 14, post-proposal check-ins)
   - Stage moves earned but not recorded
3. **Draft due touches** — follow-ups and check-ins from `templates/`, saved into each lead file's Touch Log as `DRAFT`
4. **Prospect** — find up to 10 new leads per `playbook/prospecting.md`, score per `playbook/qualification.md`, create lead files for score ≥ 6
5. **Draft first-touches** — up to 5, HOT leads first, per `templates/cold_email.md`
6. **Rewrite the dashboard** — `leads/PIPELINE.md`
7. **Report** — outreach section in the daily brief (`ops/daily_brief_template.md`):
   - HOT leads flagged
   - Drafts awaiting Morris's approval (cold outreach never sends without sign-off)
   - Overdue items and what AXIS did about them
   - Pipeline totals + maintenance MRR

## Morris's Part (10 minutes/day)

- Approve or edit the drafted outreach — reply "send" per draft or "send all"
- Take the discovery calls AXIS books
- Decide on anything below pricing floor or outside the playbook

## Weekly Review (Mondays, with the AEOS task review)

- Funnel numbers vs. targets (`pipeline.md` → Metrics That Matter)
- Reply rate check: <10% two weeks running → rewrite templates, don't raise volume
- Zombie leads (>2 weeks stale) → force close/recycle decision
- Niche performance: double down on what's replying, drop what isn't
- Maintenance clients: any due for the 90-day referral ask?

## Escalation Triggers (AXIS → Morris immediately, not in the brief)

- A lead replies wanting to move fast (same-day response required)
- A maintenance client reports their site is down
- Any legal/complaint-flavored reply to outreach
- Proposal about to expire with no decision (48h warning)

## Boundaries

- All Plug AI. Any BigHeart overlap → flag and stop (`agent/identity.md`)
- No auto-sending cold outreach. Drafts only, until Morris approves
- Opt-outs honored instantly, logged, business marked Disqualified
