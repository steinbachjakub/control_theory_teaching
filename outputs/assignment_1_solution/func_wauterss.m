function dy = func_wauterss(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 7 * y(2) - 10 * y(1) + 11 + 6 * exp(-t)) / 1;
end