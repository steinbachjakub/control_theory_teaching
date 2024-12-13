import numpy as np
import control as ct
from scipy.optimize import dual_annealing

np.random.seed(0)
not_found = True
while not_found:
    A = np.random.randint(-5, 5, size=(4, 4)).astype(np.float64)
    B = np.random.randint(-1, 1, size=(4, 1)).astype(np.float64)
    C = np.random.randint(-1, 1, size=(1, 4)).astype(np.float64)
    if np.any(A) and np.any(B) and np.any(C):
        rank_ctrb = np.linalg.matrix_rank(ct.ctrb(A, B))

        rank_obsv = np.linalg.matrix_rank(ct.obsv(A, C))
        if (rank_obsv == 4) and (rank_ctrb == 4):
            not_found = False

A = np.matrix("[4, 4, -2, 1;-3,-4,3, 3;1,-2,2,3;4, -1,  -1, -1]")
B = np.matrix("[-1; -1; 0; 0]")
C = np.matrix("[0, 0, 0, -1]")

v = np.array([[0, 0, 0, 1]]) @ np.linalg.inv(ct.ctrb(A, B))
T = np.reshape([v @ np.linalg.matrix_power(A, i) for i in range(4)], (4, 4))

ctrb_A = T @ A @ np.linalg.inv(T)
ctrb_B = T @ B
ctrb_C = C @ np.linalg.inv(T)
print(ctrb_A)
print(ctrb_B)
print(ctrb_C)
new_ctrb = ct.ctrb(ctrb_A, ctrb_B)
coeff = np.polynomial.polynomial.polyfromroots([-4 + 5j, -4 - 5j, -8, -10])
print(coeff)
desired_poly = coeff[0] * np.eye(4) + coeff[1] * ctrb_A + coeff[2] * ctrb_A @ ctrb_A + coeff[3] * ctrb_A @ ctrb_A @ ctrb_A + coeff[4]* ctrb_A @ ctrb_A @ ctrb_A @ ctrb_A
K = np.array([[0, 0, 0, 1]]) @ np.linalg.inv(new_ctrb) @ desired_poly
print(f"K: {K}")
dual_A = np.transpose(ctrb_A)
dual_B = np.transpose(ctrb_C)
dual_C = np.transpose(ctrb_B)
coeff = np.polynomial.polynomial.polyfromroots([-40, -39, -33, -33])
desired_obsv_poly = coeff[0] * np.eye(4) + coeff[1] * dual_A + coeff[2] * dual_A @ dual_A + coeff[3] * dual_A @ dual_A @ dual_A + coeff[4]* dual_A @ dual_A @ dual_A @ dual_A
dual_ctrb = ct.ctrb(dual_A, dual_B)
L = np.array([[0, 0, 0, 1]]) @ np.linalg.inv(dual_ctrb) @ desired_obsv_poly
sys = ct.ss(ctrb_A-ctrb_B @ K, ctrb_B, ctrb_C, 0)
print(f"L: {L}")
print(1 / ct.dcgain(sys))