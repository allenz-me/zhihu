function [U, H] = Upper_Heisenberg(A)
% ʹ�� Householder �任������ A ��Ϊ�Ϻ�ɭ�������
% H ���Ϻ�ɭ�������U �ǳ��ȷ������ĳ˻���U'AU = H����ʼ���� A �����������Ϻ�ɭ������� H
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