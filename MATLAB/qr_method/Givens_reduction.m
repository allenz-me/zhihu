function G = Givens_reduction(x, i, j)
% 利用 Givens 变换将 x 的第 j 个位置变为 0
% 返回初等旋转变换 G(i, j), 使得G*x 的第 j 个位置为 0
% 总的时间复杂度是 O(1)

n = length(x);
G = eye(n);
t = sqrt(x(i) ^ 2 + x(j) ^ 2);
G(i, i) = x(i) / t;
G(i, j) = x(j) / t;
G(j, j) = G(i, i);
G(j, i) = - G(i, j);
end