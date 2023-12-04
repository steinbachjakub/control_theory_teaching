function dy = func_bekaertm(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 100 * y(2) - 240 * y(1) + 10 + 4 * exp(-t)) / 10;
end