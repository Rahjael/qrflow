

# QRFlow (temporary name)

This app allows for easy qr code generation for pdf documents.

It has been tailor made for the company I work for. Codes are intended for documents that the office prints expecting them to be brought back at a later time to be scanned and archived.

Many assumptions are made about the structure of the company's database and ERP. This is intended as for the time being the app is not meant to be published for use outside of the company. The repository is kept public for portfolio purposes.


*A general purpose or more customizable version may be developed in the future.*


# Installation

Just download the latest .exe from (link:github_release_page) and put it into a folder.

I never encountered any antivirus complaints. In case yours does, just allow the .exe to run or whitelist it. **The app has no effect whatsoever outside of the folder it is run from.**


# Usage

***The app is currently meant to operate on single page .pdfs only.***


## Quick mode

1. Move your pdf inside the program's folder
2. Run the .exe

At startup, the program will automatically detect if there is any .pdf in the folder it is run from. It will automatically select the _first_ .pdf it finds.

## Manual mode

1. Run the .exe
2. Click the browse button and select the .pdf you want to attach the qr code onto


After having selected the target .pdf, fill in all the forms and a qr code will be automatically generated.

You can overwrite your original file or create a new one. Overwrite will target your selected file where it is. If you unflag the overwrite option, the new file will be saved into the program's folder and will have the "\_qr" suffix in the filename.

Closing the program will automatically delete the temporary files created during execution.


# Features

- [x] autodetect .pdf in program's folder
- [x] dynamic preview of selected .pdf
- [x] dynamic preview of generated qr code
- [ ] implement overwrite checkbox logic
- [ ] find out how to handle multiple pages pdfs
- [ ] multiple files selection (browse through pdfs found in same folder)
- [ ] database of generated qrcodes




# Images



![prev_01](https://github.com/Rahjael/qrflow/blob/main/docs/prev_01.png?raw=true)
![prev_02](https://github.com/Rahjael/qrflow/blob/main/docs/prev_02.png?raw=true)