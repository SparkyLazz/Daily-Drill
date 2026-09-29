# Progress

coding_level: 2
logic_level: 1
streak: 1
current_problem: village weighing station — the largest pumpkin weight strictly less than the heaviest recorded weight; -1 if the list is empty or all weights are equal
current_track: coding
days_reissued: 0

## History

- 2026-09-09 | coding | L1 | rearrange a list in place so zeros follow non-zeros, order of non-zeros preserved | **solved** (re-verified 2026-09-10: 613 cases incl. 600 randomized, 0 failures) | AI used: unknown (Log section was deleted from the file)
- 2026-09-10 | — | — | no drill issued — task was pointing at D:\Code\DailyWorks\Daily, which no longer exists after the vault moved | system failure, not a skip | streak unaffected
- 2026-09-10 | coding | L1 | index of the final occurrence of the largest value in a list; -1 if empty | **solved** (graded 2026-09-14: 718 cases incl. 700 randomized, 0 failures; input not modified) | AI used: no | 52 minutes — over the 45-minute cap
- 2026-09-11 | — | — | no drill issued — task did not run | system gap, not a skip | streak unaffected
- 2026-09-12 | — | — | no drill issued — task did not run | system gap, not a skip | streak unaffected
- 2026-09-13 | — | — | no drill issued — task did not run (Sunday review missed) | system gap, not a skip | streak unaffected
- 2026-09-14 | coding | L2 | largest drop between an earlier and a later hourly loaf count; 0 if it never drops | **skipped** (graded 2026-09-15: no `Solutions\drill-2026-09-14.py`; Log section left as the blank template) | AI used: not reported
- 2026-09-15 | coding | L2 | largest drop between an earlier and a later hourly loaf count; 0 if it never drops — re-issue #1, unchanged | **solved** (graded 2026-09-25: 697 cases incl. 600 randomized + 80 pre-sorted + 15 edge cases, 0 failures; input not modified; 100k list in 0.006 s) | AI used: not reported (Log left blank) | minutes: not reported
- 2026-09-16 | — | — | no drill issued — task did not run | system gap, not a skip | streak unaffected
- 2026-09-17 | — | — | no drill issued — task did not run | system gap, not a skip | streak unaffected
- 2026-09-18 | — | — | no drill issued — task did not run | system gap, not a skip | streak unaffected
- 2026-09-19 | — | — | no drill issued — task did not run | system gap, not a skip | streak unaffected
- 2026-09-20 | — | — | no drill issued — task did not run (Sunday review missed) | system gap, not a skip | streak unaffected
- 2026-09-21 | — | — | no drill issued — task did not run | system gap, not a skip | streak unaffected
- 2026-09-22 | — | — | no drill issued — task did not run | system gap, not a skip | streak unaffected
- 2026-09-23 | — | — | no drill issued — task did not run | system gap, not a skip | streak unaffected
- 2026-09-24 | — | — | no drill issued — task did not run; Rui submitted his 09-15 attempt on this date (16:53 Jakarta) | system gap, not a skip | streak unaffected
- 2026-09-25 | logic | L1 | night-market stall puzzle — place four vendors and four dishes across stalls 1-4 from six facts and prove uniqueness | **not_solved** (graded 2026-09-28: assignment in `Solutions\drill-2026-09-25.md` matches the unique solution confirmed by exhaustive search over all 576 arrangements, but the file contains no argument at all — four lines naming the result and nothing else. The problem and the vault grading rule both require the derivation.) | AI used: not reported (Log left blank) | minutes: not reported
- 2026-09-26 | — | — | no drill issued — task did not run (Saturday re-solve missed) | system gap, not a skip | streak unaffected
- 2026-09-27 | — | — | no drill issued — task did not run (Sunday review missed) | system gap, not a skip | streak unaffected
- 2026-09-28 | coding | L2 | ferry turnstile — length of the longest stretch of consecutive minutes whose passenger count rises strictly each minute; 0 on an empty list | **solved** (graded 2026-09-29: 618 cases — 2 examples, 17 edge cases, 600 randomized lists of length 0-25 over ceilings 2/3/6/20/1000/10**9 — cross-checked against both a reference implementation and an independent O(n²) brute force on every case ≤ 25 elements; 0 failures; input not modified; 100k list in 0.012 s) | AI used: not reported (Log left blank) | minutes: not reported
- 2026-09-29 | coding | L2 | village weighing station — the largest pumpkin weight strictly less than the heaviest recorded weight; -1 if the list is empty or all weights are equal | pending | AI used: pending

## Notes

