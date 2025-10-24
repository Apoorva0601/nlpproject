NL Presume Parse Final
======================

A small Python project that parses resumes and matches them to job descriptions.

Project layout
--------------

- `main_app.py` - simple entry point to run the application.
- `modules/resume_parser.py` - resume parsing utilities.
- `modules/job_matcher.py` - job matching logic that compares parsed resumes to `dataset/jobs.csv`.
- `dataset/jobs.csv` - CSV file containing job records used for matching.
- `requirements.txt` - Python package dependencies.
- `venn_env/` - included local virtual environment (DO NOT commit this to upstream repos; it's included here for convenience).

Quick start (Windows - cmd.exe)
-------------------------------

1. (Optional) Create and activate a virtual environment:

   python -m venv .venv
   .\.venv\Scripts\activate.bat

2. Install dependencies:

   pip install -r requirements.txt

3. Run the app:

   python main_app.py

Notes
-----

- The repository already contains a virtual environment folder `venn_env/` used during development. It's usually better to create a fresh environment locally as shown above.
- Inspect `dataset/jobs.csv` to see expected job columns and sample data.
- `main_app.py` is the runnable script; open it to find any CLI options or config values.

Files of interest
-----------------

- `modules/resume_parser.py` — Extracts structured fields (name, email, skills, experience, education) from resumes. Use this module to convert raw resume text/files into dicts for matching.
- `modules/job_matcher.py` — Accepts parsed resume data and scores/ranks jobs from `dataset/jobs.csv`.

Module details and usage
------------------------

- `modules/resume_parser.py`
   - Main function: `extract_skills(text)`
      - Input: a string containing the resume text.
      - Output: a deduplicated list of skill keywords found in the text (based on `SKILL_KEYWORDS`).
   - Notes: It uses NLTK tokenization and the English stopword list. If you run this on a fresh environment you may need to download NLTK data (see Notes below).

- `modules/job_matcher.py`
   - Main function: `match_jobs(skills, csv_path='dataset/jobs.csv')`
      - Input: `skills` — iterable of skill strings (e.g., the output of `extract_skills`), and optional `csv_path` to the jobs CSV.
      - Output: a pandas DataFrame with the top 10 matches, columns `Category`, `Feature`, and `Match_Score` (cosine similarity between user skills and job text).
   - Matching approach: concatenates the `Feature` and `Category` columns into a `Combined` text column, vectorizes with `CountVectorizer`, then computes cosine similarity with the user's skills string.

Example (script usage)
----------------------

You can call the modules from a small script or an interactive session. Example (Python):

```python
from modules.resume_parser import extract_skills
from modules.job_matcher import match_jobs

text = open('example_resume.txt', 'r', encoding='utf-8').read()
skills = extract_skills(text)
print('Detected skills:', skills)

matches = match_jobs(skills)
print(matches)
```

Dataset: `dataset/jobs.csv`
--------------------------

The jobs data is a CSV with (at minimum) these columns:

- `ID` — numeric job identifier
- `Category` — job category (string)
- `Feature` — a long free-text field describing job details (used for matching)

The `job_matcher` code expects `Category` and `Feature` to exist. `Feature` typically contains the role description, responsibilities, keywords and/or a pasted resume sample used as the job text for matching.

Notes
-----
- NLTK: `modules/resume_parser.py` uses `nltk.tokenize.word_tokenize` and `nltk.corpus.stopwords`. If you haven't already downloaded the NLTK data in your environment run the Python REPL and execute:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

- Virtualenv: the repository contains an existing `venn_env/` virtual environment. It's recommended to create a fresh virtual environment locally (see Quick start) rather than reusing `venn_env` when sharing or deploying.

- Streamlit UI: `main_app.py` is a Streamlit app that provides an upload UI (PDF/TXT). Run with `streamlit run main_app.py` instead of `python main_app.py` if you want the Streamlit server UI. The README above shows the minimal `python main_app.py` run; to use Streamlit's interactive web UI run:

```cmd
streamlit run main_app.py
```


Contributing
------------

- Create an issue describing the feature or bug.
- Fork and submit a pull request with tests where applicable.

License
-------

Proprietary / unspecified. Add a license file if you intend to open-source this project.

Next steps / ideas
------------------

- Add CLI arguments or a simple web UI to upload resumes and show best matches.
- Add unit tests for `resume_parser` and `job_matcher`.
- Add input validation and better CSV schema documentation.

