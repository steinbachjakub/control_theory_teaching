%% Task 1
% Clear all previous output
clear all, close all, clc;
% Declaration of the symbolic variable
% Declaration of the symbolic variable
syms y(t);
% Declaration of the first and second derivatives
dy = diff(y); d2y = diff(y, 2);
% Creating the differential equation based on the assignment
ode = 2 * d2y + 32 * dy + 126 * y == 14 + 11 * exp(-t);
% Defining the initial conditions
cond = [y(0) == 6, dy(0) == 6];
% Solution using the analytical solver
sol = dsolve(ode, cond);
pretty(simplify(expand(sol)))
% Solution using the numerical solver
tspan = 0:0.1:20;
y0 = [6; 2];
[tnum, ynum] = ode45(@func_ortegabs, tspan, y0);
% Plotting the analytical and numerical solution
fplot(sol), xlim([0 20]), ylim([0 20]);
hold on
scatter(tnum, ynum(:, 1), 10, "red", Marker="x")
hold off
title(["Numerical and analytical solution of "; ...
      "$ 2 y'' + 32 y' + 126 y = 14 + 11e^{-t}$"], Interpreter="latex")
legend(["analytical solution", "numerical solution"])
xlabel("$t[\mathrm{s}]$", Interpreter="latex")
ylabel("$y[-]$", Interpreter="latex")
% Laplace transform of the solution to check whether it corresponds with
% the manual computation
pretty(laplace(sol))

%% Task 2
% In the time domain
limit(sol, t, inf)
% In the complex domain
% We need to declare the complex variable s even though Laplace returns it
syms s;
limit(laplace(sol) * s, s, 0)

%% Task 3
% Clear all previous output
clear all, close all, clc;
syms C;
% A(s) = 2s^2 + 24s + C
% Hurwitz criterion
H1 = 2;
H2 = det([24 0; 2 C])
solve(H2 > 0, C, 'ReturnConditions', true)

%% Task 4
% Clear all previous output
clear all, close all, clc;
s = tf("s");
Hs = 1 / (2 * s^2 + 24 * s + 2592);
stepinfo(Hs)
impulse(Hs)
figure;
step(Hs)