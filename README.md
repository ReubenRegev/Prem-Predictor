# Premier League Match Predictor

A  model that predicts Premier League match outcomes using Poisson regression, 
using real match data pulled from the football-data.org API.

## How it works

Each team is assigned an attack strength and defense strength rating, fit simultaneously 
via a Poisson Generalized Linear Model (GLM) on the 2024–25 season's 380 matches. Given any 
matchup, the model computes expected goals for each side, then generates a full distribution 
of every realistic scoreline to produce win/draw/loss probabilities 
— rather than a single predicted score.

**Example:**
