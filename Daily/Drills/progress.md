# Progress

coding_level: 2
logic_level: 1
streak: 1
current_problem: night-market stall puzzle — place four vendors (Dita, Eko, Fina, Gilang) and four dishes (satay, martabak, bubur, es cendol) across stalls 1-4 from six facts, and prove the arrangement is unique
current_track: logic
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
- 2026-09-25 | logic | L1 | night-market stall puzzle — place four vendors and four dishes across stalls 1-4 from six facts and prove uniqueness | pending | AI used: pending

## Notes

- Grading is objective: coding attempts go in `Daily\Solutions\drill-YYYY-MM-DD.py` using the exact function name given in the problem, and the next run executes them against a reference implementation.
- **Logic days have no function.** The attempt file for a logic day is `Daily\Solutions\drill-YYYY-MM-DD.md` containing the assignment plus the written argument. The next run must check `current_track` in this file and look for the `.md` attempt, not a `.py`, on a logic day. Grading a logic attempt: the assignment must match the verified unique solution AND the argument must actually rule out the alternatives — a correct assignment with no argument, or with an argument that only checks the given facts against the answer rather than deriving it, grades as `not_solved`.
- AI use is recorded but never blocks a level-up. It is surfaced as a ratio in the Sunday review only.
- Do not delete the Rules or Log sections from a drill file — the next day's run reads them. Do not paste code into the drill file; code goes in `Daily\Solutions\`.
- Path was corrected on 2026-09-10 to `D:\Code\Daily-Drill\Daily\...` and runs against the new path succeed.
- 2026-09-10 → 2 solved in a row, so coding_level went 1 → 2 and streak reset to 0.
- Solutions files should contain the function only — no top-level `print` calls. Put test calls in a scratch file or under `if __name__ == "__main__":`. Raised on 09-10 and again on 09-25; the 09-15 file printed at import time.
- 2026-09-25 grading detail: the 09-15 attempt is correct but initialises the running maximum to `0`, which is only safe because the problem guarantees non-negative counts. It also shadows the builtin `max`. Neither affects the verdict; both were called out in the 09-25 drill.
- 2026-09-25: verdict solved → streak 0 → 1. A level-up needs streak 2, so coding_level stays at 2. `days_reissued` reset to 0 because the re-issued problem was answered and retired.
- Long gaps in September (09-11 to 09-13, 09-16 to 09-24) are the scheduled task not firing, not Rui skipping. No penalty was applied for any of them. The 09-13 and 09-20 Sunday reviews were missed and are not being backfilled.
- Weekday schedule (Asia/Jakarta): Mon-Thu coding, Fri logic, Sat re-solve, Sun review. 2026-09-25 is a Friday, hence a logic day; the logic track has never been drilled before, so it starts at L1.
- Verified answer to the 2026-09-25 logic problem (do NOT publish before grading): stall 1 Fina / martabak, stall 2 Gilang / satay, stall 3 Eko / bubur, stall 4 Dita / es cendol. Checked by exhaustive search over all 576 vendor-dish arrangements: exactly one satisfies all six facts, and every one of the six facts is load-bearing (dropping any single fact leaves 2 to 6 arrangements standing).
