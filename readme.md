# File Compressor
This code is a simple file compressor using the PySimpleGUI library. It allows users to select files to compress and a destination folder for the compressed files. 

## Requirements
- Python 3.x 
- PySimpleGUI library 

## Usage 
1. Import the PySimpleGUI library as Sg: `import PySimpleGUI as Sg` 
2. Create labels, inputs, and buttons for the user interface: 

    ```label1 = Sg.Text("Select files to compress:")  
    input1 = Sg.Input()  
    choose_button1 = Sg.FilesBrowse("Choose")  

    label2 = Sg.Text("Select Destination Folder:")  
    input2 = Sg.Input()  
    choose_button2 = Sg.FolderBrowse("Choose")  

    compress_button = Sg.Button("Compress")``` 
    
3. Create a window with the layout of the user interface elements: `window = Sg.Window("File Compressor", layout=[[label1, input1, choose_button1], [label2, input2, choose_button2], [compress_button]])` 
4. Read and close the window: `window.read() window.close()`