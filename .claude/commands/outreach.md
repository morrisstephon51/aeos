# /outreach — Run the Local Business Outreach Coordination Loop

You are AXIS (see `agent/identity.md`). Execute the daily LBOS run exactly as defined in `outreach/ops.md`. Autonomy mode is **template-approved**: send from approved templates without per-message sign-off; escalate everything else.

## Steps

1. Read `outreach/config.md` — quotas, niches, service area, launch-offer status, pricing floors, alert threshold.
2. Triage `outreach/leads/*.md` (skip `_TEMPLATE.md`):
   - Every lead whose **Next action date** is today or past comes first.
   - Identify sequence touches due today per `outreach/playbook/sequences.md`.
3. For each due touch: personalize the matching approved template from `outreach/templates/` with the lead's Hook and notes, **send it via Gmail**, append it to the lead's Touch Log as `SENT` with timestamp, and update Next action / Next action date.
   - Gmail unavailable → log as `QUEUED`, include the full message in the send queue section of the report, and flag the connection loss.
   - Message needs to deviate from an approved template → do NOT send; escalate as `DRAFT`.
4. Prospect new leads per `outreach/playbook/prospecting.md` (use web search if available; otherwise output a prospecting worklist) up to the daily quota (20). Score each per `outreach/playbook/qualification.md`. Create a lead file from `outreach/leads/_TEMPLATE.md` for every score ≥ 6.
5. Send first-touch emails (max 10/day) — HOT leads (score ≥ 8) first. Same send/queue/escalate rules as step 3.
6. Rewrite `outreach/leads/PIPELINE.md` from the lead files: Overdue, HOT, Active, Won/Maintenance, Totals (including launch-offer slots remaining and maintenance MRR). Stamp the date.
7. Output the run report. **Include every message sent, queued, or escalated — inline and in full** (recipient, subject, body). Then the summary block:

```
## LBOS Daily Run — YYYY-MM-DD

📬 Replies needing Morris: [n — lead + recommended response]
🔥 HOT: [n leads — names + scores]
✅ Sent: [n first-touches, n follow-ups]
📋 Queued/escalated: [n — why]
📈 Pipeline: [active] active / [won] won / [launch slots left] launch slots / $[MRR] MRR
Next: [the single most important action for Morris today]
```

## Hard Rules

- Send ONLY messages generated from approved templates. Anything off-template escalates as a draft.
- Never quote below launch-offer terms or pricing floors in `outreach/config.md`.
- Never create a lead without a verified specific Hook.
- Honor opt-outs instantly; log and disqualify.
- Any BigHeart overlap → flag and stop.
