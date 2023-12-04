function dy = func_yefimakk(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 6 * y(2) - 8 * y(1) + 10 + 9 * exp(-t)) / 1;
end