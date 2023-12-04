function dy = func_hanzlj(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 120 * y(2) - 350 * y(1) + 8 + 2 * exp(-t)) / 10;
end