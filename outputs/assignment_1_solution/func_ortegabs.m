function dy = func_ortegabs(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 32 * y(2) - 126 * y(1) + 14 + 11 * exp(-t)) / 2;
end