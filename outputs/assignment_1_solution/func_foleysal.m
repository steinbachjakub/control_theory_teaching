function dy = func_foleysal(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 28 * y(2) - 90 * y(1) + 14 + 8 * exp(-t)) / 2;
end