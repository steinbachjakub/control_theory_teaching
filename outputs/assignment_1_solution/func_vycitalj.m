function dy = func_vycitalj(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 20 * y(2) - 50 * y(1) + 3 + 13 * exp(-t)) / 2;
end