function dy = func_kavkad(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 28 * y(2) - 48 * y(1) + 10 + 4 * exp(-t)) / 4;
end