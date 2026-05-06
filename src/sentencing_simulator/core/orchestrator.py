from sentencing_simulator.agents import prosecutor, defendant, risk, fairness, judge
import os

def run_simulation(case):

    pros = prosecutor.run(case)
    defn = defendant.run(case)
    risk_out = risk.run(case)

    fairness_out = fairness.run({
        "case": case,
        "risk": risk_out
    })

    judge_input = {
        "case": case,
        "prosecutor": pros,
        "defendant": defn,
        "risk": risk_out,
        "fairness": fairness_out
    }

    verdict = judge.run(judge_input)

    return {
        "case": case,
        "prosecutor": pros,
        "defendant": defn,
        "risk": risk_out,
        "fairness": fairness_out,
        "judge": verdict
    }