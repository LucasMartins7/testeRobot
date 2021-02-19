*** Settings ***
Documentation  This is some basic info about the whole suite
Library  SeleniumLibrary
Library  api.py

*** Variables ***
${checkTag}  \#9V2Y
${clanName}  the resistance
${pathFile}  ./output/members.csv
${country}  Brazil
${keyName}  Chavinha

*** Test Cases ***
Loga na conta e cria uma chave
	[Documentation]  
    [Tags]  Log In
	Start
	Login Clash
	Create Key Clash
	${get}  Get Text  //samp
	${token}  Set Variable  ${get} 
	Finish
	${locationId}  Return Locations  ${token}  ${country}
	${clanTag}  Return Clans  ${token}  ${clanName}  ${locationId}  ${checkTag}
	Write Members  ${token}  ${clanTag}  ${pathFile}


*** Keywords ***

Start
	Open Browser  https://developer.clashroyale.com/  chrome

Finish
	Close Browser

Login Clash
    Wait Until Page Contains  Log In
    Click Link  link:Log In
	Input Text  id:email  lucas.martins@primecontrol.com.br
	Input Password  id:password  FKnu9yj@!GMW5MZ
	Click Button  //button[@type='submit']
	
	
Create Key Clash
	Wait Until Page Contains  lucas.martins
	Click Button  //*[@id="content"]/div/div[2]/div/header/div/div/div[3]/div/div/button
	Click Link  link:My Account
	Click Link  link:Create New Key
	Input Text  id:name  ${keyName}
	Input Text  id:description  ${keyName}
	Input Text  id:range-0  201.26.104.228
	Click Button  //*[@id="content"]/div/div[2]/div/div/section/div/div/div[2]/form/div[5]/button
	Wait Until Page Contains  ${keyName}
	Click Element  //h4[text()="${keyName}"]
	
	
	