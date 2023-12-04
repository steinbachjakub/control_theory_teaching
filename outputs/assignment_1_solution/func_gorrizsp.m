function dy = func_gorrizsp(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 20 * y(2) - 48 * y(1) + 3 + 13 * exp(-t)) / 2;
end