- Grading is objective: coding attempts go in `Daily\Solutions\drill-YYYY-MM-DD.py` using the exact function name given in the problem, and the next run executes them against a reference implementation.
- **Logic days have no function.** The attempt file for a logic day is `Daily\Solutions\drill-YYYY-MM-DD.md` containing the assignment plus the written argument. The next run must check `current_track` in this file and look for the `.md` attempt, not a `.py`, on a logic day. Grading a logic attempt: the assignment must match the verified unique solution AND the argument must actually rule out the alternatives — a correct assignment with no argument, or with an argument that only checks the given facts against the answer rather than deriving it, grades as `not_solved`.
- AI use is recorded but never blocks a level-up. It is surfaced as a ratio in the Sunday review only.
- Do not delete the Rules or Log sections from a drill file — the next day's run reads them. Do not paste code into the drill file; code goes in `Daily\Solutions\`.
- Path was corrected on 2026-09-10 to `D:\Code\Daily-Drill\Daily\...` and runs against the new path succeed.
- **Date convention: the drill filename uses the Asia/Jakarta date at fire time.** The task fires at 23:15 UTC, which is 06:15 the next morning in Jakarta, so the run that fires on UTC 09-28 produces `drill-2026-09-29.md`. Do not use the UTC date.
- 2026-09-10 → 2 solved in a row, so coding_level went 1 → 2 and streak reset to 0.
- **2026-09-29: verdict solved on the 09-28 coding problem → streak 0 → 1.** Not yet at 2, so coding_level stays at 2. One more solved coding day raises it to 3 ("rearrange a list in place, or compare from both ends") and resets streak to 0.
- Only one `streak` field exists in this file, so a not_solved on either track resets it; level-ups remain per-track.
- **The top-level `print` problem is now four-for-four.** Raised 09-10, 09-25, 09-28 and 09-29. The 09-28 file ends with `exampleList = [1, 1, 1]` / `print(solve(exampleList))`, which executes at import time and prints into the grading harness. It has never changed the verdict — the harness captures and discards stdout — but keep raising it every single day until a submitted file is clean. If a future file's import-time output ever makes the function itself ungradeable, that is a not_solved.
- Also on 09-28: the identifier `strech` (a typo for stretch/streak) appears five times. Cosmetic, noted once, not worth repeating daily.
- **Five drill files in a row with a completely blank Log** (09-14, 09-15, 09-25, 09-28, and 09-28's `AI used` line still carrying both options): no minutes, no AI answer, no block, no change. This is the only instrument in the system measuring anything other than pass/fail, and it is currently returning nothing. In particular there is still no minutes figure for any L2 coding problem, so there is no evidence about whether L2 is easy or hard for him. Keep raising it every day until it changes.
- **The logic track's failure mode is the argument, not the answer** (09-25). Rui got the assignment exactly right and wrote no derivation. The next logic day (Friday 2026-10-02) must restate the argument requirement prominently in the problem body AND in the constraints. The 09-25 night-market problem is **retired** — its full proof was published in the 09-28 drill and it must never be re-issued. The logic re-issue counter stays at 0 and a fresh L1 logic problem is due on Friday.
- Long gaps in September (09-11 to 09-13, 09-16 to 09-24, 09-26 to 09-27) are the scheduled task not firing, not Rui skipping. No penalty was applied for any of them. The 09-13, 09-20 and 09-27 Sunday reviews and the 09-26 Saturday re-solve were missed and are not being backfilled. The task has now fired two days running (09-28, 09-29).
- Weekday schedule (Asia/Jakarta): Mon-Thu coding, Fri logic, Sat re-solve, Sun review. 2026-09-29 is a Tuesday, hence a coding day at the current coding level of 2.
- **Saturday 2026-10-03 re-solve:** as of today the only unsolved item this week is nothing — 09-28 is solved and 09-25 is retired. If the rest of the week is also solved, Saturday gets a fresh problem one level above the then-current coding level, labelled a stretch that does not affect the ladder.
- Verified reference for the 2026-09-29 coding problem (do NOT publish before grading): walk the list once carrying the largest value seen and the largest value seen that is strictly smaller than it; when a new value exceeds the largest, the old largest becomes the runner-up; when it is smaller than the largest but larger than the runner-up (and not equal to the largest), it becomes the runner-up; return -1 if no runner-up was ever set. Equivalent to `sorted(set(weights), reverse=True)[1]`. Checked against that set-based brute force on 717 cases (2 examples, 15 hand-built edge cases — empty, single, single zero, all-same of length 50, every two-element shape, `10**9` pairs, `0`/`10**9`, max-with-duplicate, zeros-then-one, runner-up first, runner-up last — plus 700 randomized lists of length 0-30 over value ceilings 1/2/3/5/20/1000/10**9), 0 failures, input never modified, 100,000 elements in 0.004 s.
