import pandas as pd
import json
from sentencing_simulator.core.orchestrator import run_simulation

def main():
    columns = ["id", "name", "sex", "dob", "age", "race", "juv_fel_count", "juv_misd_count", "juv_other_count", "priors_count",
               "c_offense_date", "c_arrest_date", "c_charge_degree", "c_charge_desc", "vr_charge_degree", "vr_offense_date", "vr_charge_desc"]

    df = pd.read_csv("data/compas-scores-two-years.csv", usecols=columns)
    
    cases = [row.to_dict() for _, row in df.head(5).iterrows()]

    for case in cases:
        print(json.dumps(case, indent=2))
        run_simulation(case)

if __name__ == "__main__":
    main()