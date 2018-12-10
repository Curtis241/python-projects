*** Settings ***
Library  test_automation.test_suites.test_cases.MduGatewayTestCases    ${IP_ADDRESS}

*** Test Cases ***
Test System Name
   ${RESULT}=  Check System Name
   Should Be True  ${RESULT}
