# F4RefToBlender
Import Reference data from Fallout 4 or Skyrim CK into Blender using this and BadDogSkyrim's nifly implementaion.

Using Bethesda Archive Extractor, export the Meshes, Textures, and optionally Materials archives onto a large HDD.

Then, in Bethsoft's Creation Kit, export the object data table which contains the editorID and internal file path.
After that, choose an exterior or interior cell and export it's reference data.

Install this Blender addon: https://github.com/BadDogSkyrim/PyNifly
In Blender, import the python script into the text editor, and adjust the 3 file path strings to match yours.
Execute the script. Blender will lock up, but you can monitor the progress in the seperate terminal window.
