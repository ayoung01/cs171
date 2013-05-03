CS171 Project 3 - 5/2/13
Kevin Sun and Albert Young
-------------------------------------
Visualizing U.S. Foreign Trade Data

1. How do we run your code?
To run the visualization, simply open index.html in your web browser.  We recommend Google Chrome.  If you would like to run the python parsing applications, simply run the appropriate .py files in the /python directory.

2. Which parts of your code are responsible for what?
Index.html contains virtually all of the code used in the visualization, from drawing the map, displaying data, to animating the lines.  The scripts in the /python directory were used in processing data, parsing it from csv to JSON form.  In index.html, event handlers are attached to most UI elements (such as the slider and radio buttons).  The UI elements then call methods used in visualization with changed parameters. The visualization in index.html is powered through a long string of javascript executed when the document is ready, and contains the following key methods:

    - Helper Functions
    These functions perform tasks related to the slider and legend and have self-explanatory features: getcurrData getcurrentYear getcurrentMonth getcurrentMonthname updateflowtypeString updateColors updateLegend getCountryName.
 
   - .vectorMap()
    This constructor creates a vectorMap object in the jVectorMap library; its arguments specify colorscales and custom functions that are called for tooltip/panning/zooming.
    Arguments to this constructor include onViewportChange, onRegionSelected, onRegionOut, onRegionOver, and onRegionLabelShow, which all contain methods that are defined to suit our visualization.

    - togglecountry(e, code, isSelected, selectedarray)
    This method is called when a country is selected; it updates a global variable keeping track of the current country and redraws the map.

    -  changeType(typechng)
    This method calls all appropriate methods to chagne the data type being visualized; central to linking control.

    - playSlider() / playSliderfast() / playSliderreverse()
    These methods support the playing functionality of the visualization, which is acheived by using the boolean flag isPlay.  In addition, these methods recursively call themselves with setTimeout to continue the playing proccess. 

    - drawBarChart(container) 
    This method draws all the bar charts on the screen based on the time.

    - drawLineChart(container)
    Method which draws the pie charts based on the  time and appropriate radio button.

    - generateTableData() 
    Method which generates the table data to be visualized.

3. Which parts are libraries and are they hosted in the folder or externally online?
For our project we used several libraries: Boostrap, Bootstro.js, d3.js, jQuery, jQuery Animated Table Sorter, jQuery UI, jvectorMap, NVD3.js, and PrettyPhoto. All libraries are hosted in the folder, several of which were modified to fit the needs of our visualization.  For more details [and appropriate citations] on the libraries, see below. 

4. What data files are you using and how are they being fed into the code?
We do not use any data files in our implementation,we instead chose to ‘hardcode’ the data in JSON formats in the actual index.html file. This data was originally downloaded in Excel format form oecd.org and converted to JSON format using a Python script (located in /python). The data is encoded in <textarea> elements which are hidden from view by CSS. These textareas are all parsed into javascript variables using JSON.parse.

5. Any other information we need to understand your code.
None.  Our code is primarily all located in index.html. However, we also did modify the jVectorMaps library to change numeric scale and assign an ID to the SVG container of the map.  While we did comment the code, it may be useful to refer to the method description in the README for understanding.

List of Major Files and Directories
------------------------------------
Name                                            Content
ksun_ayoung_project_3_processbook.pdf           The project's processbook.  Findings are also included inside.  You should read this.
index.html                                      Our visualization. You should open and view this.
README.txt                                      (this)
/css                                            Contains style.css, used to style index.html.
/js                                             Contains the jVectorMap/jQuery/etc libraries (see below)
/data                                           Data downloaded and retrieved in excel/csv format, not directly visualized.
/python                                         Contains Python script used to convert data files to json objects embedded in index.html

List of Libraries Used
----------------------
-Boostrap (Otto, Mike; 2013). Used for Bootstro.js functionality under the CC BY 3.0 license. Accessed on 4/29/2013 at http://twitter.github.io/bootstrap/.

-Bootstro.js (Tran, Steve; 2013). Used for visualization 'demo.' under the MIT license. Accessed on 4/29/2013 at https://github.com/clu3/bootstro.js/blob/master/README.md.

-d3.js (Bostock, Mike; 2013). Used for NVD3.js functionality under the BSD license. Accessed on 4/5/2013 at http://d3js.org/.

-jQuery (Resig, John; 2013). Used for general assistance, jQuery UI/ATS functionality under the MIT license. Accessed on 4/1/2013 at http://jquery.com/.

-jQuery Animated Table Sorter (Hershberg, Matan; 2012). Used for table animations and sorting under the MIT license. Accessed on 4/28/2013 at www.matanhershberg.com/plugins/jquery-animated-table-sorter/‎.

-jQuery UI (González, Scott; 2013). Used for slider and radio buttons under the MIT license. Accessed on 4/4/2013 at http://jqueryui.com/.

-jvectorMap (Lebedev, Kirill; 2012). Used for map view under the MIT license. Accessed on 4/1/2013 at http://jvectormap.com/.

-NVD3.js (Novus Partners; 2012). Used for line and bar charts under the CC-wiki license. Accessed on 4/30/2013 at http://nvd3.org/.

-PrettyPhoto (Carone, Stephane ; 2012). Used for video overlay lightbox under the GPL v2 / CC 2.5 license. Accessed on 5/1/2013 at http://www.no-margin-for-errors.com/projects/prettyphoto-jquery-lightbox-clone/.


Summary
-------
Thanks for a wonderful class!
Please let us know if you have any questions/comments/concerns at ksun01@college.harvard.edu and ayoung@college.harvard.edu.
