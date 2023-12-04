function dy = func_haenenn(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 48 * y(2) - 108 * y(1) + 10 + 15 * exp(-t)) / 4;
end