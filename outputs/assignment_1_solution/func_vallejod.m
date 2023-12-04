function dy = func_vallejod(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 70 * y(2) - 120 * y(1) + 4 + 3 * exp(-t)) / 10;
end