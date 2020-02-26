function [U, H] = Upper_Heisenberg(A)
% 使用 Householder 变换将矩阵 A 化为上海森伯格矩阵
% H 是上海森伯格矩阵，U 是初等反射矩阵的乘积，U'AU = H，初始矩阵 A 正交相似于上海森伯格矩阵 H
[n, ~] = size(A);
U = eye(n);
for i = 2 : n - 1
    x = A(i:end, i-1);
    R = Householder_reduction(x);
    T = eye(n);
    T(i:end, i:end) = R;
    A = T * A * T;
    U = T * U;
end
U = U';
H = A;
end