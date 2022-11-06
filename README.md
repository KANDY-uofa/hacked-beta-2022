# Data Analysis on Vehicle Collision
##### A project written at
### HackED Beta 2022,
##### a 24-hour hackathon hosted by
### University of Alberta Computer Engineering Club


Our underlying goal was to raise awareness on road safety, especially in Alberta, Canada. To do so, we compiled relevant data for wider public accessibility, analyzed government-provided data sets to illustrate a trend in car collisions, and displayed aforementioned data through various displaying techniques. 
---
## Funtionality
- Compiles information through web scraping
    - Scrapes news report data from the following website whose approach is one of the most systematic and thorough in recording locations of car collision:
        - https://www.navbug.com/alberta_traffic.htm

- Analyzes government-provided data through machine learning
    - Uses two training models (ARIMA and Prophet) to analyze the trend and to predict the number of collisions

- Displays above data through displaying techniques on website

---
## Our noteworthy achievements 
- Quickly familiarized ourselves with techniques required to compile, analyze, and display data (i.e., **machine learning**, **web scraping**, and **designing websites**)
- Completed the working project within 24 hours

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
* [Takewan Yoon](https://github.com/taekwan-yoon)

