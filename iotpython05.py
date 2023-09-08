#หาพื้นที่สี่เหลี่ยมและสามเหลื่ยม โดยรับกว้าง ยาว/ฐาน สูง หาแป้นพิมพ์ และแสดงผลทางหน้าจอ
#feature การทำงานอะไรบ้าง
#1. รับค่า กว้างยาว 2. รับค่า ฐาน/สูง 
#3.คำนวณ พท. สี่เหลื่ยมและแสดง พท. สี่เหลื่ยม 4. คำนวณ พท. สามเหลื่ยม และแสดง พท. สามเหลื่ยม
def inputWitdhlong( ) : 
    wi = float(input('กว้าง'))
    lo = float(input('ยาว'))
    return wi, lo

def inputBasehigh( ) :
    ba = float(input('ฐาน : '))
    hi = float(input('สูง : '))
    return ba, hi

def calAndShowAreaSquare( wi, lo ) :
    area = wi * lo
    print(f'สี่เหลื่ยมกว้าง {wi} ยาว {lo} มีพื้นที่ {area}')

def calAndShowAreaSquare( ba, hi ) :
    area = ba * hi /2
    print(f'สามเหลื่ยมฐาน {ba} ยาว {hi} มีพื้นที่ {area}')

wi, lo = inputWitdhlong( )
calAndShowAreaSquare(wi, lo)
print('...........................')
ba, hi = inputBasehigh( )
calAndShowAreaSquare(ba, hi)