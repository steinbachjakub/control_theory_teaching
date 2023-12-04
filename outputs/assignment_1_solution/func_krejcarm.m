function dy = func_krejcarm(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 9 * y(2) - 18 * y(1) + 7 + 2 * exp(-t)) / 1;
end