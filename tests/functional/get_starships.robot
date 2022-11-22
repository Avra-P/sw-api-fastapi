*** Settings ***
Library     RequestsLibrary

*** Variables ***
${Base_URL}     http://localhost:8000
${endpoint}     /starships

${existingID}       2
${nonexistingID}    200

*** Test Cases ***
1_Get_All_Starships
    [Tags]    swapi    get    alldata   positive
    create session  Get_All_Starships  ${Base_URL}
    ${response}=     get on session     Get_All_Starships  ${Base_URL}${endpoint}
    # Validations
    ${status_code}=         convert to string       ${response.status_code}
    should be equal         ${status_code}      200
    ${body}=                Set Variable        ${response.content}
    should not be empty     ${body}

2_Get_Starship_Per_ID
    [Tags]    swapi    get    id    negative
    create session  Get_Starship_Per_ID  ${Base_URL}
    ${response}=     get on session     Get_Starship_Per_ID  ${Base_URL}${endpoint}/${existingID}
    # Validations
    ${status_code}=         convert to string       ${response.status_code}
    should be equal         ${status_code}      200
    ${body}=                Set Variable        ${response.content}
    should not be empty     ${body}

3_Get_People_Per_ID_Validation_404
    [Tags]    swapi    get    id    negative
    create session  Get_Starship_Per_ID_404  ${Base_URL}
    ${response}=     get on session     Get_Starship_Per_ID_404  ${Base_URL}${endpoint}/${nonexistingID}  expected_status=404
    # Validations
    ${status_code}=         convert to string       ${response.status_code}
    should be equal         ${status_code}      404
    ${body}=                Set Variable        ${response.content}
    log to console      ${body}
    should not be empty     ${body}
