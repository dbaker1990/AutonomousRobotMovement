import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import ColorRGBA

class TimeDiag:
    def __init__(self):
        self.update_rate = 50
        self.freq = 1./self.update_rate
        
        # initialize variables
        self.scan_data = []
        
        #subscribers
        rospy.Subscriber("/scan", LaserScan, self.LaserCallBack)

        # publishers
        self.pub1 = rospy.Publisher('/scan1', LaserScan, queue_size=10)
        self.pub2 = rospy.Publisher('/scan2', LaserScan, queue_size=10)
        self.pub3 = rospy.Publisher('/scan3', LaserScan, queue_size=10)
        
        # timers
        rospy.Timer(rospy.Duration(self.freq), self.LaserScanTimeUpdate)
        

    def LaserCallBack(self, msg):
        self.scan_data = msg
        
    def LaserScanTimeUpdate(self, event):
        pub = rospy.Publisher('chatter_color', ColorRGBA)
        pub2 = rospy.Publisher('Diag 2', ColorRGBA)
        #scan = LaserScan()
        
        #scan.header.stamp = self.get_clock()
        
        t = rospy.Time()
        seconds = t.to_sec()
        
        currentTime = rospy.Time.now()
        
        pub.publish(currentTime - seconds)
        
        if currentTime - seconds >= 5.0:
            print("Time Stamp is wrong in scan 1!")
            pub2.publish("The time stamp is wrong. The difference value is " + currentTime - seconds)
        
    def kill_node(self):
        rospy.signal_shutdown("Done")

rospy.init_node('talker', anonymous=True)

while not rospy.is_shutdown():
    print("I'm running!")

if __name__ == "__main__":
    
    try:
        td = TimeDiag()
    except rospy.ROSInterruptException:
        pass