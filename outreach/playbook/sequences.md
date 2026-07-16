# Outreach Sequences — Cadence & Rules

Every qualified lead enters a timed sequence. **Autonomy mode: template-approved** (per `agent/email_rules.md` category pre-authorization) — Morris has approved the templates once; AXIS sends each touch on its due date via Gmail without per-message sign-off. What still escalates to Morris: every reply, HOT leads, anything that requires deviating from an approved template, and all template changes. If Gmail is not connected, AXIS falls back to a ready-to-paste send queue in the run report.

---

## Standard Email Sequence

| Day | Touch | Template | Rule |
|-----|-------|----------|------|
| 0 | First-touch email | `templates/cold_email.md` | Must open with the lead's specific observation |
| 3 | Follow-up #1 | `templates/follow_up.md` §1 | Add one new piece of value (a fix, a stat, a mockup offer) |
| 7 | Follow-up #2 | `templates/follow_up.md` §2 | Shorter. One question. |
| 14 | Breakup note | `templates/follow_up.md` §3 | Graceful exit, leaves door open → Lost (`no-response`) |

## HOT Lead Overlay (score ≥ 8)

- Day 0: email **and** phone call attempt (`templates/call_script.md` opener)
- Day 1: if no answer, voicemail + text if number is mobile
- Then rejoin standard sequence at Day 3
- Within 15 min of home base and score ≥ 9: propose a walk-in to Morris in the daily brief

## Reply Handling

- **Any reply → stage Engaged.** Sequence stops immediately; from here it's conversation, not cadence.
- Positive/curious → objective is one thing only: **book the discovery call**. Offer two specific time slots.
- Objection → handle per `templates/call_script.md` objection table, once. Push twice, never three times.
- Hard no → Lost (`hard-no`), thank them, stop. Log the reason verbatim.

## Post-Call Sequence

| Day | Action |
|-----|--------|
| 0 | Discovery call → proposal drafted same day (`templates/proposal.md`) |
| 1 | Proposal sent with a specific expiry (14 days) |
| 4 | Check-in: "any questions on the proposal?" |
| 10 | Final nudge with expiry reminder |
| 14 | Silence → Lost (`proposal-no-response`), recycle eligible in 90 days |

## Anti-Spam / Reputation Rules

- Max first-touch emails per day = quota in `config.md` — personalization over volume
- Never email the same business twice in one sequence position
- Every email identifies Plug AI and includes a real opt-out line; honor opt-outs instantly and log them in the lead file
- No purchased lists. Ever. Every contact was individually researched.
