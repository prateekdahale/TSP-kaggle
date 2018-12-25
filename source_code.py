import pandas as pd
from utils import calculate_score

file = "input/solution.csv"
cities_data = pd.read_csv("../travelling_salesman/cities.csv")


def reading_solution(filename):
    return pd.read_csv(filename)

solution = reading_solution(file)

print(calculate_score(cities_data,solution['Path']))