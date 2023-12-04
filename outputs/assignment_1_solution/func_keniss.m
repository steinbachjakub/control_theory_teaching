function dy = func_keniss(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 28 * y(2) - 90 * y(1) + 13 + 13 * exp(-t)) / 2;
end