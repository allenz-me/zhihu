function H = Householder_reduction(x)
% 对于一个向量 x，求出一个Householder矩阵，使得 Hx = ke1，k < 0

k = norm(x);  % 向量 x 的模长
n = length(x);
e1 = zeros(n, 1);
e1(1) = 1;
w = x - k * e1;

H = eye(n) - 2 * (w * w') / (norm(w) ^ 2);

end