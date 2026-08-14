import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy.stats import poisson


def fit_model(model_df):
    return smf.glm(
        formula="goals ~ team + opponent + is_home",
        data=model_df,
        family=sm.families.Poisson()
    ).fit()


def predict_expected_goals(home_team, away_team, model):
    home_row = pd.DataFrame({"team": [home_team], "opponent": [away_team], "is_home": [1]})
    away_row = pd.DataFrame({"team": [away_team], "opponent": [home_team], "is_home": [0]})

    home_lambda = model.predict(home_row).iloc[0]
    away_lambda = model.predict(away_row).iloc[0]
    return home_lambda, away_lambda


def match_outcome_probabilities(home_xg, away_xg, max_goals=10):
    home_probs = [poisson.pmf(i, home_xg) for i in range(max_goals + 1)]
    away_probs = [poisson.pmf(j, away_xg) for j in range(max_goals + 1)]

    score_matrix = np.outer(home_probs, away_probs)

    home_win = np.sum(np.tril(score_matrix, -1))
    draw = np.sum(np.diag(score_matrix))
    away_win = np.sum(np.triu(score_matrix, 1))
    return home_win, draw, away_win