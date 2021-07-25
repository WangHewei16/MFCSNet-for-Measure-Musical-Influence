## Code
* `./Figure Code/`: This folder contains Census model code which can produce the `Figure1.png` after running. It should run in vs2012 + pcl1.8.0 + boost environment.
* `./Table Code/`: This folder contains the test code in middlebury. It will produce the information data of the proposed algorithm in `Table1.png` and `Table2.png`. I use opencv 2.4.8, other versions should be OK but not too low.

## Data
* `./Data/`: This folder contains the data folder contains Tsukuba, Venus, Teddy and cones datasets from Middlebury official test datasets. The current directory images.xml is the input item, it will read the contents of the file. In the previous directory../sample/test_images, the image in the images directory is the input item and the name is the same as the name in images.xml correspondingly. The output results are saved in the result directory under the current directory.
* `./Data_extended/`: This folder contains 27 data sets from Middlebury official test datasets. 
