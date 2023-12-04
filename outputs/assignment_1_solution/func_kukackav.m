function dy = func_kukackav(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 160 * y(2) - 600 * y(1) + 15 + 3 * exp(-t)) / 10;
end