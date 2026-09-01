"""Dictionary Filtering, Conditionals, and Range Lookup in Python Loops.

Demonstrates iterating through collections of user dictionaries, filtering based on
social media platform presence ('linkedin' vs 'twitter'), and matching user IDs
against numeric ranges.

Import Notes:
    - 'from typing import List, Dict, Any, Tuple': Standard library typing module imports
      used for static type annotations on dictionary sequences and structured returns.
"""

from typing import List, Dict, Any, Tuple


def get_sample_users() -> List[Dict[str, Any]]:
    """Return a sample list of user detail dictionaries."""
    return [
        {"id": 3, "fname": "Tim", "lname": "John", "email": "tim.john@icloud.com", "linkedin": True},
        {"id": 5, "fname": "Dielman", "lname": "Ary", "email": "dielman.ary@icloud.com", "linkedin": False},
        {"id": 7, "fname": "Holly", "lname": "Smith", "email": "holly.smith@icloud.com", "twitter": True},
        {"id": 9, "fname": "Alan", "lname": "Cory", "email": "alan.cory@icloud.com", "twitter": False},
    ]


def display_user_summaries(users: List[Dict[str, Any]]) -> List[str]:
    """Format and display user summaries (ID, First Name, Last Name, Email)."""
    summaries: List[str] = []
    print("Id   Fname    Lname    Email")
    print("-" * 45)
    for detail in users:
        summary = f"{detail['id']:<4d} {detail['fname']:<8s} {detail['lname']:<8s} {detail['email']}"
        summaries.append(summary)
        print(summary)
    return summaries


def filter_users_by_social_platform(
    users: List[Dict[str, Any]]
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """Filter user dictionaries into separate active Twitter and LinkedIn user lists.

    Args:
        users: List of user detail dictionaries.

    Returns:
        Tuple containing (active_twitter_users, active_linkedin_users).
    """
    twitter_users: List[Dict[str, Any]] = []
    linkedin_users: List[Dict[str, Any]] = []

    print("\n--- Social Media Account Verification ---")
    for user in users:
        # Standardized key 'twitter' (corrected from legacy 'twetter')
        if "twitter" in user and user["twitter"] is True:
            twitter_users.append(user)
            print(f"Twitter User Found: {user['fname']} {user['lname']}")
        elif "linkedin" in user and user["linkedin"] is True:
            linkedin_users.append(user)
            print(f"LinkedIn User Found: {user['fname']} {user['lname']}")

    return twitter_users, linkedin_users


def search_users_by_id_range(
    users: List[Dict[str, Any]], max_range: int = 10
) -> List[Dict[str, Any]]:
    """Search through range numbers and match user IDs against range values.

    Args:
        users: List of user detail dictionaries.
        max_range: Range ceiling to search through (default: 10).

    Returns:
        List of user dictionaries matching range IDs.
    """
    matched_users: List[Dict[str, Any]] = []
    print(f"\n--- Searching through ID range 0 to {max_range - 1} ---")

    for step in range(0, max_range):
        for user in users:
            if user["id"] == step:
                matched_users.append(user)
                print(f"Matched ID {step}: {user['fname']} {user['lname']} (Email: {user['email']})")

    return matched_users


def demo_for_dict() -> None:
    """Run dictionary filtering and range search demonstration."""
    users = get_sample_users()

    print("=== 1. Basic User Summaries ===")
    display_user_summaries(users)

    print("\n=== 2. Social Media Platform Filtering ===")
    tw_users, li_users = filter_users_by_social_platform(users)
    print(f"Active Twitter Count: {len(tw_users)}")
    print(f"Active LinkedIn Count: {len(li_users)}")

    print("\n=== 3. Range ID Matching ===")
    search_users_by_id_range(users, 10)


if __name__ == "__main__":
    demo_for_dict()
