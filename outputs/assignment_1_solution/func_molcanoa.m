function dy = func_molcanoa(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 13 * y(2) - 36 * y(1) + 6 + 1 * exp(-t)) / 1;
end