function dy = func_bonackj(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 16 * y(2) - 64 * y(1) + 9 + 13 * exp(-t)) / 1;
end