function dy = func_chaparre(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 24 * y(2) - 72 * y(1) + 11 + 7 * exp(-t)) / 2;
end