function dy = func_amaxopos(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 28 * y(2) - 90 * y(1) + 4 + 10 * exp(-t)) / 2;
end