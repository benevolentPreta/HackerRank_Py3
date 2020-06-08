### Python2.7/3 scripts to generate a table of contents/progress in the root README.md file.

=============================================================================================

## Initial Usage
 1. run `update-list.py` to generate `challenges.json` file.
 2. run `mkdirs.py` to create directories for all of the challenges listed in `challenges.json`
 3. run `generate-README.py` to create the root `README.md` and update progress.

## Completing Challenges
 + Lack of `.py` file present in challenge directory will be marked as "No Attempt" in the README.md
 + `working.py` file in challenge directory will be marked as "Unsuccessful Attempt"
 + `solution.py` file in challgenge directory will be marked/couted as completed, and link to solution will be added to the README.md
