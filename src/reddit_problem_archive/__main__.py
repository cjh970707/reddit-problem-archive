"""Entry point for the Reddit Problem Archive prototype scaffold."""

from .config import Settings


def main() -> None:
    settings = Settings.from_env()
    print("Reddit Problem Archive prototype scaffold")
    print("Status: non-commercial, read-only planning prototype")
    print(f"Configured user-agent placeholder set: {bool(settings.reddit_user_agent)}")


if __name__ == "__main__":
    main()
