function dy = func_stampoui(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 32 * y(2) - 48 * y(1) + 8 + 13 * exp(-t)) / 4;
end