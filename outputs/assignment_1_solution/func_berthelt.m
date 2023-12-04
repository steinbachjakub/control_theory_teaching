function dy = func_berthelt(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 11 * y(2) - 24 * y(1) + 3 + 5 * exp(-t)) / 1;
end