function dy = func_mammai(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 64 * y(2) - 240 * y(1) + 15 + 10 * exp(-t)) / 4;
end