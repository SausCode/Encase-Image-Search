Github: https://github.com/SausCode/Encase-Image-Search

This project uses the Google Vision API as well as the python module imagemounter to open an encase file, mount it, and tag image file (png, jpg, gif).
The user can then type in search terms and the program outputs the path to the image file.

Steps to setup:
1) get a google cloud vision credential (json) @ https://cloud.google.com/docs/authentication/api-keys?hl=en&visit_id=636886486228278470-3830920996&rd=1
2) `git clone https://github.com/SausCode/Encase-Image-Search.git`
3) `cd Encase-Image-Search`
4) `pip3 install -r requirements.txt`
5) `sudo python vision.py </path/to/encase.e01(2,3)> <google_credential.json>`
6) follow on screen instructions
