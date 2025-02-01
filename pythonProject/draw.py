import matplotlib.pyplot as plt

# plt.xlabel('The range of carsMain and carsSide', fontdict={'family' : 'Times New Roman', 'size'   : 16})#x轴标签
# plt.ylabel('Synthesis Time (s)', fontdict={'family' : 'Times New Roman', 'size'   : 16})#y轴标签
#
# x1 = [5,10,15,20,25,30,35]
#
# y1 = [0.232833333, 1.925333333, 6.703, 32.54833333, 64.525, 174.2355, 383.317]
# x2 = [5,10,15,20,25,30,35]
# y2 = [0.123, 0.123, 0.123, 0.123, 0.123, 0.123, 0.123]
#
# plt.plot(x1,y1,'-o',ms=5)
# plt.plot(x2,y2,'-o',ms=5)
#
# plt.legend(['Boolean encoded method',"Our method"], fontsize=12)
# plt.savefig('SynTime.pdf', bbox_inches='tight')
# plt.show()




plt.xlabel('Integer range', fontdict={'family' : 'Times New Roman', 'size'   : 16})#x轴标签
plt.ylabel('Synthesis Time (s)', fontdict={'family' : 'Times New Roman', 'size'   : 16})#y轴标签

x1 = [5,10,15,20,25,30,35, 40]

y1 = [0.1446, 0.199, 0.2556, 0.3812, 0.5012, 0.6862, 0.9138, 1.2146]
x2 = [5,10,15,20,25,30,35, 40]
y2 = [0.151,0.151,0.151,0.151,0.151,0.151,0.151,0.151 ]

plt.plot(x1,y1,'-o',ms=5)
plt.plot(x2,y2,'-o',ms=5)

plt.legend(['Boolean encoded method',"Our method"], fontsize=12)
plt.savefig('SynTime.pdf', bbox_inches='tight')
plt.savefig('SpeedControl.pdf', bbox_inches='tight')
plt.show()







plt.xlabel('Integer range', fontdict={'family' : 'Times New Roman', 'size'   : 16})#x轴标签
plt.ylabel('Synthesis Time (s)', fontdict={'family' : 'Times New Roman', 'size'   : 16})#y轴标签

x1 = [5,10,15,20,25,30]

y1 = [ 0.217, 1.5424, 5.489, 25.78833, 49.19567, 133.2725]
x2 = [5,10,15,20,25,30]
y2 = [0.1294,0.1294,0.1294,0.1294,0.1294,0.1294]

plt.plot(x1,y1,'-o',ms=5)
plt.plot(x2,y2,'-o',ms=5)

plt.legend(['Boolean encoded method',"Our method"], fontsize=12)
plt.savefig('PlaceControl.pdf', bbox_inches='tight')
plt.show()



plt.xlabel('Integer range', fontdict={'family' : 'Times New Roman', 'size'   : 16})#x轴标签
plt.ylabel('Synthesis Time (s)', fontdict={'family' : 'Times New Roman', 'size'   : 16})#y轴标签

x1 = [5,10,15,20,25,30]

y1 = [0.1934, 1.446, 5.3792, 22.66, 47.15, 122.14]
x2 = [5,10,15,20,25,30]
y2 = [0.1208,0.1208,0.1208,0.1208,0.1208,0.1208 ]

plt.plot(x1,y1,'-o',ms=5)
plt.plot(x2,y2,'-o',ms=5)

plt.legend(['Boolean encoded method',"Our method"], fontsize=12)
plt.savefig('StockStatus.pdf', bbox_inches='tight')
plt.show()



plt.xlabel('Integer range', fontdict={'family' : 'Times New Roman', 'size'   : 16})#x轴标签
plt.ylabel('Synthesis Time (s)', fontdict={'family' : 'Times New Roman', 'size'   : 16})#y轴标签

x1 = [5,10,15,20,25,30,35]

y1 = [0.232833333, 1.925333333, 6.703, 32.54833333, 64.525, 174.2355, 383.317]
x2 = [5,10,15,20,25,30,35]
y2 = [0.123, 0.123, 0.123, 0.123, 0.123, 0.123, 0.123]

plt.plot(x1,y1,'-o',ms=5)
plt.plot(x2,y2,'-o',ms=5)

plt.legend(['Boolean encoded method',"Our method"], fontsize=12)
plt.savefig('ComfortZone.pdf', bbox_inches='tight')
plt.show()