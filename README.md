
# Fricofier
Created for the 2022 UGA Makeathon

## Description
This is a custom font and document conversion tool designed to save ink. It uses small white inlines in the Courier Prime font to use less ink while still being equally readable. Fricofier was desgned to promote sustainability.


This font is not meant to be used in a word processor. Recommended usage is to write your document in Courier Prime, then run this tool before printing. 

This font is best used on Inkjet printers. Inkjet printers bleed ink slightly, so this font looks more or less identical to Courier Prime. It can still be used on a laserjet printer, however it is more noticeable. 

## Installation

After downloading this repo, install the Fricofont inside the requirements folder.

Then install these dependencies:
```
pip install docx
pip install python-docx
```

## Usage
You can run this program through command line, or file explorer.
### Preferred (File explorer)
Drag the .docx file onto of the "fricofier.py" file, and a new file will be 
created with the suffix "_fricofied.docx" in the same directory as the original file. 

### Command line
Open terminal inside of same folder as fricofied.
```bash
python3 fricofier.py "document.docx"

```

## Team

- Miguel Delao-Zurita
- Will Gohn 
- Conner Caddell 
- Bhaktiar Hossain

## License
[MIT](https://opensource.org/licenses/MIT)







