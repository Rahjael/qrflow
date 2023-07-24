# InfoTag

This app allows for easy QR code generation to retain user generated data for PDF documents.

The documents that the office prints expect them to be brought back at a later time and then be scanned and digitally archived.

This streamlines the process, *routing* the files to the correct folders. 

## Disclaimer 

Many assumptions are made about the structure of the company's database and ERP. This had been tailor made for my exact setup and workflow, and it is not meant to be published for use outside of the company. The repository is kept public for portfolio purposes.

*A general purpose or more customizable version may be developed in the future.*

# Installation

Just download the latest .exe from (link:github_release_page) and put it into a folder.

I never encountered any antivirus complaints. 

**The app has no effect whatsoever outside of the folder it is run from.**

# Quick usage

1. Move your pdf inside the program's folder
2. Run the .exe

At startup, the program will automatically detect if there is any .pdf in the folder it is run from. It will automatically select the _first_ .pdf it finds.

# Manual usage

1. Run the .exe
2. Click the browse button and select the .pdf you want to attach the QR code onto
3. Fill in all the forms (QR)

## Options

- **Overwrite** will target your selected file where it is and replace it
- **Default behavior**: the new file will be saved into the program's folder and will have the "\_qr" suffix in the filename

Closing the program will automatically delete the temporary files created during execution.

# Features

- [x] autodetect .pdf in program's folder
- [x] dynamic preview of selected .pdf
- [x] dynamic preview of generated qr code
- [ ] implement overwrite checkbox logic
- [ ] find out how to handle multiple pages pdfs
- [ ] multiple files selection (browse through pdfs found in same folder)
- [ ] batch process for multiple files
- [ ] reposition QR on the document or create new templates

# Screenshots

*(image gallery showcase)*
