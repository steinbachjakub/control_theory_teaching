function dy = func_guerrerm(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 56 * y(2) - 192 * y(1) + 7 + 14 * exp(-t)) / 4;
end