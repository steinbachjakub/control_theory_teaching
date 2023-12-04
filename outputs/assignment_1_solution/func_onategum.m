function dy = func_onategum(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 18 * y(2) - 40 * y(1) + 3 + 13 * exp(-t)) / 2;
end