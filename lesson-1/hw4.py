#4. ������������ ������ ����� ������������� �����. ������� ����� ������� ����� � �����. ��� ������� ����������� ���� while � �������������� ��������.

number = int(input("������� ����� ������������� �����: "))
number,max_digit=number//10,number%10

while number>=1:
    digit=number%10
    number=number//10
    if digit>max_digit: max_digit=digit

print(f"������������ ����� {max_digit}")