# Local Business Outreach System (LBOS)

**Operator:** AXIS — Plug AI
**Objective:** Turn local businesses with no website (or a bad one) into paying clients for website **build**, **creation**, and **maintenance** — on a repeatable, daily-coordinated loop.

---

## What This Is

A pipeline system AXIS runs every day:

1. **Prospect** — find local businesses that need a website or have a broken/outdated one
2. **Qualify** — score them so only real opportunities get outreach effort
3. **Reach out** — first-touch email/call/walk-in using the templates
4. **Follow up** — timed sequence (Day 0 / 3 / 7 / 14), no lead goes cold silently
5. **Close** — call → proposal → signed build project
6. **Maintain** — convert every build into a recurring maintenance plan (the real revenue)

## Files

| File | Purpose |
|------|---------|
| `config.md` | Service area, target niches, daily quotas, pricing — edit this first |
| `pipeline.md` | Lead stages, lead record format, movement rules |
| `services.md` | Website build packages + maintenance plans (what we sell) |
| `playbook/prospecting.md` | How to find local businesses that need a website |
| `playbook/qualification.md` | Lead scoring — who gets outreach, who gets skipped |
| `playbook/sequences.md` | Outreach cadence: Day 0 / 3 / 7 / 14, per-channel |
| `templates/cold_email.md` | First-touch email (has website / no website variants) |
| `templates/follow_up.md` | Follow-up messages for each sequence step |
| `templates/call_script.md` | Discovery call script |
| `templates/proposal.md` | Build + maintenance proposal skeleton |
| `leads/_TEMPLATE.md` | Lead record template — copy per lead |
| `leads/PIPELINE.md` | Live pipeline dashboard — updated every run |
| `ops.md` | Daily/weekly coordination cadence — how AXIS runs this |

## Quick Start

1. `config.md` is set: Chicago, IL — 20 leads/10 first-touches per weekday, launch-offer pricing active
2. The loop runs automatically Mon–Fri mornings (or manually via `/outreach`) — AXIS prospects, scores, sends approved-template outreach via Gmail, and updates the pipeline
3. Read the run report — every sent message appears inline; replies and HOT leads escalate to you
4. Templates are pre-approved once by Morris; any new or edited template requires re-approval before AXIS may send it (see `agent/email_rules.md`)

## Rules of the System

- **No lead sits untouched >3 days.** Every lead has a next action and a date.
- **Maintenance is the goal.** A build without a maintenance plan attached is a half-closed deal.
- **Quality over volume.** Daily quota is small on purpose — personalized beats blasted.
- **Everything is logged.** If it's not in the lead file, it didn't happen.
