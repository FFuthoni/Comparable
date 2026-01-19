# Comparable

Compare two, ideally similar, almost identical objects or collections in one click.

## Overview

Imagine a scenario where you are modelling or sculpting, and you are about to make changes that you are not sure about yet, or you want to make an alternate version of your object, or you just like your current progress so much that you don't want to lose it.  
So you duplicate your object as a backup and continue working.  
Afterward, since you have made a backup, you want to see how different your new model is compared to the old one.  
You hide one object and show the other, hide one object and show the other, hide one object and show the other, and so on.  
It's fine, but it can get tedious after a while.  
So with this add-on, I hope to make those processes just a little, tiny bit easier.

Open the sidebar, click **Comparable**, select two objects, and press the switch button, simple as that.
![An animated gif showing the use of an addon in Blender sidebar panel](https://github.com/user-attachments/assets/5e6b2d0c-4ce1-4810-a7f7-c6f2b60f0149)

or collections.
![An animated gif showing the use of an addon in Blender sidebar panel](https://github.com/user-attachments/assets/1ecced3f-6c1e-444b-8c82-3b5c5270ff29)


## Features & Options

1. **Sidebar panel**
    - Switch button, obviously  
          Switch between the two objects or collections.  
          Two **different** objects or collections need to be selected first for the button to be functional.
          ![Comparable Demo_Tile_Switch button](https://github.com/user-attachments/assets/e4b996cf-2093-4a76-88d8-5a4cd0c7acdb)
        
    - Reset button  
          Reset both selected objects or collections to be visible.  
          The reset button does not take into account the objects or collections' visibility prior to the comparison and will just set all to be visible.  
          Two **different** objects or collections also need to be selected first for the button to be functional.
          ![Comparable Demo_Tile_Reset button](https://github.com/user-attachments/assets/72f86c07-4d21-4b4e-8cd5-168a00b67582)

    - Affect render  
          An option to affect the render visibility of objects or collections.  
          This option will only take effect when you press the Switch button after you enable this option.  
          When enabled, the Reset button will also reset both objects or collections render visibility the same way it resets the viewport visibility.  
          ![Comparable Demo_Affect Render](https://github.com/user-attachments/assets/6177dbf5-570b-41e6-9d61-13f52c9641c5)


2. **Preferences**
    - Keymaps  
          There are four configurable keymaps for each button. However, they are deactivated by default to avoid conflict with your setup.  
          You can change them to your liking.
          ![Comparable Demo_Keymaps](https://github.com/user-attachments/assets/082362ef-0e7d-4dbd-bc65-afedd59bc2ff)

   - Sidebar category  
          You can change the sidebar category to whichever category you like—either an existing one or a custom one.
          ![Comparable Demo_Sidebar category](https://github.com/user-attachments/assets/b944e6f5-2fc5-4b3e-b389-03dfc1fa17e0)

## Compatibility
There are three main files included in the [release page](https://github.com/FFuthoni/Comparable/releases) for each Blender version you are using.  
_Please be aware that these results were based on my limited tests in the time that I had available. Thanks for your understanding._
1. *... _2.8x.zip* -> for Blender version 2.8 and newer. Up to 2.93.
2. *... _3.0x.zip* -> for Blender version 3.0 and newer. Up to 4.1.
3. *... _4.2x.zip* -> for Blender version 4.2 and newer. This version also complies with the new Blender extension guideline.

## Installation
- Download from the [release page](https://github.com/FFuthoni/Comparable/releases)
- Download from the Blender Extension website. [Awaiting approval queue](https://extensions.blender.org/approval-queue/comparable/)
