import roslib
import rospy
import math
import tf
from sensor_msgs.msg import Image, CompressedImage
import geometry _msg.msg
from cv_bridge import CvBridge, CvBridgeError
import cv2
import pickle
import os
bridge = CvBridge()
image_downsample_rate = 1.0
i = 0
image_time = rospy.Time()
bag_path = ""

def image_callback(msg):
    global image_time, i
    image_time = msg.header.stamp
    iamge_dir = ""
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
    try:
        cv2_img = bridge.compressed_imgmsg_to_cv2(msg, "bgr8")
        cv2.imwrite('{}/{}.jpeg'.format(image_dir, image_time.to_sec()), cv2_img)
        rospy.loginfo("save image:{:.2f}".format(image_time.to_sec()))
    except CvBridgeError, e:
        rospy.loginfo(e)

if __name__ == '__main__':
    rospy.init_node('tf_listener')
    listener = tf.TransformListener()
    pose_pool = {}
    rate = rospy.Rate(32.0)
    rospy.loginfo("start listening")

    #get image data
    image_topic = ""
    rospy.Subscriber(image_topic, CompressedImage, image_callback, queue_size=200)
    rospy.spin()