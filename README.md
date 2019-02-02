# Hassin حسّن

Having noticed that only a small percentage of Tunisian citizens pay their taxes towards the municipalities by analyzing the data provided by "marsad baladiyya", The goal of Hassin platform is to encourage the citizens to start paying the taxes (الجبايات). 

## Getting Started

The idea behind the platform is to state the facts that citizens are ignorant of, or choose to ignore about the taxes, and to show him concretely how much their municipalities can offer, if the required amount of taxes is paid.
The platform is specific to each municipality, meaning, a user can see the changes that the particular municipality he belongs to can accomplish, if the required amount of taxes is paid.

### Prerequisites

Python is needed to run this project, just open your command line/ terminal depending on the Operating System you're using, navigate to the directory where the project is placed using the cd command, and finally start a python server, using the command "python -m http.server"  or simply double click run.bat or run.sh depending on your OS, then open localhost:8000 in your browser.

### Installing

You only need to install python on your machine and add it to your environment variables to be able to run it from your command line/ terminal.

## Built With

* [Web] html, css, javascript
* [Bootstrap](https://getbootstrap.com/) - CSS/JS Framework: Open Source
* [JQuery](https://jquery.com/) - JS Framework: Open Source
* [Python](https://www.python.org/) - Parsing the GeoJSON format file.
* [D3JS](https://d3js.org/) - JS Plugin: Data visualizing with maps: Open source.
* [Photoshop](https://www.adobe.com/) - for creating the logo

## Contributing

Yessine Borchani, Ahmed Ben Neji, Kais Ben Daamech, Nadhem Maaloul

## Project Description:
The website contains multiple sections:<br/>
1- A greeting cover containing the logo...<br/>
2- List of facts such as the amount of taxes paid compared to the amount of investement of the municipality in the projects improving the situation of the region.<br/>
The previous sections were done using bootstrap.<br/>
3- An interactive map of Tunisia in which, clicking a state opens a popup, allowing the user to choose the municipality he wants. Upon choosing the municipality, another window pops up visualizing for him the data in terms of potential projects that can be performed in his regin such as building schools, building football stadiums (with football being by far the tunisian's most preferable sport).
This part was done using Python to parse the data, get conclusions, generate pie charts and D3JS to display the interactive map. 
