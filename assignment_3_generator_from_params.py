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
# Load the list of students
STUDENTS = pd.read_csv("students.csv")
# Additional parameters
with open(PARAMETERS_FILE, "r", encoding="utf-8") as f:
    content = eval("[" + f.read().replace("}{", "},{") + "]")

for index, (name, surname, email, context) in enumerate(zip(STUDENTS["First name"], STUDENTS["Surname"], STUDENTS["Email address"], content)):
 
    assignment_filename = Path("tex_files", f"{email.split('@')[0]}.tex")
    with open(assignment_filename, mode="w", encoding="utf-8") as results:
        results.write(TEMPLATE_ASSIGNMENT.render(context))
        print(f"... wrote {assignment_filename}")

    subprocess.run(["pdflatex", f"--output-directory={OUTPUT_FOLDER}", assignment_filename, "-quiet"])

# Delete all auxiliary files
files_to_delete = list(OUTPUT_FOLDER.glob("*.log")) + list(OUTPUT_FOLDER.glob("*.aux"))
for file in files_to_delete:
    file.unlink()
