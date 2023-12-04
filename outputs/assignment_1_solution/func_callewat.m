function dy = func_callewat(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 6 * y(2) - 8 * y(1) + 5 + 5 * exp(-t)) / 1;
end