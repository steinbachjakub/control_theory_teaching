function dy = func_methensr(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 26 * y(2) - 84 * y(1) + 11 + 7 * exp(-t)) / 2;
end