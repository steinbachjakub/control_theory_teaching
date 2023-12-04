function dy = func_josifkoh(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 36 * y(2) - 80 * y(1) + 4 + 9 * exp(-t)) / 4;
end