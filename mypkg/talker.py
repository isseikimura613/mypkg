import rclpy                     #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from person_msgs.srv import Query   #通信の型（16ビットの符号付き整数


<<<<<<< HEAD
def cb():          #17行目で定期実行されるコールバック関数
    global n       #関数を抜けてもnがリセットされないようにしている
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

rclpy.init()
node = Node("talker")
srv = node.create_service(Query, "query", cb)
rclpy.spin(node)
