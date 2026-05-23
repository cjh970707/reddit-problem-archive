# Reddit Problem Archive

Read-only, non-commercial prototype for analyzing a limited set of publicly available Reddit discussions to identify recurring practical problems, frustrations, unmet needs, and solution-seeking behavior.

## Project Status

This repository currently provides **planning documentation and a minimal Python scaffold only**.

- Prototype stage: **internal validation / non-commercial research**
- API behavior: **read-only**
- Not implemented yet: data collection, NLP classification, aggregation pipelines, reporting jobs

## Purpose

The Reddit Problem Archive is intended to help identify recurring everyday pain points discussed publicly on Reddit, including:

- repetitive or time-consuming tasks
- dissatisfaction with existing tools/workflows
- requests for easier ways to solve common problems
- practical difficulties in productivity, personal finance, household management, meal preparation, homeownership, and small business operations

## Initial Target Subreddits

- `r/productivity`
- `r/Adulting`
- `r/personalfinance`
- `r/Frugal`
- `r/mealprep`
- `r/homeowners`
- `r/smallbusiness`

## Planned API Usage (Read-Only)

The intended implementation is to use Reddit's authorized Data API in a strictly read-only manner:

1. Retrieve a limited number of public posts from selected public subreddits.
2. Retrieve relevant public comments where needed for context.
3. Search for problem/solution-seeking expressions such as:
   - "I hate having to..."
   - "Is there an easier way..."
   - "How do you deal with..."
   - "There has to be a better way..."
   - "What do you use for..."
   - "This takes forever..."
   - "Does anyone else struggle with..."

## Planned Processing Workflow

1. Retrieve public Reddit content through authorized API access.
2. Detect whether a post describes a recurring practical problem or request for a solution.
3. Generate an anonymized one-sentence summary of the problem.
4. Categorize pain points (for example: time burden, repetitive task, cost, confusion, inconvenience, dissatisfaction).
5. Group similar anonymized summaries into aggregate themes.
6. Produce internal aggregate reports of recurring problem areas.

## Privacy, Data Handling, and Compliance Commitments

- Read-only operation only: no posting, commenting, voting, messaging, or moderation actions.
- No individual tracking or user profile creation.
- No inference of sensitive personal characteristics.
- No resale of Reddit content or user-level data.
- No use of Reddit content to train machine learning models or large language models.
- Usernames are not retained in the analytical dataset.
- Only minimal source identifiers/URLs may be retained for deduplication, source verification, and deletion synchronization.
- Deleted or unavailable Reddit content must be removed through periodic deletion synchronization.
- Initial use is internal and non-commercial.

## Minimal Python Scaffold

The scaffold is intentionally lightweight and does not perform API access yet.

```text
.
├── .env.example
├── pyproject.toml
├── requirements.txt
└── src/
    └── reddit_problem_archive/
        ├── __init__.py
        ├── __main__.py
        └── config.py
```

## Local Setup (Scaffold Only)

1. Create and activate a virtual environment.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Copy environment template:

   ```bash
   cp .env.example .env
   ```

4. (Optional) Run the placeholder module:

   ```bash
   PYTHONPATH=src python -m reddit_problem_archive
   ```

## Environment Variables

See `.env.example` for placeholder values:

- `REDDIT_CLIENT_ID`
- `REDDIT_CLIENT_SECRET`
- `REDDIT_USER_AGENT`
- `DATABASE_URL`

## Important Notes

- This repository does **not** include real credentials or access tokens.
- This repository does **not** implement scraping or unauthorized API access.
- This repository is intended to support transparent technical documentation for a planned Reddit Data API access request.
