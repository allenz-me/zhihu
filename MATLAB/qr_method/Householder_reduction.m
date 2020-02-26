function H = Householder_reduction(x)
% ����һ������ x�����һ��Householder����ʹ�� Hx = ke1��k < 0

k = norm(x);  % ���� x ��ģ��
n = length(x);
e1 = zeros(n, 1);
e1(1) = 1;
w = x - k * e1;

H = eye(n) - 2 * (w * w') / (norm(w) ^ 2);

end