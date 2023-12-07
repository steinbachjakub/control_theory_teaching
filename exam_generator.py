"""
Exam from Control Theory generator.
Authors: Jakub Steinbach, Jan Vrba
"""
from pathlib import Path
import subprocess
import os
from datetime import date
import random
from math import copysign
import numpy as np
from numpy import random as rnd
import pandas as pd
from jinja2 import Environment, FileSystemLoader
from sympy import symbols, Function, dsolve



# Get values for head (exam year, exam date, number of students)
EXAM_DATES = ["19-12-2023", "04-01-2024", "11-01-2024", "25-01-2024", "01-02-2024", "08-02-2024"]
EXAM_YEAR = date.today().strftime("%Y")
EXAM_DATE = date.today().strftime("%d %B %Y")

# Set up latex environment
ENVIRONMENT = Environment(loader=FileSystemLoader("./templates/exam/"))
TEMPLATE_HEAD = ENVIRONMENT.get_template("exam_head.txt")
OUTPUT_FOLDER = Path("outputs", f"exams_{date.today().strftime('%Y')}")

for idx, exam_date in enumerate(EXAM_DATES):
    assignment_filename = Path("tex_files", f"assigment{idx + 1}.tex")
    if idx == 1:
        break
    # Generate head
    head_filename = Path("tex_files", f"head_exam_{idx + 1}.tex")
    context = {
        "exam_date": exam_date,
        "exam_idx": idx + 1
    }
    # Generate tex file with head
    with open(head_filename, mode="w", encoding="utf-8") as exam_tex_file:
        exam_tex_file.write(TEMPLATE_HEAD.render(context))
        print(f"... wrote {head_filename}")

    # Generate first question which is
    # 1. ODE to transfer function
    # 2. step response y(t) from transfer function
    if random.choice([1, 2]) == 1:
        TEMPLATE_Q1 = ENVIRONMENT.get_template("question1_variant1.txt")
        tf_zero = random.choice([x for x in range(5, 11)])
        denumerator_coeffs = [random.choice([i for i in range(-3,3)]), random.choice([i for i in range(-4,4)])]
        denumerator = "s^2"
        if denumerator_coeffs[0] != 0:
            if denumerator_coeffs[0] == 1:
                denumerator += "+s"
            else:
                denumerator += f"{denumerator_coeffs[0]:+}s"
        if denumerator_coeffs[1] != 0:
            denumerator += f"{denumerator_coeffs[1]:+}"

        context = {
            "zero": tf_zero,
            "denumerator": denumerator
        }
    else:
        TEMPLATE_Q1 = ENVIRONMENT.get_template("question1_variant2.txt")
    q1_filename = Path("tex_files", f"q1_exam_{idx + 1}.tex")
    with open(q1_filename, mode="w", encoding="utf-8") as exam_tex_file:
        exam_tex_file.write(TEMPLATE_Q1.render(context))
        print(f"... wrote {head_filename}")


    # Join text files together to final assignment tex file
    tex_files = Path(f"tex_files")
    with open(assignment_filename, "w") as assignment_text:
        for tex_file in tex_files.glob(f"*_{idx + 1}.tex"):
            with open(tex_file, "r") as source_tex:
                assignment_text.write(source_tex.read())
    # Compile PDF
    subprocess.run(['pdflatex', f'--output-directory={OUTPUT_FOLDER}',
                    assignment_filename, "-quiet"], check=True)

# Delete all auxiliary files
files_to_delete = list(OUTPUT_FOLDER.glob("*.log")) + list(OUTPUT_FOLDER.glob("*.aux"))
for file in files_to_delete:
    file.unlink()

