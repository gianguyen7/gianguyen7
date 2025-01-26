#!/bin/bash

# Set variables
ACR_NAME="w255mids.azurecr.io/cinnguyenn/project"
NAMESPACE="cinnguyenn"                        
KUSTOMIZATION_PATH=".k8s/overlays/prod/kustomization.yaml"   

# Get the current Git commit hash (short version)
TAG=$(git rev-parse --short HEAD)

# Full image name with commit hash
FULL_IMAGE_NAME="$ACR_NAME/$IMAGE_NAME:$TAG"

# Build the Docker image for the appropriate platform
echo "Building Docker image: $FULL_IMAGE_NAME..."
docker build --platform linux/amd64 -t ${ACR_NAME}:${TAG} .

# Push the images (specific tag and latest) to Azure Container Registry
echo "Pushing Docker image to ACR..."
az acr login --name w255mids
docker push ${ACR_NAME}:${TAG}

export TAG=${TAG}

# Update kustomization.yaml with the new image tag
echo "Updating kustomization.yaml with new image tag: $TAG..."
yq -i '.images[].newTag = strenv(TAG)' ${KUSTOMIZATION_PATH}

# Apply the updated kustomization.yaml to the cluster
echo "Applying kustomization.yaml to Kubernetes..."
kubectl apply -k .k8s/overlays/prod

echo "Checking deployment status..."
kubectl rollout status deployment/project-api-deployment -n ${NAMESPACE}

# Output success message
echo "Deployment complete"
