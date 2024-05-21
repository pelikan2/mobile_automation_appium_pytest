# mobile_automation_appium_pytest

This automation framework is written in appium with pytest, automated application called Pelipecky, is mobile alternative
of popular website Pelikan.sk.

# Project Setup

1. Clone project to your favourite IDE: https://github.com/pelikan2/mobile_automation_appium_pytest.git
2. In file requirements.txt are all necessary packages, so in terminal paste this command:

<br>MacOS: pip3 install -r requirements.txt </br>
<br>Windows: pip install -r requirements.txt </br>

**appium setup:**
To be able to run automation script on mobile device in appium, you need to install appium to your machine
<br>**for macOS:**</br>
1. install brew (if not installed) **/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"** 
2. brew install node
3. npm install -g appium
4. npm install -g appium-doctor
5. appium-doctor --android
6. install JDK
7. install android SDK
8. configure zsh_profile file

create zsh_profile file with environment variables:

    #JAVA
    export JAVA_HOME="$(/usr/libexec/java_home -v 21)"
    export JAVA_HOME='/Library/Java/JavaVirtualMachines/jdk-21.jdk/Contents/Home'
    export PATH=$JAVA_HOME/bin:$PATH
    
    #ANDROID
    export ANDROID_HOME=/Users/Vlado/Library/Android/sdk
    export PATH=$ANDROID_HOME/platform-tools:$PATH
    export PATH=$ANDROID_HOME/tolls:$PATH
    export PATH=$ANDROID_HOME/tools/bin:$PATH

9. source zsh_profile
10. Install UIAutomator plugin to your appium server
11. run appium server: **appium -p 4724** - I run appium server on port 4724.
12. You should be able to run test cases in your IDE terminal
pytest Tests/test_scenarios.py -v -s 

<br>**for windows:**</br>
2. install node
3. npm install -g appium
4. npm install -g appium-doctor
5. appium-doctor --android
6. install JDK
7. install android SDK
8. configure environment variables for windows:


    #JAVA
    export JAVA_HOME="$(/usr/libexec/java_home -v 21)"
    export JAVA_HOME='/Library/Java/JavaVirtualMachines/jdk-21.jdk/Contents/Home'
    export PATH=$JAVA_HOME/bin:$PATH
    
    #ANDROID
    export ANDROID_HOME=/Users/Vlado/Library/Android/sdk
    export PATH=$ANDROID_HOME/platform-tools:$PATH
    export PATH=$ANDROID_HOME/tolls:$PATH
    export PATH=$ANDROID_HOME/tools/bin:$PATH

10. Install UIAutomator plugin to your appium server
11. run appium server: **appium -p 4724**
12. You should be able to run test cases in your IDE terminal
pytest Tests/test_scenarios.py -v -s

# How to generate allure report

You need to install allure to your machine
<br> MacOS: brew install allure </br>
<br> Windows: install package scoop, link: https://scoop.sh/, allure installation: scoop install allure</br>

<br> To generate .json files for allure report creation: pytest -v -s --alluredir=reportallure </br>

<br> allure serve reportallure\ - generate allure report</br>