## Smart Colony Counter
microbial colony counter algorithm that is much easier to use and smarter to count colonies.

## what this software exactly do?
main goal of this Application is create an easy to use Colony counter, without any calibration or technical complexity. A thing just works.

## How to use?

 1. Download one of the releases that suitable for your system and run
    it.
 2. select a Folder to save count output images.
 ![enter image description here](https://github.com/mjroohany-rgb/smart-colony-counter/blob/main/How%20to%20use/How%20to%20use%20%281%29.png)
 4. select image containing cultured Petri dish.
 ![enter image description here](https://github.com/mjroohany-rgb/smart-colony-counter/blob/main/How%20to%20use/How%20to%20use%20%282%29.png)

> usually does not need clean plate marks or opening plate door - just a clear image is enough.

 5. Microbial plate will automatically recognized,
  calibrations will automatically done for each picture separately
   ![enter image description here](https://github.com/mjroohany-rgb/smart-colony-counter/blob/main/How%20to%20use/How%20to%20use%20%283%29.png)

> (so you can use multiple culture mediums with different colors).

 5. results will be shown:
 - if it is acceptable you can count new plate
![enter image description here](https://github.com/mjroohany-rgb/smart-colony-counter/blob/main/How%20to%20use/How%20to%20use%20%284%29.png)
![enter image description here](https://github.com/mjroohany-rgb/smart-colony-counter/blob/main/How%20to%20use/How%20to%20use%20%285%29.png)
- If it is not acceptable you can recount with **"look for smaller colonies"** option that has different counting algorithm which is more suitable for small sized colonies.

## Requirements
I suggest **python version 3.8.20** specially when you want to build from source.
also using **conda** can help full for handling dependencies

**library requirements:**

 - easygui==0.98.3
 - numpy==1.24.3
 - opencv-python==4.10.0
 - scikit-image==0.20.0

## Acknowledgement

This project was originally intended as a (D.V.M) degree thesis in **Islamic Azad University - Shabestar Branch** - Faculty of Veterinary Medicine.

subject was: Design and construction of the smart colony counter device and compare its functionality with the standard counting method.

Supervisor: M.H. Movassagh (PhD)
Advisor: A.A. Dadjouyan (PhD)
Author: Mohammad Javad Rouhanifar (D.V.M)

## license

source code and all sample images are distributed under GPLv3 (GNU General Public License version 3) license.

> Written with [StackEdit](https://stackedit.io/).
