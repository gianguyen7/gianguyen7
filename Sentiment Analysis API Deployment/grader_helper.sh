#!/bin/bash
accumulator=0
expected=5

assert() {
    local message="$1"
    local assertion="$2"

    if [[ -z "$message" || -z "$assertion" ]]; then
        echo "❌ Assertion error: Missing message or assertion."
        return 1
    fi

    if eval "$assertion"; then
        echo "✅ $message"
        accumulator=$((accumulator + 1))
    else
        echo "❌ $message"
    fi
}

# kubectl get virtualservices.networking.istio.io -A | grep mids255.com | awk '{print $4}' | tr -d '["]' | awk -F. '{print $1}' | sort | uniq  >NAMESPACE.txt

# Example Payloads
RegularPayload='{ "MedInc":10, "HouseAge":42, "AveRooms":6.98, "AveBedrms":1.02, "Population":322, "AveOccup":2.55, "Latitude":37.88, "Longitude":-122.23 }'
multiPayload='{"houses": [{ "MedInc": 8.3252, "HouseAge": 42, "AveRooms": 6.98, "AveBedrms": 1.02, "Population": 322, "AveOccup": 2.55, "Latitude": 37.88, "Longitude": -122.23},{ "MedInc": 0, "HouseAge": 0, "AveRooms": 0, "AveBedrms": 0, "Population": 0, "AveOccup": 0, "Latitude": 0, "Longitude": 0}]}'
projectPayload='{"text": ["string"]}'

while read -r NAMESPACE; do
    echo ""
    echo "Namespace: $NAMESPACE"

    # Perform warm-up requests
    for run in {1..10}; do
        curl --silent --output /dev/null -X POST "https://${NAMESPACE}.mids255.com/lab/predict" -H 'Content-Type: application/json' -d "$RegularPayload"
        curl --silent --output /dev/null -X POST "https://${NAMESPACE}.mids255.com/lab/bulk-predict" -H 'Content-Type: application/json' -d "$multiPayload"
        curl --silent --output /dev/null -X POST "https://${NAMESPACE}.mids255.com/project/bulk-predict" -H 'Content-Type: application/json' -d "$projectPayload"
    done

    # Assertions for various endpoints
    curl --fail --silent -X POST "https://${NAMESPACE}.mids255.com/lab/predict" -H 'Content-Type: application/json' -d "$RegularPayload" >/dev/null
    assert "Check lab4 predict" "[[ $? -eq 0 ]]"

    curl --fail --silent -X POST "https://${NAMESPACE}.mids255.com/lab/bulk-predict" -H 'Content-Type: application/json' -d "$multiPayload" >/dev/null
    assert "Check lab4 bulk-predict" "[[ $? -eq 0 ]]"

    curl --fail --silent -X POST "https://${NAMESPACE}.mids255.com/project/bulk-predict" -H 'Content-Type: application/json' -d "$projectPayload" >/dev/null
    assert "Check project bulk-predict" "[[ $? -eq 0 ]]"

    curl --fail --silent "https://${NAMESPACE}.mids255.com/lab/docs" >/dev/null
    assert "Check lab docs" "[[ $? -eq 0 ]]"

    curl --fail --silent "https://${NAMESPACE}.mids255.com/project/docs" >/dev/null
    assert "Check project docs" "[[ $? -eq 0 ]]"
done <NAMESPACE.txt

if [[ $accumulator -eq $expected ]]; then
    echo "🎉 All assertions passed! Total: $expected"
else
    echo "❌ Some assertions failed. Passed: $accumulator/$expected"
fi

# echo "load test"
# while read NAMESPACE; do
#     echo "$NAMESPACE"
#     k6 run load.js
# done <NAMESPACE.txt
