import numpy as np
from numpy import random as rnd
import pandas as pd
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from sympy import symbols, Function, dsolve
import subprocess
import os

# Set up latex environment
ENVIRONMENT = Environment(loader=FileSystemLoader("./templates/"))
TEMPLATE_ASSIGNMENT = ENVIRONMENT.get_template("template_ass1.txt")
TEMPLATE_SOLUTION = ENVIRONMENT.get_template("template_ass1_sol.txt")
TEMPLATE_SOLUTION_FUNCTION = ENVIRONMENT.get_template("template_ass1_func.txt")
OUTPUT_FOLDER = Path("outputs", "assignment_1").absolute()
PARAMETERS_FILE = Path("outputs", "parameters_assignment_1.csv")
PARAMETERS_FILE.unlink(missing_ok=True)
# Load the list of students
STUDENTS = pd.read_csv("students.csv")
# Generate specific assignment for each student
for index, (name, surname, email) in enumerate(zip(STUDENTS["First name"], STUDENTS["Surname"], STUDENTS["Email address"])):
    # if index == 2:
    #     break
    # Assignment
    ## Task 1
    ### Left-side-parameters
    ode_a = rnd.choice([1, 2, 4, 10])
    ode_b, ode_c = rnd.randint(2, 11, 2)
    ### Right-side functions
    right_side_coeff = rnd.randint(1, 16, 2)
    right_side_function = f"{right_side_coeff[0]} + {right_side_coeff[1] if right_side_coeff[1] != 1 else ''}" + "e^{-t}"

    ### Initial Conditions
    initial_conditions = list(rnd.randint(1, 10, 2))

    # Task 3
    # Transfer function pole polynomial parameters
    hsp_a = rnd.choice([1, 2, 3, 10])
    hsp_b, hsp_c = rnd.randint(2, 11, 2)

    # Generate context based on the randomly generated tasks
    context = {
            "name": name + " " + surname,
            "ode_params": [ode_a if ode_a != 1 else "", ode_a * (ode_b + ode_c), ode_a * ode_b * ode_c],
            "ode_params_sol": [ode_a, ode_a * (ode_b + ode_c), ode_a * ode_b * ode_c],
            "ode_right_side": right_side_function,
            "ode_right_side_sol": right_side_coeff,
            "ode_initial_conditions": initial_conditions,
            "hs_bottom": [hsp_a if hsp_a != 1 else "", hsp_a * (hsp_b + hsp_c), hsp_a * (hsp_b * hsp_c) ** 2],
            "hs_bottom_sol": [hsp_a, hsp_a * (hsp_b + hsp_c), hsp_a * (hsp_b * hsp_c) ** 2],
            "func_name": f"func_{email.split('@')[0]}"
            }
    assignment_filename = Path("tex_files", f"{email.split('@')[0]}.tex")
    with open(assignment_filename, mode="w", encoding="utf-8") as results:
        results.write(TEMPLATE_ASSIGNMENT.render(context))
        print(f"... wrote {assignment_filename}")

    solution_filename = Path("outputs", "assignment_1_solution", f"{email.split('@')[0]}_sol.m")
    with open(solution_filename, mode="w", encoding="utf-8") as results:
        results.write(TEMPLATE_SOLUTION.render(context))
        print(f"... wrote {solution_filename}")

    solution_function_filename = Path("outputs", "assignment_1_solution", f"func_{email.split('@')[0]}.m")
    with open(solution_function_filename, mode="w", encoding="utf-8") as results:
        results.write(TEMPLATE_SOLUTION_FUNCTION.render(context))
        print(f"... wrote {solution_function_filename}")

    subprocess.run(['pdflatex', f'--output-directory={OUTPUT_FOLDER}', assignment_filename, "-quiet"])

    if PARAMETERS_FILE.exists():
        with open(PARAMETERS_FILE, "a", encoding="utf-8") as f:
            f.write(str(context))
    else:
        with open(PARAMETERS_FILE, "w", encoding="utf-8") as f:
            f.write(str(context))

# Delete all auxiliary files
files_to_delete = list(OUTPUT_FOLDER.glob("*.log")) + list(OUTPUT_FOLDER.glob("*.aux"))
for file in files_to_delete:
    file.unlink()
