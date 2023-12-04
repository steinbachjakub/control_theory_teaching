function dy = func_novotncu(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 19 * y(2) - 90 * y(1) + 1 + 2 * exp(-t)) / 1;
end