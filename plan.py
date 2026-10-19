import re

def write_plan(content):
    with open('plan.md', 'w') as f:
        f.write(content)

plan = """Modo: completo
Reason: The request modifies core calculations (macros, targets, 1RM), application state (upgrading appRevision), and AI context.

1. *In `index.html`, Update `targetFor` and `goalsFor` functions*
   - Execute `python3 modify_targets.py` using `run_in_bash_session` to unconditionally apply C calculation changes and goal references.
   - Run `node verify.js` to read modified code to verify changes.

2. *In `index.html`, Update `#btn-prometabolic` logic and `upgradeTo22` migration*
   - Execute `python3 modify_prometabolic.py` to change `btn-prometabolic`'s onclick logic and apply `upgradeTo22` inside `migrate`.
   - Execute `python3 modify_version.py` to bump `APP_VERSION` to `v31`.
   - Execute `python3 modify_changelog.py` to add `v31` changelog entry.
   - Run `node verify.js` to confirm syntax.

3. *In `index.html`, Update `CONTEXT` and `state.context`*
   - Execute `python3 modify_context.py` to update the `CONTEXT` constant with the Peat/Dinkov rules.
   - Execute `grep -n "CONTEXT=" index.html` to read the updated `CONTEXT` and confirm it was modified correctly.

4. *In `index.html`, Modify `#balance-card` ratios (`renderRatios`)*
   - Execute `python3 modify_ratios.py` to change `cpRef` to use `3.0`, add A:D equilibrium, and Zn:Cu equilibrium to `#balance-card`.
   - Execute `python3 get_functions.py index.html renderRatios` to read `renderRatios` and confirm syntax.

5. *In `index.html`, Modify micro limits in 7-day accumulation*
   - Execute `python3 modify_iron_selenium.py` to edit `LENS` array limits and add Iron, Selenium, Vitamin A, and Iodine to the `LIMIT` set.
   - Execute `grep -n "LENS=" index.html` and `grep -n "LIMIT=" index.html` to ensure modifications are valid.

6. *In `index.html`, Improve Gym progression detection (`gpSessionMetrics` and `gpStatus`)*
   - Execute `python3 modify_gym.py` to change `m.e1rm` in `gpSessionMetrics` to Epley equation, and update `gpStatus` to mark "Progresión (+1RM)".
   - Execute `python3 get_functions.py index.html gpSessionMetrics gpStatus` to read and verify the edits were correctly applied.

7. *In `index.html`, Update Calendar and Header (`renderCalendar`, `renderHeader`)*
   - Execute `python3 modify_calendar.py` and `python3 modify_cal_logic.py` to update tabs and mini-dots per day.
   - Execute `python3 modify_header.py` to add the horizontal sliding chip bar in the header.
   - Execute `python3 get_functions.py index.html renderCalendar calendarCell` to read modified components, and `node verify.js` again to verify no breakages.

8. *Run Validation Check*
   - Run the final verification test suite using `node verify.js` to ensure all changes are correct and no regressions were introduced.

9. *Complete pre commit steps*
   - Complete pre commit steps to ensure proper testing, verification, review, and reflection are done.
"""
write_plan(plan)
