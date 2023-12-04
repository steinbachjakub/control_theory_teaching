function dy = func_cilerj(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 56 * y(2) - 160 * y(1) + 12 + 1 * exp(-t)) / 4;
end