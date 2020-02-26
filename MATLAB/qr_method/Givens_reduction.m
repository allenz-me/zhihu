function G = Givens_reduction(x, i, j)
% ���� Givens �任�� x �ĵ� j ��λ�ñ�Ϊ 0
% ���س�����ת�任 G(i, j), ʹ��G*x �ĵ� j ��λ��Ϊ 0
% �ܵ�ʱ�临�Ӷ��� O(1)

n = length(x);
G = eye(n);
t = sqrt(x(i) ^ 2 + x(j) ^ 2);
G(i, i) = x(i) / t;
G(i, j) = x(j) / t;
G(j, j) = G(i, i);
G(j, i) = - G(i, j);
end