using RosMessageTypes.Ur3UnityRos;
using Unity.Robotics.ROSTCPConnector;
using UnityEngine;

public class JointPosPub : MonoBehaviour
{
    [InspectorReadOnly]public string topicName = "joint_pos";
    public URController urCtrl;
    public float publishMessageFrequency = .5f;

    ROSConnection ros;
    float timeElapsed;

    private void Start()
    {
        ros = ROSConnection.GetOrCreateInstance();
        ros.RegisterPublisher<JointPositionMsg>(topicName);
    }

    private void Update()
    {
        timeElapsed += Time.deltaTime;
        if (timeElapsed > publishMessageFrequency)
        {
            JointPositionMsg jPos = new JointPositionMsg(urCtrl.GetJointAngles());
            ros.Publish(topicName, jPos);
            print("Message published.");
            timeElapsed = 0;
        }
    }
}
