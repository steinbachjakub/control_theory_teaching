function dy = func_willenj(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 11 * y(2) - 30 * y(1) + 14 + 13 * exp(-t)) / 1;
end