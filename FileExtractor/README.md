## :scroll: Magic Copy

This App provide a simple way to copy all the latest version of your render shots, based on a series of folders provided as an input.

<img width="1199" height="620" alt="image" src="https://github.com/user-attachments/assets/edd2f908-8745-443e-a5b7-8a15760ad5bd" />



<br/>The *SOURCE_FOLDER* is where all your shots are located, example C:/Testing/SOURCE_FOLDER contains the folders [shot_0010, shot_0020, shot_0030 and so on].

The DESTINATION_FOLDER is where all your new files will be located

The Render folder is where your render is located, sometimes there are tasks like cmp, roto, tracking and more, you want to be sure to take the right path from **ANY SHOT FOLDER**
> [!NOTE]
> The script will automatically make the path out of your render folder in order to find any match. The name Render is just a place holder, you can call it collection, EXR, Dinosaur or however you want
> but the path should be the same for every shot folder. if your shot_0010 has shot_0010/Dinosaur/cmp/Render, the following folders (shot_0020, shot_0020,...., shot__n) has to have the same structure!


Shot patter will be you name convention for the Shot_####
>[!CAUTION]
> The Shot patter is very important! need to match **EXACTLY** the patter of your shot convention!
> I could have omitted this but everyone has his own way to name folders, you can call them shot_0010, SHOT_0010, Shot_0010, Dinosaur_0010, DINOSAUR_0010, etc etc.
> This part will make sure to iterate through all of the folder! Also need to match the Shot folder in your render folder parameter!

<br\>I hope everyhting is clear, this is the version 0.1 and I still need to improve things, but it works decently. If you need anything or you find issues open a ticket!
