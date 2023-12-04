function dy = func_planabad(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 8 * y(2) - 16 * y(1) + 7 + 4 * exp(-t)) / 1;
end