import rospy
import time

from sensor_msgs.msg import Imu

def listener():
	rospy.init_node('imu_listener', anonymous=True)
	rospy.Subscriber("/imu/data", Imu, imuCallback)
	rospy.spin()

def imuCallback(data):
	orient_x = float(round(data.orientation.x, 3))
	orient_y = float(round(data.orientation.y, 3))
	orient_z = float(round(data.orientation.z, 3))

	#print("Orientation -> X: ", orient_x, end = ' ')
	#print("Y: ", orient_y, end = ' ')
	#print("Z: ", orient_z, end = '\r')

	lin_x = float(round(data.linear_acceleration.x, 3))
	lin_y = float(round(data.linear_acceleration.y, 3))

	#print("Linear Acc. -> X:", lin_y, end = '   ')

	ang_z = float(round(data.angular_velocity.z, 3))
	print("Angular Vel. -> Z: ", ang_z, end = '\r')

if __name__ == '__main__':
	listener()
