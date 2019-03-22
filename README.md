Github: https://github.com/SausCode/Encase-Image-Search

This project uses the Google Vision API as well as the python module 
`imagemounter` to open an encase file, mount it, and tag image file (png, jpg, 
gif).  The user can then type in search terms, and the program outputs the path 
to the image file. Furthermore the program can show the images to the user 
along with the label that it generated.


# Setup 
Get a [Google Cloud Vision credential (json)](https://cloud.google.com/docs/authentication/api-keys?hl=en&visit_id=636886486228278470-3830920996&rd=1)

# Installation
1. `git clone https://github.com/SausCode/Encase-Image-Search.git`
2. `cd Encase-Image-Search`
3. `pip3 install -r requirements.txt`
4. `sudo python vision.py /path/to/imageFile.e01(2,3) <google_vision_credential.json>`
5. Follow on screen instructions

# Background
Our original intention was to roll the functionality of this code directly into 
Autopsy.  In researching that, we ran into a couple problems:

1. Autopsy only allows for Java Plugins, which isn't an issue, but we had a lot 
of trouble getting the Google Vision API installed for Java. In Python, on the 
other hand, it was trivially easy.
2. The greater issue was that Autopsy does not allow plugins to have outside 
libraries that have native code. This meant that even if we did succeed in 
getting the Google Vision API installed, Autopsy would not have let it run.

To compromise, we built this script that can: 
1. Take in an image file
2. Mount it (which makes it window-compatible only)
3. Walk through the file system
4. Finding all the images
5. Send the images to be analyzed by the Google Vision API
6. Report all the labels to the user and allow the user to search through
said labels.
7. Show the images themselves along with the label that was generated.

# Recommended Use
We believe that this is a valuable tool for forensics experts who are interested
in leveraging Google's powerful machine learning techniques to the world of 
digital forensics. Rather than being used as an ingest module from within 
Autopsy, we suggest that users run this program alongside Autopsy and use its
results to better understand the case at hand.

