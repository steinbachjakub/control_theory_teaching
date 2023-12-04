function dy = func_desmetj(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 20 * y(2) - 100 * y(1) + 3 + 6 * exp(-t)) / 1;
end