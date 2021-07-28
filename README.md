## Analysis and Mining on Music Evolution and Influence through Network Science and Machine Learning


### Executive summary
By utilizing the data sets of musical characteristics and links between music influencers and followers, we aim to build a model that measures musical influence. First, we will analyze the influencer-follower relations by looking at the network of musical influence, observing the correlation between followers and influencers, and closely examining several subnetworks extracted from the entire network. Second, we will propose measures quantify the similarities within and between musical genres, using the musical characteristics, such as danceability, energy, valence, etc. in order to measure the influence between artists, and find the more influential characteristics. Finally, we will apply our model on the whole timeline to analyze the evolutions and revolutions of music through time, with the goal to reveal the relation between music and culture, society, politics, and technologies.


### Code
All codes are written in `python3`.
* `Measure_Musical_Influence_Model`: A model that measures musical influence. It can discover the characteristics of the artist network such as small world effect and scale-free network. The efficient t-SNE dimensionality reduction algorithm is used before the cluster analysis of artists. Innovatively combines Jaccard similarity coefficient and cluster analysis to measure similarity. Innovatively combines community detection algorithm and machine learning method to find more contagious characteristics. It can keenly discoverconnotation of the music revolution and used anomaly detection and key node detection to find the revolutionary artists.


### Data
The dataset used in our case study can be found in the folder `./data/.`
* `data_by_artist`: Based on full_music_data.csv, summarizing the mean values of musical features for each artist.
* `data_by_year`: Based on full_music_data.csv, summarizing the mean values of musical features for each year from 1921 to 2020.
* `full_music_data`: This file includes 98,340 songs and their artist_name, artist_id and some musical features. artist_id is the same unique indentification number given in the influence_data.csv file.
* `influence_data`: This file contains musical influencers and followers for 5,854 artists in the last 90 years, which are reported by artists themselves and the opinion of industry experts. Data is encoded in utf-8 to ensure that all characters could be handled correctly.



### Figures
The results figures are stored in the folder `./Figures/.`
* `Figure1.png`:
* `Figure2.png`:
* `Figure3.png`:
* `Figure4.png`:
* `Figure5.png`:
* `Figure6.png`:
* `Figure7.png`:
* `Figure8.png`:
* `Figure9.png`:
* `Figure10.png`:
* `Figure11.png`:
* `Figure12.png`:
* `Figure13.png`:
* `Figure14.png`:
* `Figure15.png`:
* `Figure16.png`:
* `Figure17.png`:
* `Figure18.png`:
* `Figure19.png`:
* `Figure20.png`:
* `Figure21.png`:


### Tables
The results tables are stored in the folder `./Tables/.`
* `Table1.png`:
* `Table2.png`:
* `Table3.png`:
* `Table4.png`:
