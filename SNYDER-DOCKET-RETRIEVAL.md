# Retrieving the Snyder docket

**STATUS: a standing want, not a pending action. Stewart, 25 August 2026: "I'll probably not
do this but keep it on file as a want."**

**Do not present this as imminent, and do not keep raising it.** It stays on file because the
information is genuinely unobtainable any other way and would close four open questions at
once, so if the opportunity ever arises the script is ready. The tracker should carry the
Grillmair tail as **confirmed unreported**, which is honest and is the correct standing
position, rather than as pending retrieval.

**For Stewart, if he ever wants it. This is a manual retrieval. Claude cannot do it, because
the LA Superior Court case portal does not expose criminal minute orders to anonymous web
requests and there is no public API.**

## What we are trying to learn

**People v. Freddy Snyder, Los Angeles County Superior Court case 26AVCF00232.**

Snyder is charged with the February 16, 2026 killing of Carl Grillmair, plus a
first-degree residential burglary count for conduct in late December 2025 that was charged
only after the killing.

Three questions, in priority order:

1. **Was Snyder held to answer at the preliminary hearing on June 5, 2026, or was it continued?** Media coverage stops dead after May 28, 2026. No outlet, DA release, or accessible record states the outcome.
2. **What happened at the June 18, 2026 date?** That is the last documented court date in the file.
3. **Was the firearm enhancement amended down** between the February complaint (intentional discharge causing great bodily injury) and the May arraignment (personal use of a rifle)?

## Why it matters

Grillmair is **S3/P1/I3**, the strongest documented sequence in the tracker and the case that
drove the whole v2 redesign. The sequence argument rests on a chain of institutional
failures. Whatever the court did on June 5 either extends that chain or closes part of it.
Right now the tracker has to say "confirmed unreported," which is honest but weak, and a
hostile reader will notice that the strongest case has an unresolved tail.

---

## Option 1: Phone the criminal clerk (fastest, free)

**Michael D. Antonovich Antelope Valley Courthouse**
42011 4th Street West, Lancaster, CA 93534
**Criminal Clerk's Office, 1st Floor: (661) 483-5798**
General information: (661) 483-5500
Clerk's office hours 8:30 a.m. to 4:30 p.m., Mon-Fri, except court holidays. Call early.

### What to say

> "Hi, I'd like the case status and the minute orders for a criminal case. Case number is
> two-six-A-V-C-F-zero-zero-two-three-two, People versus Freddy Snyder. I'm looking for
> what happened at the June 5, 2026 preliminary hearing and the June 18, 2026 date.
> Can you tell me whether the defendant was held to answer, and what the next scheduled
> date is?"

### Notes on the call

- You do **not** need to be a party, an attorney, or state a reason. California criminal minute orders are presumptively public records.
- If they ask who you are, "a member of the public" is a complete answer.
- Read the case number back slowly. `26AVCF00232`. The `AV` is the Antelope Valley designator.
- Ask specifically for the **minute order**, not "the outcome". Minute order is the term that gets you the clerk's actual entry rather than a summary.
- Also worth asking: **"Is there a next court date on calendar?"** A future date tells you the case is alive and roughly where it is, even if they will not read you the June 5 entry over the phone.
- If the clerk will not read minute orders over the phone (some will not), go to Option 2 and ask them in the same call how to submit the request.

---

## Option 2: Written records request (authoritative, produces a document you can cite)

Copies are **$0.50 per page.** Certification, if you want it, is **$25 per document.** You
do not need certification for research purposes; certification only matters if you need it
to be legally self-authenticating.

Two routes:

**In person, at the courthouse where the case was filed.** Go to the Criminal Records window
at the Antelope Valley courthouse with government photo ID, fill out the Criminal Records
Request Form at the counter, pay the per-page fee. This is the fastest way to walk out with
paper the same day.

**By mail.** Download the Criminal Records Request Form from lacourt.org, enclose a
self-addressed stamped envelope and a check payable to "Los Angeles Superior Court" with
**"Not to Exceed $20.00"** written on the memo line. Mail to:

```
Los Angeles Superior Court
Criminal Records Division
111 North Hill Street
Los Angeles, CA 90012
```

Note that the central Criminal Records Division at 111 N Hill handles mail requests, but the
file itself lives at the Antelope Valley courthouse, so a mailed request may route slower
than going to Lancaster directly.

---

## Option 3: The online case portal

`lacourt.org` has a criminal case search. It is worth two minutes before you pick up the
phone, but set expectations low: LA's public criminal portal typically returns only
defendant name, case number, charges and next hearing date, and often requires a date of
birth or driver's licence number to disambiguate. **It generally does not surface minute
order text.** If it shows a future hearing date, that alone partly answers question 1,
because a case that was dismissed would not have one.

---

## What to bring back

Whatever you get, capture these fields and hand them to a Claude session:

| Field | Value |
|---|---|
| June 5 2026 minute order text, or clerk's summary | |
| Was defendant held to answer? | |
| June 18 2026 outcome | |
| Current charges as of today, with enhancements | |
| Firearm enhancement: amended or unchanged? | |
| Next scheduled date and department | |
| Any dismissal, plea, or continuance, with the stated reason | |

Then say "update the Grillmair record from the docket" and the session will fold it into
`PROJECT.md`, the open-questions list, and the case record in `the-vanishing-v2.html`.

## Recording rule

Record what the docket says, not what it implies. If Snyder was held to answer, that is a
routine outcome and the tracker should say so plainly rather than dress it up. If the
hearing was continued for an unremarkable reason, that closes an open question rather than
opening a new one, and closing questions is how this project stays credible.
