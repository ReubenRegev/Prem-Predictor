import json
import pandas as pd


def load_raw_matches(filepath="data/pl_2024_25_raw.json"):
    with open(filepath, "r") as f:
        data = json.load(f)
    return data["matches"]


def matches_to_dataframe(matches):
    rows = []
    for match in matches:
        rows.append({
            "date": match["utcDate"],
            "home_team": match["homeTeam"]["name"],
            "away_team": match["awayTeam"]["name"],
            "home_goals": match["score"]["fullTime"]["home"],
            "away_goals": match["score"]["fullTime"]["away"],
            "status": match["status"]
        })
    return pd.DataFrame(rows)


def reshape_for_model(df):
    rows_for_model = []
    for _, row in df.iterrows():
        rows_for_model.append({
            "team": row["home_team"],
            "opponent": row["away_team"],
            "is_home": 1,
            "goals": row["home_goals"]
        })
        rows_for_model.append({
            "team": row["away_team"],
            "opponent": row["home_team"],
            "is_home": 0,
            "goals": row["away_goals"]
        })
    return pd.DataFrame(rows_for_model)


if __name__ == "__main__":
    matches = load_raw_matches()
    df = matches_to_dataframe(matches)
    df.to_csv("data/pl_2024_25.csv", index=False)
    print(f"Cleaned {len(df)} matches, saved to data/pl_2024_25.csv")