function dy = func_tiesenf(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 9 * y(2) - 20 * y(1) + 1 + 10 * exp(-t)) / 1;
end