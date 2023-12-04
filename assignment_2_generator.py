import random

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
TEMPLATE_ASSIGNMENT = ENVIRONMENT.get_template("template_ass2.txt")
OUTPUT_FOLDER = Path("outputs", "assignment_2").absolute()
PARAMETERS_FILE = Path("outputs", "parameters_assignment_2.csv")
PARAMETERS_FILE.unlink(missing_ok=True)
# Load the list of students
STUDENTS = pd.read_csv("students.csv")
# Additional parameters
IMAGES = list(Path("templates", "images").glob("*.png"))
random.shuffle(IMAGES)
while len(IMAGES) < STUDENTS.shape[0]:
    IMAGES += IMAGES
# Generate specific assignment for each student
for index, (name, surname, email) in enumerate(zip(STUDENTS["First name"], STUDENTS["Surname"], STUDENTS["Email address"])):
    # if index == 2:
    #     break
    # Assignment
    ## Task 1
    t1_freq = random.randint(1, 11)
    possible_stability = ["has undamped oscillations", "has damped oscillations"]
    t1_stab = possible_stability[np.random.randint(0, 2)]

    ## Task 2
    t2_img = IMAGES[index].name

    ## Task 3
    t3_trans_params = [np.random.randint(11, 20)/10] + list(np.random.randint(1, 20, 2))

    ## Task 4 & 5
    p, a, b = 0.75 + np.random.randint(0, 10, 3) / 10
    t45_trans = [2*a + p, (a ** 2 + b ** 2) * 2 * a * p, p * (a ** 2 + b ** 2)]
    # Generate context based on the randomly generated tasks
    context = {
            "name": name + " " + surname,
            "t1": [t1_freq, t1_stab],
            "t2": t2_img,
            "t3": t3_trans_params,
            "t4": list(f"{x:.2f}" for x in t45_trans),
            }
    assignment_filename = Path("tex_files", f"{email.split('@')[0]}.tex")
    with open(assignment_filename, mode="w", encoding="utf-8") as results:
        results.write(TEMPLATE_ASSIGNMENT.render(context))
        print(f"... wrote {assignment_filename}")

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
