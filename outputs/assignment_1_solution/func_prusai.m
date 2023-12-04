function dy = func_prusai(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 40 * y(2) - 64 * y(1) + 3 + 9 * exp(-t)) / 4;
end