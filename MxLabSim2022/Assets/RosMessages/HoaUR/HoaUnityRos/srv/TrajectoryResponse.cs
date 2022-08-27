//Do not edit! This file was generated by Unity-ROS MessageGeneration.
using System;
using System.Linq;
using System.Collections.Generic;
using System.Text;
using Unity.Robotics.ROSTCPConnector.MessageGeneration;

namespace RosMessageTypes.HoaUnityRos
{
    [Serializable]
    public class TrajectoryResponse : Message
    {
        public const string k_RosMessageName = "hoa_unity_ros/Trajectory";
        public override string RosMessageName => k_RosMessageName;

        public double[] jointAngles;

        public TrajectoryResponse()
        {
            this.jointAngles = new double[0];
        }

        public TrajectoryResponse(double[] jointAngles)
        {
            this.jointAngles = jointAngles;
        }

        public static TrajectoryResponse Deserialize(MessageDeserializer deserializer) => new TrajectoryResponse(deserializer);

        private TrajectoryResponse(MessageDeserializer deserializer)
        {
            deserializer.Read(out this.jointAngles, sizeof(double), deserializer.ReadLength());
        }

        public override void SerializeTo(MessageSerializer serializer)
        {
            serializer.WriteLength(this.jointAngles);
            serializer.Write(this.jointAngles);
        }

        public override string ToString()
        {
            return "TrajectoryResponse: " +
            "\njointAngles: " + System.String.Join(", ", jointAngles.ToList());
        }

#if UNITY_EDITOR
        [UnityEditor.InitializeOnLoadMethod]
#else
        [UnityEngine.RuntimeInitializeOnLoadMethod]
#endif
        public static void Register()
        {
            MessageRegistry.Register(k_RosMessageName, Deserialize, MessageSubtopic.Response);
        }
    }
}
