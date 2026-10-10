"""Fetch public LeetCode stats for soumya-chk101. No auth needed.

Queries LeetCode's public GraphQL endpoint for solved counts, ranking,
calendar streak, and badges, and writes data/leetcode.json:

    python scripts/fetch_leetcode.py
"""

import json
import sys
import requests

USERNAME = "soumya-chk101"
OUT = "data/leetcode.json"

QUERY = """
query ($user: String!) {
  allQuestionsCount { difficulty count }
  matchedUser(username: $user) {
    username
    profile { ranking }
    submitStatsGlobal { acSubmissionNum { difficulty count } }
    userCalendar { streak totalActiveDays activeYears }
    badges { name displayName icon creationDate }
  }
  userContestRanking(username: $user) {
    rating
    topPercentage
    attendedContestsCount
    badge { name }
  }
}
"""


def main() -> None:
    resp = requests.post(
        "https://leetcode.com/graphql",
        json={"query": QUERY, "variables": {"user": USERNAME}},
        headers={
            "Content-Type": "application/json",
            "Referer": "https://leetcode.com",
            "User-Agent": "profile-art-refresh/1.0",
        },
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json().get("data", {})
    if not data.get("matchedUser"):
        sys.exit(f"LeetCode user {USERNAME} not found in response")

    totals = {q["difficulty"]: q["count"] for q in data.get("allQuestionsCount", [])}
    solved = {
        s["difficulty"]: s["count"]
        for s in data["matchedUser"]["submitStatsGlobal"]["acSubmissionNum"]
    }
    contest = data.get("userContestRanking") or {}

    out = {
        "username": USERNAME,
        "ranking": data["matchedUser"]["profile"]["ranking"],
        "solved": {
            "All": solved.get("All", 0),
            "Easy": solved.get("Easy", 0),
            "Medium": solved.get("Medium", 0),
            "Hard": solved.get("Hard", 0),
        },
        "totals": {
            "All": totals.get("All", 3400),
            "Easy": totals.get("Easy", 850),
            "Medium": totals.get("Medium", 1750),
            "Hard": totals.get("Hard", 800),
        },
        "contest": {
            "rating": round(contest.get("rating") or 0),
            "top_percent": contest.get("topPercentage"),
            "attended": contest.get("attendedContestsCount") or 0,
            "badge": (contest.get("badge") or {}).get("name") or "",
        },
        "badges": data["matchedUser"].get("badges") or [],
        "calendar": {
            "max_streak": (data["matchedUser"].get("userCalendar") or {}).get("streak", 0),
            "active_days": (data["matchedUser"].get("userCalendar") or {}).get("totalActiveDays", 0),
            "active_years": (data["matchedUser"].get("userCalendar") or {}).get("activeYears", []),
        },
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print(f"wrote {OUT}: {out['solved']['All']} solved (E:{out['solved']['Easy']} M:{out['solved']['Medium']} H:{out['solved']['Hard']}), rank #{out['ranking']:,}, streak {out['calendar']['max_streak']}")


if __name__ == "__main__":
    main()
