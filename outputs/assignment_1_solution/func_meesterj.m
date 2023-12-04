function dy = func_meesterj(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 32 * y(2) - 64 * y(1) + 12 + 15 * exp(-t)) / 4;
end