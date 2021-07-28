from machine import Pin, I2C
from DFRobot_TCS3430 import DFRobot_TCS3430

I2C_SDA = 21
I2C_SCL = 22
i2c = I2C(1, scl=Pin(I2C_SCL), sda=Pin(I2C_SDA), freq=400000)
sensor = DFRobot_TCS3430(i2c)
ledsensor = Pin(18, Pin.OUT) #led on board

def getcolor():
    while (sensor.begin() == False ):
        print('Please check that the IIC device is properly connected')
    
    ledsensor.value(1)
    time.sleep(1)
    Z = sensor.get_z_data()
    X = sensor.get_x_data()
    Y = sensor.get_y_data()
    IR1 = sensor.get_ir1_data()
    IR2 = sensor.get_ir2_data()
    print('X:%d'%X,'Y:%d'%Y,'Z:%d'%Z,'IR1:%d'%IR1,'IR2:%d'%IR2)
    ledsensor.value(0)
    
    
if __name__ == "__main__":
  getcolor()  
