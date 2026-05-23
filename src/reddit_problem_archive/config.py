"""Configuration models for future Reddit API integration."""

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    """Environment-driven settings for the prototype."""

    reddit_client_id: str = ""
    reddit_client_secret: str = ""
    reddit_user_agent: str = ""
    database_url: str = "sqlite:///reddit_problem_archive.db"

    @classmethod
    def from_env(cls) -> "Settings":
        return cls(
            reddit_client_id=os.getenv("REDDIT_CLIENT_ID", ""),
            reddit_client_secret=os.getenv("REDDIT_CLIENT_SECRET", ""),
            reddit_user_agent=os.getenv("REDDIT_USER_AGENT", ""),
            database_url=os.getenv("DATABASE_URL", "sqlite:///reddit_problem_archive.db"),
        )
