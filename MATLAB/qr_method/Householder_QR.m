function [Q, R ] = Householder_QR(A)
% 对可逆矩阵A使用Householder变换进行QR分解
% Q 是正交矩阵，R 是对角元为正的上三角矩阵。易证这样的 QR 分解是唯一的
[n, ~] = size(A);
Q = eye(n);
for i = 1 : n - 1
    x = A(i:end,i);
    H = Householder_reduction(x);
    T = eye(n);    % 临时变量
    T(i:end, i:end) = H;
    Q = T * Q;
    A = T * A;
end
Q = Q';
R = A;
end