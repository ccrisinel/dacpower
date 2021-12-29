from dac import *

step_v = 10/16
step_8b = 4096/16
list_power = []
j = 0
for i,k in enumerate(range(20,105, 5)):

    list_power.append([k/10,i*step_v, int(i*step_8b)])
list_power[16][2] = 4095

#for i in list_power:
#    print(i)

def kwToVolt(kw):
    return round(1.25*kw-2.5, 1)

def kwToStep(kw):
    step = int(round(512*kw-1024,0))
    return step if step <= 4095 else 4095

def VoltToKw(volt):
    return round(0.8*volt+2, 1)

def StepToKw(step):
    return round(0.00195313*step+2, 1)

def power_cmd(kw):

    step = kwToStep(float(kw))
    dac = AptinexDAC()
    dac.set_voltage(step)



