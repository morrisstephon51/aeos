# LBOS Ops — How AXIS Coordinates This Daily

Runs automatically every weekday morning (Chicago time) via scheduled Routine; `/outreach` can also be run manually anytime. **Autonomy mode: template-approved** — Morris approved the templates once, AXIS sends. See `playbook/sequences.md`.

---

## Daily Run (the `/outreach` loop, Mon–Fri)

1. **Read config** — `config.md` (quotas, niches, floors, launch offer status, thresholds)
2. **Triage the pipeline** — scan `leads/*.md`:
   - Overdue next-actions first (dates in the past)
   - Sequence touches due today (Day 3 / 7 / 14, post-proposal check-ins)
   - Stage moves earned but not recorded
3. **Send due touches** — personalize from approved templates, send via Gmail, log each in the lead file's Touch Log as `SENT`. No Gmail connection → log as `QUEUED` and put the full message in the send queue.
4. **Prospect** — up to 20 new leads per `playbook/prospecting.md`, scored per `playbook/qualification.md`, lead files created for score ≥ 6
5. **Send first-touches** — up to 10, HOT leads first. Off-template personalization → escalate as `DRAFT` instead of sending.
6. **Rewrite the dashboard** — `leads/PIPELINE.md`
7. **Report** — the run report includes **every message sent or queued, inline and in full**, plus:
   - Replies received → escalated with recommended response
   - HOT leads flagged
   - Pipeline totals + launch-offer slots remaining + maintenance MRR
   - The single most important action for Morris today

## Morris's Part (minutes/day)

- Read the run report; answer escalations (replies, HOT leads, off-template drafts)
- Take the discovery calls AXIS books
- Approve any template changes (a changed template is unapproved until Morris signs off)

## Weekly Review (Mondays, with the AEOS task review)

- Funnel numbers vs. targets (`pipeline.md` → Metrics That Matter)
- Reply rate check: <10% two weeks running → rewrite templates (re-approval required), don't raise volume
- Zombie leads (>2 weeks stale) → force close/recycle decision
- Niche performance: double down on what's replying, drop what isn't
- Launch offer status: slots filled? 60-day referral asks due?

## Escalation Triggers (AXIS → Morris immediately, not in the brief)

- Any reply from a lead (same-day response required — this is where clients come from)
- A maintenance client reports their site is down
- Any legal/complaint-flavored reply to outreach
- Proposal about to expire with no decision (48h warning)
- Gmail send failures or connection loss (system silently stalling = pipeline dying)

## Boundaries

- All Plug AI. Any BigHeart overlap → flag and stop (`agent/identity.md`)
- Sending authority covers **approved templates only** — new or edited templates, and any message that deviates from one, require Morris's sign-off (`agent/email_rules.md`)
- Opt-outs honored instantly, logged, business marked Disqualified
- Volume caps in `config.md` are hard ceilings, never exceeded to "catch up"
