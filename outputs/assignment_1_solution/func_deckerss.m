function dy = func_deckerss(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 48 * y(2) - 108 * y(1) + 3 + 4 * exp(-t)) / 4;
end