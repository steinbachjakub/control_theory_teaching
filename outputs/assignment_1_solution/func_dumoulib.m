function dy = func_dumoulib(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 160 * y(2) - 630 * y(1) + 15 + 10 * exp(-t)) / 10;
end