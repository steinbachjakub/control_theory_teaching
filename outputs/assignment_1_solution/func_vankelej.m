function dy = func_vankelej(t, y)
dy = zeros(2, 1);
dy(1) = y(2);
dy(2) = (- 68 * y(2) - 288 * y(1) + 8 + 13 * exp(-t)) / 4;
end