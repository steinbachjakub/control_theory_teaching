function dy = func_floriacl(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 28 * y(2) - 96 * y(1) + 10 + 3 * exp(-t)) / 2;
end