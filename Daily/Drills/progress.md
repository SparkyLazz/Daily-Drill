# Progress

coding_level: 2
logic_level: 1
streak: 0
current_problem: largest drop between an earlier and a later hourly loaf count; 0 if it never drops (`solve(counts: list[int]) -> int`)
current_track: coding
days_reissued: 1

## History

- 2026-09-09 | coding | L1 | rearrange a list in place so zeros follow non-zeros, order of non-zeros preserved | **solved** (re-verified 2026-09-10: 613 cases incl. 600 randomized, 0 failures) | AI used: unknown (Log section was deleted from the file)
- 2026-09-10 | — | — | no drill issued — task was pointing at D:\Code\DailyWorks\Daily, which no longer exists after the vault moved | system failure, not a skip | streak unaffected
- 2026-09-10 | coding | L1 | index of the final occurrence of the largest value in a list; -1 if empty | **solved** (graded 2026-09-14: 718 cases incl. 700 randomized, 0 failures; input not modified) | AI used: no | 52 minutes — over the 45-minute cap
- 2026-09-11 | — | — | no drill issued — task did not run | system gap, not a skip | streak unaffected
- 2026-09-12 | — | — | no drill issued — task did not run | system gap, not a skip | streak unaffected
- 2026-09-13 | — | — | no drill issued — task did not run (Sunday review missed) | system gap, not a skip | streak unaffected
- 2026-09-14 | coding | L2 | largest drop between an earlier and a later hourly loaf count; 0 if it never drops | **skipped** (graded 2026-09-15: no `Solutions\drill-2026-09-14.py`; Log section left as the blank template) | AI used: not reported
- 2026-09-15 | coding | L2 | largest drop between an earlier and a later hourly loaf count; 0 if it never drops — **re-issue #1, unchanged** | pending | AI used: pending

## Notes

- Grading is objective: attempts go in `Daily\Solutions\drill-YYYY-MM-DD.py` using the exact function name given in the problem, and the next run executes them against a reference implementation.
- AI use is recorded but never blocks a level-up. It is surfaced as a ratio in the Sunday review only.
- Do not delete the Rules or Log sections from a drill file — the next day's run reads them. Do not paste code into the drill file; code goes in `Daily\Solutions\`.
- Path was corrected on 2026-09-10 to `D:\Code\Daily-Drill\Daily\...` and the first run against the new path succeeded.
- 2026-09-10 → 2 solved in a row, so coding_level went 1 → 2 and streak reset to 0.
- Solutions files should contain the function only — no top-level `print` calls. Put test calls in a scratch file or under `if __name__ == "__main__":`.
- Gap of 2026-09-11 to 09-13: no drills were issued because the task did not fire. Nothing was skipped by Rui; no penalty applied. The 09-13 Sunday review was missed and is not being backfilled — the next Sunday review (2026-09-20) covers the week.
- 2026-09-15: the 09-14 problem is re-issued unchanged because it was skipped. The solution was deliberately withheld from the 09-15 drill file for that reason. `days_reissued` counts how many times this same problem has been re-issued; at 3 consecutive not_solved the coding track drops a level and a different problem is given. A skip re-issues indefinitely and does not trigger the level drop.
