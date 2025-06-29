from VENI.proxy import UAVController
import rospy
if __name__ == "__main__":

    controller = UAVController("standard_vtol", "0", takeOffOffset=[2.3, 0.4, 0.5])
    flag = 0
    rate = rospy.Rate(20)
    controller.send_command("multirotor")
    rospy.sleep(1.5)
    for i in range(100):
        controller.goto_position(0, 0, 5.0)
        controller.send_command("OFFBOARD")
        rate.sleep()
        controller.send_command("ARM")
    while not rospy.is_shutdown():
        print(controller.state.mode)
        if flag == 0:
            
            reach1 = controller.goto_position(0, 0, 14.0)
            print(reach1)
            if reach1 :
                flag = 1
                controller.send_command("plane")
        if flag == 1:
            reach2 = controller.goto_position(500, 0, 25.0)
        rate.sleep()

