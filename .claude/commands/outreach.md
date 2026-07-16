# /outreach — Run the Local Business Outreach Coordination Loop

You are AXIS (see `agent/identity.md`). Execute the daily LBOS run exactly as defined in `outreach/ops.md`.

## Steps

1. Read `outreach/config.md` — quotas, niches, service area, pricing floors, alert threshold.
2. Triage `outreach/leads/*.md` (skip `_TEMPLATE.md`):
   - List every lead whose **Next action date** is today or past — these come first.
   - Identify sequence touches due today per `outreach/playbook/sequences.md`.
3. For each due touch, draft the message using the matching file in `outreach/templates/`, personalized with the lead's Hook and notes. Append it to that lead's Touch Log with status `DRAFT`, and update Next action / Next action date.
4. Prospect new leads per `outreach/playbook/prospecting.md` (use web search if available; otherwise output a prospecting worklist for Morris) up to the daily quota. Score each per `outreach/playbook/qualification.md`. Create a lead file from `outreach/leads/_TEMPLATE.md` for every score ≥ 6.
5. Draft first-touch emails (max = daily quota) — HOT leads (score ≥ 8) first.
6. Rewrite `outreach/leads/PIPELINE.md` from the lead files: Overdue, HOT, Active, Won/Maintenance, Totals (including maintenance MRR). Stamp the date.
7. Output the run report in this format:

```
## LBOS Daily Run — YYYY-MM-DD

🔥 HOT: [n leads — names + scores]
✉️  Drafts awaiting approval: [n — lead: touch type]
⚠️  Overdue handled: [n — what was done]
📈 Pipeline: [active] active / [won] won / $[MRR] maintenance MRR
Next: [the single most important action for Morris today]
```

## Hard Rules

- Never send anything. Drafts only — Morris approves.
- Never quote below the pricing floors in `outreach/config.md`.
- Never create a lead without a verified specific Hook.
- Any BigHeart overlap → flag and stop.
