from troposphere import Ref, Template
import troposphere.ec2 as ec2

t = Template()

# Instance as parameters
# instance = ec2.Instance("myinstance", ImageId="ami-013be31976ca2c322", InstanceType="t1.micro")

# Instance as properties
instance = ec2.Instance("myinstance")
instance.ImageId = "ami-013be31976ca2c322"

instance.InstanceType = "t1.micro"
t.add_resource(instance)

print(t.to_json())
