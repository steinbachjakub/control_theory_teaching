function dy = func_vereersl(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 11 * y(2) - 24 * y(1) + 5 + 14 * exp(-t)) / 1;
end