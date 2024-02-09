# QRDataHarvester
A tool which records the data from QR Code and save in the txt file.

<h1>Setup</h1>
1. Make sure the python and pip3 is installed on your system (Windows/Linux/MacOS).<br>
2. Install the <i>pillow</i> and <i>pyzbar</i> module on your system (Windows/Linux/MacOS) by copy and run the following command :<br><br>

```
pip3 install -r requirements.txt
```

<h1>Tested Systems</h1>
The tool is currently tested on : <br>
1. Windows (10)<br>
The testing is going on different systems.

<h1>Install and Run</h1>
1. Download or Clone the Repository.<br>
2. Open that folder in Terminal (Linux/MacOS) or CMD/Powershell (Windows).<br>
3. Type the following command : <br>
<i>

For Windows<br><br>

```
python QRDataHarvester.py -i "name_of_image.png/path_of_image_file_with_filename.png" -o "name_of_text_file.txt"
```
</i>

<i>
For Linux/MacOS<br>

```
./python QRDataHarvester.py -i "name_of_image.png/path_of_image_file_with_filename.png" -o "name_of_text_file.txt"
```
</i><br>
5. Hit enter.<br>
6. After sometimes, the data from QR Code is save in the txt file.

# Includes
It also supports other image formats like <b>jpg</b>, <b>jpeg</b> and <b>bmp</b>.

<h1>Key Features</h1>
<b>1. It works on any design of QR Code.</b><br>
<b>2. It stores every data in txt file.</b><br>
