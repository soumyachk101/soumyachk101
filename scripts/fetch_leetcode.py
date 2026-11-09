"""Fetch public LeetCode stats for soumya-chk101. No auth needed.

Queries LeetCode's public GraphQL endpoint for solved counts, ranking,
calendar streak, and badges, and writes data/leetcode.json:

    python scripts/fetch_leetcode.py
"""

import json
import os
import re
import sys
import requests

USERNAME = "soumya-chk101"
OUT = "data/leetcode.json"

CORE_QUERY = """
query ($user: String!) {
  allQuestionsCount { difficulty count }
  matchedUser(username: $user) {
    username
    profile { ranking }
    submitStatsGlobal { acSubmissionNum { difficulty count } }
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

CALENDAR_QUERY = """
query ($user: String!) {
  matchedUser(username: $user) {
    userCalendar { streak totalActiveDays activeYears }
  }
}
"""

HEADERS = {
    "Content-Type": "application/json",
    "Referer": "https://leetcode.com",
    "User-Agent": "profile-art-refresh/1.0",
}


def load_previous_calendar() -> dict:
    if os.path.exists(OUT):
        try:
            with open(OUT, encoding="utf-8") as f:
                prev = json.load(f)
            cal = prev.get("calendar") or {}
            if cal:
                return {
                    "max_streak": cal.get("max_streak", 0),
                    "active_days": cal.get("active_days", 0),
                    "active_years": cal.get("active_years", []),
                }
        except Exception:
            pass
    return {"max_streak": 0, "active_days": 0, "active_years": []}


def fetch_calendar() -> dict | None:
    try:
        resp = requests.post(
            "https://leetcode.com/graphql",
            json={"query": CALENDAR_QUERY, "variables": {"user": USERNAME}},
            headers=HEADERS,
            timeout=20,
        )
        resp.raise_for_status()
        payload = resp.json()
        matched = (payload.get("data") or {}).get("matchedUser")
        if matched and matched.get("userCalendar"):
            cal = matched["userCalendar"]
            return {
                "max_streak": cal.get("streak", 0),
                "active_days": cal.get("totalActiveDays", 0),
                "active_years": cal.get("activeYears", []),
            }
        errs = [e.get("message", "") for e in payload.get("errors", [])]
        print(f"warning: userCalendar unavailable ({'; '.join(errs) or 'null'}); preserving previous calendar stats")
    except Exception as exc:
        print(f"warning: userCalendar fetch failed ({exc}); preserving previous calendar stats")
    return None


def main() -> None:
    resp = requests.post(
        "https://leetcode.com/graphql",
        json={"query": CORE_QUERY, "variables": {"user": USERNAME}},
        headers=HEADERS,
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
    badges = data["matchedUser"].get("badges") or []

    calendar = fetch_calendar() or load_previous_calendar()
    for b in badges:
        m = re.search(r"(\d+)\s+Days\s+Badge", b.get("displayName", ""))
        if m and calendar.get("active_days", 0) < int(m.group(1)):
            calendar["active_days"] = int(m.group(1))

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
        "badges": badges,
        "calendar": calendar,
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print(f"wrote {OUT}: {out['solved']['All']} solved (E:{out['solved']['Easy']} M:{out['solved']['Medium']} H:{out['solved']['Hard']}), rank #{out['ranking']:,}, streak {out['calendar']['max_streak']}")


if __name__ == "__main__":
    main()
