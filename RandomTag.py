import random
import string

random_image_tag = ''.join(random.choices(string.ascii_lowercase, k=10))

yaml_template = f"""
apiVersion: v1
kind: Namespace
metadata:
  name: ns-demo-anish-sahariar

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-deployment
  namespace: ns-demo-anish-sahariar
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
        - name: my-container
          image: 840249918025.dkr.ecr.us-east-2.amazonaws.com/demo:{random_image_tag}
          ports:
            - containerPort: 80
"""

with open('deployment_random.yaml', 'w') as yaml_file:
    yaml_file.write(yaml_template)

print("YAML file with random image tag generated.")
