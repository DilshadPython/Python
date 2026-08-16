from dataclasses import dataclass
import os


@dataclass(frozen=True)
class AppConfig:
    # Strict typed settings with immutable guarantees
    db_uri: str
    secret_key: str
    debug_mode: bool = False

    @classmethod
    def from_env(cls) -> "AppConfig":
        db = os.getenv("DATABASE_URL")
        key = os.getenv("SECRET_KEY")
        if not db or not key:
            raise ValueError("DATABASE_URL and SECRET_KEY must be set!")

        return cls(
            db_uri=db,
            secret_key=key,
            debug_mode=os.getenv("DEBUG") == "1"
        )