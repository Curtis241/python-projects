#!/bin/bash

run_robot_tests() {
    IP_ADDRESS=$1
    echo "Running tests on mdu gateway at ${IP_ADDRESS}"
    SCRIPT=$(readlink -f "$0")
    SCRIPTPATH=$(dirname "$SCRIPT")
    source venv3/bin/activate
    pybot --pythonpath ${SCRIPTPATH}/test_automation/ -d output/ -v IP_ADDRESS:${IP_ADDRESS} test_automation/test_automation/test_suites/
}

if [[ $# -eq 1 ]]; then
    run_robot_tests $1
else
  echo "Invalid parameters"
fi

