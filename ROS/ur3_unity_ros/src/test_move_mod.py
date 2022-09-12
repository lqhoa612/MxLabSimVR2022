#!/usr/bin/env python3
import sys
import math as m
import numpy as np  

import rospy
import actionlib
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectoryPoint
from sensor_msgs.msg import JointState


# If your robot description is created with a tf_prefix, those would have to be adapted
JOINT_NAMES = [
    "shoulder_pan_joint",
    "shoulder_lift_joint",
    "elbow_joint",
    "wrist_1_joint",
    "wrist_2_joint",
    "wrist_3_joint",
]


def send_joint_trajectory():
    # Make sure the controller is loaded and activated
    trajectory_client = actionlib.SimpleActionClient("/scaled_pos_joint_traj_controller/follow_joint_trajectory", FollowJointTrajectoryAction)

    # Wait for action server to be ready
    timeout = rospy.Duration(5)
    if not trajectory_client.wait_for_server(timeout):
        rospy.logerr("Could not reach controller action server.")
        sys.exit(-1)

    # Create and fill trajectory goal
    goal = FollowJointTrajectoryGoal()
    goal.trajectory.joint_names = JOINT_NAMES

    # joint position:  [3, 2, 1, 4, 5, 6]
    position = [0, -m.pi/2, 0, -m.pi/2, 0, -m.pi/2] # rad
    duration = 3.0

    point = JointTrajectoryPoint()
    point.positions = position
    point.time_from_start = rospy.Duration(duration)
    goal.trajectory.points.append(point)

    rospy.loginfo("Executing trajectory using the /scaled_pos_joint_traj_controller")

    trajectory_client.send_goal(goal)
    trajectory_client.wait_for_result()

    result = trajectory_client.get_result()
    rospy.loginfo("Trajectory execution finished in state {}".format(result.error_code))

def JointPosCallback(data):
    dp = data.position
    temp = [ m.degrees(dp[0]), m.degrees(dp[1]), m.degrees(dp[2]), m.degrees(dp[3]), m.degrees(dp[4]), m.degrees(dp[5]) ]
    temp_rd = [ np.round(temp[0]), np.round(temp[1]), np.round(temp[2]), np.round(temp[3]), np.round(temp[4]), np.round(temp[5]) ]
    rospy.loginfo(temp_rd)

def GetJointPosition():
    trajectory_sub = rospy.Subscriber("joint_states", JointState, JointPosCallback) 

if __name__ == "__main__":
    rospy.init_node("test_move")
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        # send_joint_trajectory()
        GetJointPosition()
        rate.sleep()