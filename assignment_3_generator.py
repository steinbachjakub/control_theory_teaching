import random

import numpy as np
from numpy import random as rnd
import pandas as pd
import control as ct
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import subprocess
import os


# Set up latex environment
ENVIRONMENT = Environment(loader=FileSystemLoader("./templates/"))
TEMPLATE_ASSIGNMENT = ENVIRONMENT.get_template("template_ass3.txt")
OUTPUT_FOLDER = Path("outputs", "assignment_3").absolute()
PARAMETERS_FILE = Path("outputs", "parameters_assignment_3.csv")
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
    a = [random.randint(1,10) for _ in range(3)]
    b = [random.randint(1, 5) for _ in range(3)]

    ## Task 2

    not_found = True
    while not_found:
        A = np.random.randint(-5, 5, size=(4, 4))
        B = np.random.randint(-1, 1, size=(4, 1))
        C = np.random.randint(-1, 1, size=(1, 4))
        if np.any(A) and np.any(B) and np.any(C):
            rank_ctrb = np.linalg.matrix_rank(ct.ctrb(A, B))

            rank_obsv = np.linalg.matrix_rank(ct.obsv(A, C))
            if (rank_obsv == 4) and (rank_ctrb == 4):
                not_found = False

    a_lines = str(A).replace("[", "").replace("]", "").splitlines()
    a_matrix = [r"\begin{bmatrix}"]
    a_matrix += ["  " + " & ".join(l.split()) + r"\\" for l in a_lines]
    a_matrix += [r"\end{bmatrix}"]
    b_line = str(b).replace("[", "").replace("]", "")
    b_matrix = [r"\begin{bmatrix}"]
    b_matrix += [" " + " \\ ".join(b_line.split(","))]
    b_matrix += [r"\end{bmatrix}"]
    c_lines = str(C).replace("[", "").replace("]", "").splitlines()
    c_matrix = [r"\begin{bmatrix}"]
    c_matrix += ["  " + " & ".join(l.split()) + r"\\" for l in c_lines]
    c_matrix += [r"\end{bmatrix}"]

    observer = [random.randint(-40, -30) for _ in range(4)]
    observer.sort()
    acl = random.sample([x + 1 for x in range(10) ], 4)
    acl.sort()
    # Generate context based on the randomly generated tasks
    context = {
            "name": name + " " + surname,
            "a": [value if value > 1 else "" for value in a],
            "b": [value if value > 1 else "" for value in b],
            "A_matrix": "\n".join(a_matrix),
            "B_matrix": "\n".join(b_matrix).replace(",", ""),
            "C_matrix": "\n".join(c_matrix),
            "observer": observer,
            "acl": acl
            }
    assignment_filename = Path("tex_files", f"{email.split('@')[0]}.tex")
    with open(assignment_filename, mode="w", encoding="utf-8") as results:
        results.write(TEMPLATE_ASSIGNMENT.render(context))
        print(f"... wrote {assignment_filename}")

    subprocess.run(["pdflatex", f"--output-directory={OUTPUT_FOLDER}", assignment_filename, "-quiet"])

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
