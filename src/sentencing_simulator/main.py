import pandas as pd
from sentencing_simulator.core.orchestrator import run_simulation

def main():
    df = pd.read_csv("data/cleaned/cleaned_compas.csv")

    results = []
    for _, row in df.iterrows():
        case = row.to_dict()
        results.append(run_simulation(case))

    print(results)