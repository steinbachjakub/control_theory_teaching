function dy = func_blieckf(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 100 * y(2) - 250 * y(1) + 10 + 15 * exp(-t)) / 10;
end