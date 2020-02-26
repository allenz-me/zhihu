function [Q, R ] = Householder_QR(A)
% �Կ������Aʹ��Householder�任����QR�ֽ�
% Q ����������R �ǶԽ�ԪΪ���������Ǿ�����֤������ QR �ֽ���Ψһ��
[n, ~] = size(A);
Q = eye(n);
for i = 1 : n - 1
    x = A(i:end,i);
    H = Householder_reduction(x);
    T = eye(n);    % ��ʱ����
    T(i:end, i:end) = H;
    Q = T * Q;
    A = T * A;
end
Q = Q';
R = A;
end