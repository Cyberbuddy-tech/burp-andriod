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
