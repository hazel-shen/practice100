# pod crash practicing
cat <<'EOF' | oc apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: crash-demo
spec:
  containers:
  - name: crash
    image: registry.access.redhat.com/ubi9/ubi-minimal
    command: ["sh","-c","echo boom; exit 1"]
  restartPolicy: Always
EOF
---
cat <<'EOF' | oc apply -f -
apiVersion: v1
kind: Pod
metadata: 
  name: pullfail-demo
spec:
  containers:
  - name: bad
    image: notexist.repo.local/ghost:never
EOF
---
cat <<'EOF' | oc apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: oom-demo
spec:
  containers:
  - name: hungry
    image: python:3.12-alpine
    command: ["python","-c","a=[]\nwhile True: a.append('x'*1024*1024)"]
    resources:
      limits: { memory: "10Mi" }
      requests: { memory: "10Mi" }
EOF
