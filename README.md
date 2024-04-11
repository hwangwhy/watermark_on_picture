

# About this stuff
A simple way to add a watermark in to your picture 


## Installation
Clone the project and install the dependencies.
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
 pip install pillow
```

## Usage
To add a watermark to your images, create a watermark png file and place all of your photos in a folder. Then call watermarker.py as such:
```python
python watermark.py input_dir output_dir watermark.png
```
Create and replace the input_dir with the folder of the photos, output_dir with the folder to store the modified folders, and watermark.png with your watermark.

These folders and picture need to be on the source code folder.
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
