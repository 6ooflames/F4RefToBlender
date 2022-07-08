
# F4RefToBlender   [![Badge License]][License]

*Import reference data from **Bethesda** games into **Blender**.*

<br>

## Supported

<kbd>  Fallout 4  </kbd>  
<kbd>  Skyrim CK  </kbd>

<br>
<br>

## Requirements

- **[PyNifly]**

<br>
<br>

## Usage

1.  Use **Bethesda Archive Extractor** to export:
    
    <kbd>  Meshes  </kbd>  
    <kbd>  Textures  </kbd>  
    <kbd>  ( Materials )  </kbd>
    
    *Requires a lot of space.*
    
2.  Use **Bethesda's Creation Kit** to export the object data <br>
    table which contains the editorID and internal file path.
    
3.  Choose an exterior / interior cell and export its reference data;

4.  Import the python script into **Blender**'s text editor.

5.  Adjust the 3 file paths to match yours.

6.  Execute the script.

    *Blender will lock up, however you can monitor* <br>
    *the progress in a separate terminal window.*

<br>


<!----------------------------------------------------------------------------->

[PyNifly]: https://github.com/BadDogSkyrim/PyNifly

[License]: LICENSE

[Badge License]: https://img.shields.io/badge/License-GPL_3-blue.svg?style=for-the-badge