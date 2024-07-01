# FC24_API
![Static Badge](https://img.shields.io/badge/Docker-red) 
![Static Badge](https://img.shields.io/badge/Streamlit-white)
![Static Badge](https://img.shields.io/badge/Python-cyan) 


# Streamlit-Github Page link
Paste the following link on your browzer to see the streamlit app.

[Link_to_streamlit](https://fc24appdocker-5blvjpdvkummkxpgwra9b2.streamlit.app/)


# Overview
Streamlit web app with FC24 male players for my nephews. Wraped in Docker image.

It has been used only FC24 male player, for memory purpose. 

The goal of this project is basically to create quickly an app for my nephews and more importantly **dockerise** it so they can use it on their own latop.


# Screenshots


![Diagram](./Streamlit_Docker.png?raw=true "Project")

# Tasks
- [x] Streamlit User friendly for kids interested in FC24 players.
- [x] Dockerise the project and push the image to Dockerhub.
- [x] Github Pages to be run on other laptops withhout the need to use Docker.




# Structure of the Repo
- .gitignore: files/folder to ignore during the pushes to the distant repo.
- fc??24.ipynb: Notebook for tests and drafts
- funct.py: functions that will be used in the main.py
- main.py: file to run for the streamlit web app.
- male_player.csv: csv files containing the players.
- requirement.txt: libraries used for this project




# Problematic to deal with?
During this project, different problematics were on the road.
- [x] Modular Script
      
   Small functions have been defined for each tasks instead of one massive one performing all tasks.

- [x] Wild format **VS** Long format data
  
  Conversion of wild data to long format with melt(). This allow to create radar graphs later on.


# Personal Conclusion

- It has been keep using **git, venv** in this project to feel more and more comfortable with those tools. 

- It has been tried to **create a clean script using multiple self made functions**. 

- **Interesting experience to struggle and deal with wide format data**, to convert them into long format to finally plot a **new type of graph (Radar graph)**.

- In Future projects the focus will be on **writting a clean jupyter notebook** and not only a clean main.py but also paying more attention on github pushes writting more explicits comments, maybe limiting my numbers of pushes.









