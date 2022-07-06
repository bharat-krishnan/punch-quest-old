# combat.ai

# Purpose
Given a video of two people sparring or one person training, this application will

1. First, track their movements and categorize them according to what they are
2. Second, provide analytics on the success of a fighter's movements and also informing them of their vulnerabilities
3. Making a web application with a easy to use UI/UX to display the video analysis

# Data For Modelling

Each action will be trained through a collection of arrays of size (30,17*3)
These arrays will be derived from a 30 frame video, where each frame records 17 key points in the body, with each point having 3 coordinates, namely(x,y,z)
It is our goal to indentify the following actions: stances (orthodox, southpaw, philly shell, peek a boo, clinch) jab, cross, left hook, right hook, left uppercut, right upercut

# First Task

1. Install correct dependencies for posture tracking
2. Successfully pinpoint coordinates of the key 17 points of all people in the video
3. Draw the edges that connect these points to display skeleton of the individuals
4. Collect 100 videos (30 frames) of jab, cross, guard to start off with
5. Collect the data from each of these videos in the form of a (30,51) array -> end up with 100 (30,51) arrays for each action so 300 data points to train model
- Reserve 15 videos, 5 in each to test if the prediction is working
6. Install dependencies for the model (scikit learn, tensorhub)
7. Figure out how to structure the nodes and layers of the deep learning model
8. Train model 
9. Test model
10. Build quick UI for us to verify it is working in the video
11. Repeat Everything until we recognize that all of the moves are well trained and acurate




