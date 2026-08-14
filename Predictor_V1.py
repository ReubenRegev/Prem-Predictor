from data_prep import load_raw_matches, matches_to_dataframe, reshape_for_model
from modeling import fit_model, predict_expected_goals, match_outcome_probabilities

matches = load_raw_matches()
df = matches_to_dataframe(matches)
model_df = reshape_for_model(df)

model = fit_model(model_df)

home_team = input("Home Team: (Proper, exact name)")
away_team = input("Away Team: (Proper, exact name)")

home_xg, away_xg = predict_expected_goals(home_team, away_team, model)
home_win, draw, away_win = match_outcome_probabilities(home_xg, away_xg)

print(f"{home_team} vs {away_team}")
print(f"Expected goals — {home_team}: {home_xg:.2f}, {away_team}: {away_xg:.2f}")
print(f"Home win: {home_win:.1%}, Draw: {draw:.1%}, Away win: {away_win:.1%}")