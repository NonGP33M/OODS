'''

Chapter : 10 - item : 5 - กล่องสินค้า

มีสินค้าอยู่ n ชิ้น โดยชิ้นที่ i (0 <= i < n) มีน้ำหนัก Wi กิโลกรัม  นำสินค้าบรรจุใส่กล่องไม่เกิน k ใบ โดยมีเงื่อนไขว่า
1. สิ่งของต้องมีน้ำหนักรวมกันไม่เกินน้ำหนักมากสุดที่กล่องรับไหว
2. หากสิ่งของชิ้นที่ a และชิ้นที่ b อยู่ในกล่องเดียวกัน (a <= b) สิ่งของทุกชิ้นที่อยู่ระหว่างสองชิ้นนี้ (ทุกชิ้นที่ i ที่ a < i < b) จะต้องอยู่ในกล่องนี้ด้วย (นั่นคือสิ่งที่ของในกล่องเดียวกันจะต้องเป็นสิ่งของที่ตำแหน่งติดกัน)

ถ้าทุกกล่องสามารถรับน้ำหนักได้เท่ากัน จงหาว่าเราสามารถใช้กล่องที่รับน้ำหนักได้น้อยสุดเท่าใด โดยที่ยังบรรจุของตามเงื่อนไขได้ และใช้กล่องครบทุกใบ

อธิบาย Input
แบ่ง Data เป็น 2 ชุดด้วย /
    -   ด้านซ้ายหมายถึง สินค้า n ชิ้น และแต่ละชิ้นมีน้ำหนัก W กิโลกรัม
    -   ด้านขวาหมายถึง จำนวนกล่อง k ใบ

คำใบ้  Optimization Problem


อธิบาย Test Case #1

มีสินค้าอยู่ 5 ชิ้น โดยมีน้ำหนักเป็น 6 2 4 3 7 ตามลำดับ และมีกล่องจำนวน 3 ใบ   และน้ำหนักที่น้อยที่สุดที่สามารถใส่สินค้าได้ครบทุกชิ้น และใส่ลงกล่องได้ทุกใบคือ 8 กิโลกรัม โดยในกล่องที่ 1 จะใส่สินค้า 2 ชิ้นที่มีน้ำหนัก 6 และ 2   กล่องใบที่ 2 จะใส่สินค้า 2 ชิ้นที่มำน้ำหนัก 4 และ 3  และกล่องใบที่ 3 จะใส่สินค้า 1 ชิ้นที่มีน้ำหนัก 7

อธิบาย Test Case #2

มีสินค้าอยู่ 10 ชิ้น โดยมีน้ำหนักเป็น 8 7 2 5 1 10 9 2 3 5 ตามลำดับ และมีกล่องจำนวน 5 ใบ   และน้ำหนักที่น้อยที่สุดที่สามารถใส่สินค้าได้ครบทุกชิ้น และใส่ลงกล่องได้ทุกใบคือ 14 กิโลกรัม โดยในกล่องที่ 1 จะใส่สินค้า 1 ชิ้นที่มีน้ำหนัก 8   กล่องใบที่ 2 จะใส่สินค้า 3 ชิ้นที่มีน้ำหนัก 7 2 และ 5   กล่องใบที่ 3 จะใส่สินค้า 2 ชิ้นที่มีน้ำหนัก 1 และ 10   กล่องใบที่ 4 จะใส่สินค้า 3 ชิ้นที่มีน้ำหนัก 9 2 และ 3    และกล่องใบที่ 5 จะใส่สินค้า 1 ชิ้นที่มีน้ำหนัก 5

'''

inp1,n = input('Enter Input : ').split('/')
inp1 = [int(e) for e in inp1.split()]
data=inp1.copy()
inp1.sort(reverse=True)
n=int(n)
l=inp1[0]
r=100
while(l!=r):
    mid=int((l+r)/2)
    box=[]
    alrShift=False
    for i in range(n):
        box.append(mid)
    j=0
    for i in data:
        while( j < n and box[j]<i):
           j+=1
        if j >= n:
            l=mid+1
            alrShift=True
            break
        box[j]-=i
    if not alrShift:
        r=mid

print('Minimum weigth for {0} box(es) = {1}'.format(n,l))