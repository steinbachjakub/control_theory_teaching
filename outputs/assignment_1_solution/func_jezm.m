function dy = func_jezm(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 170 * y(2) - 720 * y(1) + 9 + 6 * exp(-t)) / 10;
end