import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Talker():
    def __init__(self, nh):
        self.pub = nh.create_publisher(Int16, "countup", 10)
        self.n = 0
        nh.create_timer(0.5, self.cb)

<<<<<<< HEAD
<<<<<<< HEAD
def cb():          #17行目で定期実行されるコールバック関数
    global n       
    msg = Int16()  #メッセージの「オブジェクト」
    msg.data = n#msgオブジェクトの持つdataにnを結び付け
    pub.publish(msg)        #pubの持つpublishでメッセージ送信
    n += 1
=======
def cb(request, response):          
    if request.name == "木村一星":
        response.age = 20
    else:
        response.age = 255

    return response
>>>>>>> dev
=======
    def cb(self):
        msg = Int16()
        msg.data = talker.n
        self.pub.publish(msg)
        self.n += 1
>>>>>>> dev

rclpy.init()
node = Node("talker")
talker = Talker(node)
rclpy.spin(node)
