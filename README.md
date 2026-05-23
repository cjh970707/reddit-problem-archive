Create a minimal Python project scaffold and a detailed README for a read-only, non-commercial prototype called "Reddit Problem Archive."

Purpose:
This application is intended to analyze a limited set of publicly available Reddit posts and relevant public comments in order to identify recurring everyday problems, frustrations, unmet needs, and solution-seeking behavior expressed by Redditors.

The application will focus on discussions such as:
- repetitive or time-consuming everyday tasks,
- dissatisfaction with existing tools or workflows,
- questions asking for easier ways to solve common problems,
- practical difficulties related to productivity, personal finance, household management, meal preparation, homeownership, and small business operations.

Initial target subreddits:
- r/productivity
- r/Adulting
- r/personalfinance
- r/Frugal
- r/mealprep
- r/homeowners
- r/smallbusiness

Planned API behavior:
- Use Reddit's authorized Data API in a read-only manner.
- Retrieve a limited number of public posts and, where relevant, public comments from selected public subreddits.
- Search for public discussions containing problem- or solution-seeking expressions such as:
  - "I hate having to..."
  - "Is there an easier way..."
  - "How do you deal with..."
  - "There has to be a better way..."
  - "What do you use for..."
  - "This takes forever..."
  - "Does anyone else struggle with..."

Planned processing:
1. Retrieve public Reddit content through authorized API access.
2. Detect whether a post describes a recurring practical problem or request for a solution.
3. Generate an anonymized one-sentence summary of the problem.
4. Categorize the pain point, such as time burden, repetitive task, cost, confusion, inconvenience, or dissatisfaction with an existing solution.
5. Group similar anonymized problem summaries into aggregate themes.
6. Produce internal aggregate reports of recurring problem areas.

Data handling and compliance requirements:
- The application is read-only and will not post, comment, vote, message users, or perform moderation actions.
- It will not track individuals or create user profiles.
- It will not infer sensitive personal characteristics.
- It will not resell Reddit content or user-level data.
- It will not use Reddit content to train a machine learning model or large language model.
- Usernames will not be retained in the analytical dataset.
- Minimal source identifiers and URLs may be retained only for deduplication, source verification, and deletion synchronization.
- Deleted or unavailable Reddit content must be removed through periodic deletion synchronization.
- The initial version is for internal validation and non-commercial research only.

Please create:
- A professional README.md explaining the project purpose, planned architecture, API usage, privacy and data handling rules, and current non-commercial prototype status.
- A basic Python project structure suitable for future Reddit API integration.
- A .env.example file containing placeholder environment variables only, such as REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT, and DATABASE_URL.
- A requirements.txt file with minimal placeholder dependencies appropriate for a future Python API client project.
- A .gitignore appropriate for Python and environment-variable files.

Do not include any actual Reddit credentials, access tokens, API keys, or functional scraping behavior. Do not implement unauthorized API access. The repository should serve primarily as transparent technical documentation for a planned Reddit Data API access request.
