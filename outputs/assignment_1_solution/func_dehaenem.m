function dy = func_dehaenem(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 48 * y(2) - 140 * y(1) + 2 + 11 * exp(-t)) / 4;
end