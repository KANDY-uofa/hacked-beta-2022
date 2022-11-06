# Data Analysis on Vehicle Collision in Alberta
###### A project written at
#### HackED Beta 2022,
###### a 24-hour hackathon hosted by
#### University of Alberta Computer Engineering Club


## Our goal was to raise awareness on **road safety**, specifically in **Alberta**. 
#### To do so, we _compiled_ news data, _analyzed_ government-provided datasets, and _displayed_ them in a website. 
---
## Funtionality (C.A.D.)
- **C**ompiles information through web scraping
    - Scrapes news report data from a website whose approach is one of the most systematic and thorough in recording locations of collisions:
        - https://www.navbug.com/alberta_traffic.htm

- **A**nalyzes government data on car collisions through machine learning
    - Uses two training models (ARIMA and Prophet) to analyze trends and to predict future occurrences

- **D**isplays above data in a website

---
## Our noteworthy achievements 
- **Originality**: 
    - Currently, there is _no publicly accessible compiled information_ on car collision locations
    - Nobody else _analyzed the trends_ in car collisions using _machine learning_ 
- **Complexity**:
    - Quickly familiarized ourselves with techniques required to compile, analyze, and display data
        - Web scraping
        - Machine learning
        - Web designing
- **Execution** and **Polishness**
    - Completed the _working_ project within 24 hours
- **Utility**
    - Our project _raises awareness_ on road safety and can be extended to _encourage the government authorities to implement our system_ through showcasing its importance.

---
## Steps to run the program
- **Scraping website data**
    1. Move to "webscraping" directory
    2. To start the program and to create an output file, run:
    ```
    python3 web_scraper.py > scraped_data.txt
    ```

---
## Background information of contents
- "ARIMA_Prediction_Model" directory
- "Prophet_Prediction_Model" directory
- "dataset" directory
- "webscraping" directory contains files that scrape website data

---
## Team members:
* [Min Joh](https://github.com/CavityKingu)
* [Dohyun Kim](https://github.com/kdhminime)
* [Yongbin Kim](https://github.com/yongbin4) 
* [Jamie Lee](https://github.com/jamielee0629)
* [Taekwan Yoon](https://github.com/taekwan-yoon)

