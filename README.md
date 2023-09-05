## MFCSNet: Musician-Follower Complex Social Network for Measuring Musical Influence


### Executive summary
By utilizing the data sets of musical characteristics and links between music influencers and followers, we aim to build a model that measures musical influence. First, we will analyze the influencer-follower relations by looking at the network of musical influence, observing the correlation between followers and influencers, and closely examining several subnetworks extracted from the entire network. Second, we will propose measures to quantify the similarities within and between musical genres, using musical characteristics, such as danceability, energy, valence, etc. in order to measure the influence between artists and find the more influential characteristics. Finally, we will apply our model to the whole timeline to analyze the evolutions and revolutions of music through time, with the goal of revealing the relationship between music and culture, society, politics, and technology.


### Data
The dataset used in our case study can be found in the folder `./Data/.`
* `data_by_artist.csv`: Based on full_music_data.csv, summarizing the mean values of musical features for each artist.
* `data_by_year.csv`: Based on full_music_data.csv, summarizing the mean values of musical features for each year from 1921 to 2020.
* `full_music_data.csv`: This file includes 98,340 songs and their artist_name, artist_id and some musical features. artist_id is the same unique identification number given in the influence_data.csv file.
* `influence_data.csv`: This file contains musical influencers and followers for 5,854 artists in the last 90 years, which are reported by artists themselves and the opinion of industry experts. Data is encoded in utf-8 to ensure that all characters can be handled correctly.


### Figures
The results figures are stored in the folder `./Figures/.`
* `Figure1.png`: The Network of Genre Influence. Each node represents a musician. Each directed edge represents a pair of influencer-followers.
* `Figure2.png`: The Network of New Age Music (left) and Jazz Music (right). 
* `Figure3.png`: Linear Regression to verify small-world effect (left) and Count of Follower (right). We take the logarithm of the number of nodes and perform a linear regression with the average distance, making this figure.
* `Figure4.png`: Power Law Distribution. We gain the number of followers and the number of nodes for each number of followers and plot in double logarithmic coordinates.
* `Figure5.png`: t-SNE of Cluster Result of Music Data. We use BIRCH clustering algorithm to cluster the data and visualize the result.
* `Figure6.png`: Heat Map of Genres and Characteristics. Each grid in the figure represents the normalized average value of the corresponding characteristics of the corresponding genre.
* `Figure7.png`: Visualization of Decision Tree. Using the decision tree, we can distinguish genres.
* `Figure8.png`: Time Series of Various Characteristics. This figure shows the changes in the characteristics of major genres between 1920 and 2020.
* `Figure9.png`: Heat Map of Jaccard Similarity Coefficient Between Genres. This figure reflects the similarity between genres.
* `Figure10.png`: Artists Network after Community Findings. We use Louvain algorithm to find the community and visualize the result.
* `Figure11.png`: Feature Importance. We use the LightGBM as a machine learning tool to find the differences between the various characteristics of music in their influence.
* `Figure12.png`: Network of Bob Dylan and Its Relative Artists. This figure shows artists that influenced Bob Dylan and others that followed him.
* `Figure13.png`: Visualization of Eigenvector Centrality. We can detect key nodes via eigenvector centrality.
* `Figure14.png`: Change of Pop/Rock Artist Network (1960----1980----2000). 
* `Figure15.png`: Time Series of Popularity.
* `Figure16.png`: Time Series of Number of Communities and Average Degree. We use community detection algorithm to obtain these results.
* `Figure17.png`: Time Series of Average Path Length and Average Cluster Coefficient between 1940 to 2020.
* `Figure18.png`: Average Danceability of Several Genres from 1925 to 1945. 
* `Figure19.png`: Release Counts of Several Genres from 1940 to 1945.
* `Figure20.png`: Average of Acousticness by Year.
* `Figure21.png`: The Boom of Pop/Rock Music (1950s-1960s-1980s). Yellow edge means that the follower is a Pop/Rock artist and blue is not. The yellow part gradually occupying the main stream illustrates the booming of Pop/Rock music. 


### Tables
The results tables are stored in the folder `./Tables/.`
* `Table1.png`: Average Distance and Number of Nodes (musicians) in the network of genre influence.
* `Table2.png`: The Result of Artist. This table shows the difference between Bob Dylan and his influncers in each musical feature.
* `Table3.png`: The Rank of Artist. Based on the anomalous value and eigenvector centrality of artists from Pop/Rock, we can find the order of preference by similarity to ideal situation (TOPSIS).
* `Table4.png`: Characteristics for Different Genres. We judge whether their music is revolutionary by comparing the feature values of some bands in Table 3 and the whole pop / rock music.
