# SIGIP-Camera-downloader
A simple camera download script for all the traffic cameras of Infraestruturas de Portugal.

```
options:
  -h, --help            show this help message and exit
  -r ROADS, --roads ROADS
                        Download Speciffic roads. Ex: "IC8,A1"
```

## Running the scripts

To run both scripts you will need the following python libraries:
 - `tqdm` is a library that provides a progress bar for long-running tasks. (1st script)
 - `requests` is a library that allows you to send HTTP requests using Python (1st script)
 - `argparse` is a library that provides an easy way to write command-line tools in Python (1st script)
 - `opencv-python` is a library that provides support for computer vision tasks using the OpenCV library (2nd script)
 - `pytesseract` is a library that provides support for Tesseract, an open-source OCR (Optical Character Recognition) engine, in Python (2nd script)

### Running examples

#### Normal execution 1st script(downloads every camera in Infraestruturas de Portugal database)
```
python3 .\sigip_download_script.py
```

#### Filtered execution 1st script(downloads every camera at IC19)
```
python3 .\sigip_download_script.py -r "IC19"
```

#### Normal execution 2nd script
```
python3 .\check_repeats.py
```
Example output
```
At road A1, camera 128145 did not update on last download. Folder -> .\A1\128145\1671449051000 | LastUpdate 07/12/2022 00:50
At road N6, camera 124580 did not update on last download. Folder -> .\N6\124580\1671449051000 | LastUpdate 19/12/2022 11:09
```



The second script present should be used to help determine if a camera is down. If a camera starts sending repeated video (stoped updating) it should be checked manually and probably reported to Infraestruturas de Portugal. To help with the process the script uses tesseract to print the date and time present in the video.

## Current cameras that are down

 - Na estrada A1 a camera 121686 nao faz update desde 07/12/2022 00:56
 - Na estrada A1 a camera 128143 nao faz update desde 07/12/2022 00:50
 - Na estrada A1 a camera 128144 nao faz update desde 07/12/2022 00:50
 - Na estrada A1 a camera 128145 nao faz update desde 07/12/2022 00:50
 - Na estrada A20 a camera 121693 nao faz update desde 29/10/2022 01:50
 - Na estrada A28 a camera 121702 nao faz update desde 26/10/2022 13:22
 - Na estrada IC19 a camera 121791 nao faz update desde 30/11/2022 16:19
 - Na estrada IP2 a camera 124720 nao está disponivél
 - Na estrada IP7 a camera 121807 nao faz update desde 26/10/2022 13:04
 - Na estrada IP7 a camera 121812 nao faz update desde 08/12/2022 21:11
 - Na estrada N6 a camera 10009 nao faz update desde 20/10/2022 11:42
 - Na estrada N6 a camera 10010 nao faz update desde 26/10/2022 13:07
 - Na estrada N6 a camera 10011 nao faz update desde 17/10/2022 11:16

## DISCLAIMER
The scripts provided on this repository are intended for educational and informational purposes only. The author of these scripts makes no representations or warranties of any kind, express or implied, about the completeness, accuracy, reliability, suitability or availability with respect to the scripts or the information contained in them for any purpose. Any reliance you place on such information is therefore strictly at your own risk.

In no event will the author of these scripts be liable for any loss or damage including without limitation, indirect or consequential loss or damage, or any loss or damage whatsoever arising from loss of data or profits arising out of, or in connection with, the use of the scripts.

The user of these scripts is solely responsible for any actions taken with the scripts, and is advised to use caution and common sense when using them.


