function dy = func_tichyv(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 24 * y(2) - 64 * y(1) + 1 + 5 * exp(-t)) / 2;
end