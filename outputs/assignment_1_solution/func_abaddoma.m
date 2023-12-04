function dy = func_abaddoma(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 90 * y(2) - 140 * y(1) + 9 + 3 * exp(-t)) / 10;
end