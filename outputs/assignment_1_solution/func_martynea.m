function dy = func_martynea(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 110 * y(2) - 180 * y(1) + 8 + 9 * exp(-t)) / 10;
end