# TEMPLATE_ASSIGNMENT = ENVIRONMENT.get_template("template_ass1.txt")
# TEMPLATE_SOLUTION = ENVIRONMENT.get_template("template_ass1_sol.txt")
# TEMPLATE_SOLUTION_FUNCTION = ENVIRONMENT.get_template("template_ass1_func.txt")
# OUTPUT_FOLDER = Path("outputs", "assignment_1").absolute()
# PARAMETERS_FILE = Path("outputs", "parameters_assignment_1.csv")
# PARAMETERS_FILE.unlink(missing_ok=True)







# # Load the list of students
# STUDENTS = pd.read_csv("students.csv")
# # Generate specific assignment for each student
# for index, (name, surname, email) in enumerate(zip(STUDENTS["First name"], STUDENTS["Surname"], STUDENTS["Email address"])):
#     # if index == 2:
#     #     break
#     # Assignment
#     ## Task 1
#     ### Left-side-parameters
#     ode_a = rnd.choice([1, 2, 4, 10])
#     ode_b, ode_c = rnd.randint(2, 11, 2)
#     ### Right-side functions
#     right_side_coeff = rnd.randint(1, 16, 2)
#     right_side_function = f"{right_side_coeff[0]} + {right_side_coeff[1] if right_side_coeff[1] != 1 else ''}" + "e^{-t}"
#
#     ### Initial Conditions
#     initial_conditions = list(rnd.randint(1, 10, 2))
#
#     # Task 3
#     # Transfer function pole polynomial parameters
#     hsp_a = rnd.choice([1, 2, 3, 10])
#     hsp_b, hsp_c = rnd.randint(2, 11, 2)
#
#     # Generate context based on the randomly generated tasks
#     context = {
#             "name": name + " " + surname,
#             "ode_params": [ode_a if ode_a != 1 else "", ode_a * (ode_b + ode_c), ode_a * ode_b * ode_c],
#             "ode_params_sol": [ode_a, ode_a * (ode_b + ode_c), ode_a * ode_b * ode_c],
#             "ode_right_side": right_side_function,
#             "ode_right_side_sol": right_side_coeff,
#             "ode_initial_conditions": initial_conditions,
#             "hs_bottom": [hsp_a if hsp_a != 1 else "", hsp_a * (hsp_b + hsp_c), hsp_a * (hsp_b * hsp_c) ** 2],
#             "hs_bottom_sol": [hsp_a, hsp_a * (hsp_b + hsp_c), hsp_a * (hsp_b * hsp_c) ** 2],
#             "func_name": f"func_{email.split('@')[0]}"
#             }
#     assignment_filename = Path("tex_files", f"{email.split('@')[0]}.tex")
#     with open(assignment_filename, mode="w", encoding="utf-8") as results:
#         results.write(TEMPLATE_ASSIGNMENT.render(context))
#         print(f"... wrote {assignment_filename}")
#
#     solution_filename = Path("outputs", "assignment_1_solution", f"{email.split('@')[0]}_sol.m")
#     with open(solution_filename, mode="w", encoding="utf-8") as results:
#         results.write(TEMPLATE_SOLUTION.render(context))
#         print(f"... wrote {solution_filename}")
#
#     solution_function_filename = Path("outputs", "assignment_1_solution", f"func_{email.split('@')[0]}.m")
#     with open(solution_function_filename, mode="w", encoding="utf-8") as results:
#         results.write(TEMPLATE_SOLUTION_FUNCTION.render(context))
#         print(f"... wrote {solution_function_filename}")
#
#     subprocess.run(['pdflatex', f'--output-directory={OUTPUT_FOLDER}', assignment_filename, "-quiet"])
#
#     if PARAMETERS_FILE.exists():
#         with open(PARAMETERS_FILE, "a", encoding="utf-8") as f:
#             f.write(str(context))
#     else:
#         with open(PARAMETERS_FILE, "w", encoding="utf-8") as f:
#             f.write(str(context))
#
# # Delete all auxiliary files
# files_to_delete = list(OUTPUT_FOLDER.glob("*.log")) + list(OUTPUT_FOLDER.glob("*.aux"))
# for file in files_to_delete:
#     file.unlink()
