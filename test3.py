from digi.xbee.devices import XBeeDevice
from digi.xbee.exception import TimeoutException, InvalidPacketException
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
i = 0.0
def main():
	print(" +-----------------------------------------+")
	print(" |    Python Xbee Receive And Graph Data   |")
	print(" +-----------------------------------------+\n")
	fig=plt.figure()
	ax5=fig.add_subplot(1,1,1, projection='polar')
	props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
	def inc():
		global i
		if i<360:
			i+=1
		else:
			i=0.0
	def animate(j):
		try:
			ax5.cla()
			inc()
			ax5.plot([1,i*np.pi/180],[0, 1],'k', linewidth=5)#points[15][-1]
			ax5.vlines(0, 0, 1, colors='g', linestyles='dashed', label='')
			ax5.vlines(60*np.pi/180, 0, 1, colors='r', linestyles='dashed', label='')
			ax5.vlines(-60*np.pi/180, 0, 1, colors='r', linestyles='dashed', label='')
			if i < 10:
				number = '0'+str(i)
			else:
				number = str(i)
			textstr = ''.join((("Angle: {}".format(number))))
			ax5.set_title("Lean Angle")
			ax5.text(215*np.pi/180, 0.85, textstr,fontsize=14, bbox=props)
			ax5.set_rmax(1)
			ax5.set_yticklabels([])
			ax5.set_theta_zero_location('N')
			ax5.set_theta_direction(-1)
			ax5.set_thetamin(-90)
			ax5.set_thetamax(90)
			#ax5.set_xticklabels([-60,0,60])
			ax5.grid(True)
				
		except Exception as e:
			print(e)
			print('first one')
			pass
	ani = animation.FuncAnimation(fig, animate, interval=10)
	mng = plt.get_current_fig_manager()
	mng.window.state('zoomed')
	plt.show()
if __name__ == '__main__':
    main()