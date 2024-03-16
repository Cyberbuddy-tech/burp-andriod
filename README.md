<h1 style="color: #FF5733;">Burp-Android</h1>

<p>Burp-Android is a Python script that facilitates interactions with Burp Suite on an Android device using the Android Debug Bridge (ADB). This script allows users to perform various operations such as converting certificate files, pushing them to the device, and executing additional scripts remotely.</p>

<h2 style="color: #33FFBD;">Features</h2>
<ul>
  <li><strong>Certificate Conversion:</strong> Convert .der files to .pem format for use with Burp Suite.</li>
  <li><strong>Push Certificates:</strong> Push converted certificate files to the Android device's /system/etc/security/cacerts/ directory.</li>
  <li><strong>Change Permissions:</strong> Change permissions of the pushed certificate files to ensure proper functionality.</li>
  <li><strong>Reboot Device:</strong> Reboot the Android device to apply changes.</li>
</ul>

<h2 style="color: #33FFBD;">Prerequisites</h2>
<ul>
  <li>Python 3.x</li> 
  <li>Android Debug Bridge (ADB)</li>
  <li>OpenSSL</li>
  <li>Colorama Python library (will be installed automatically)</li>
  <em>(Use openssl Installer tool to install python ,openssl automatic)</em>
</ul>

<h2 style="color: #33FFBD;">Installation</h2>
<ol>
  <li>Clone the repository to your local machine:</li>
  <em>(Your Can Download And Uzip)</em>
</ol>
<pre><code style="color: #FF5733;">git clone https://github.com/yourusername/Burp-Android.git</code></pre>
<ol start="2">
  <li>Navigate to the project directory:</li>
</ol>
<pre><code style="color: #FF5733;">cd Burp-Android</code></pre>
<ol start="3">
  <li>Run the script main.py:</li>
</ol>
<pre><code style="color: #FF5733;">python main.py</code></pre>
<p>Follow the on-screen instructions to proceed with the desired actions.</p>

<h2 style="color: #33FFBD;">Usage</h2>
<p>Run main.py and follow the menu options to perform various tasks such as converting certificates, pushing them to the device, and executing additional scripts.</p>

<h2 style="color: #33FFBD;">Example</h2>
<pre><code style="color: #FF5733;">python main.py</code></pre>
<pre><code style="color: #33FFBD;">Menu:
0. Back
1. Run certy.py
2. Run phssl.py
Enter your choice:</code></pre>
<h1>Disclaimer:</h1>

The information provided in this script and associated documentation is for educational purposes only. The use of this script for any unauthorized or malicious activities is strictly prohibited. The author shall not be liable for any damages or legal consequences arising from the misuse of this script.

Use this script responsibly and only on devices and networks that you are authorized to test. Always obtain proper authorization before performing any security testing activities. By using this script, you agree to take full responsibility for your actions and to use it in compliance with applicable laws and regulations.

The author does not endorse or encourage illegal or unethical activities, including but not limited to hacking, cracking, or unauthorized access to computer systems or networks. Any actions taken using this script are solely the responsibility of the user.

This script is provided as-is, without any warranty or guarantee of its suitability or effectiveness for any particular purpose. The author makes no representations or warranties regarding the accuracy, reliability, or completeness of the information provided herein.

By using this script, you acknowledge that you have read, understood, and agree to abide by the terms of this disclaimer.

