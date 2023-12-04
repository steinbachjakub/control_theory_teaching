function dy = func_hospodal(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 150 * y(2) - 500 * y(1) + 2 + 7 * exp(-t)) / 10;
end