# LBOS Pipeline

## Stages

```
Prospect → Qualified → Contacted → Engaged → Call Booked → Proposal Sent → Won (Build) → Maintenance → [Lost / Disqualified]
```

| Stage | Definition | Exit Criteria |
|-------|-----------|---------------|
| **Prospect** | Found, not yet scored | Scored per `playbook/qualification.md` |
| **Qualified** | Score ≥ 6, contact info found | First-touch sent |
| **Contacted** | First-touch sent, no reply yet | Reply received, or sequence exhausted |
| **Engaged** | Replied — any response counts | Call booked or hard no |
| **Call Booked** | Discovery call on calendar | Call completed |
| **Proposal Sent** | Proposal delivered after call | Signed, or 14 days of silence |
| **Won (Build)** | Deposit paid, build started | Site launched |
| **Maintenance** | On a recurring plan | Churn (goes to Lost with reason) |
| **Lost** | Hard no, or sequence exhausted | Logged with reason; recycle eligible after 90 days |
| **Disqualified** | Hit a disqualifier in `config.md` | Never re-enter |

## Movement Rules

- Every lead in Qualified → Proposal Sent **must** have a `Next Action` and `Next Action Date`. No exceptions.
- A lead with a `Next Action Date` in the past is **overdue** — surfaces at the top of every `/outreach` run and in the daily brief.
- Sequence exhausted (Day 14 touch, no reply) → move to Lost, reason `no-response`. Recycle in 90 days with a fresh angle.
- Won leads are not done: launching the site triggers the maintenance pitch if not already sold (see `templates/proposal.md`).

## Lead Record

One file per lead in `leads/`, named `business-name-slug.md`, using `leads/_TEMPLATE.md`.

Required fields: Business, Niche, Location, Website status, Score, Stage, Contact, Next Action, Next Action Date, Touch Log.

## Dashboard

`leads/PIPELINE.md` is the single-glance view — a table of every active lead sorted by stage then next-action date. AXIS rewrites it at the end of every `/outreach` run. If the dashboard and a lead file disagree, the lead file wins; fix the dashboard.

## Metrics That Matter (weekly, in Monday review)

1. New qualified leads this week
2. First-touches sent
3. Reply rate (target: >10%)
4. Calls booked
5. Proposals → closes (target: >30%)
6. **MRR from maintenance plans** — the north star
