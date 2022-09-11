# Punch Quest
A fitness application for traditional & thai boxing that helps individuals work on their punching combinations and body movement.

## Contributers
Bharat Krishnan
Jai Narayanan
Austin Brown

## Overview
This application utilizes real-time action-recognition.  It does this through the use of 3D pose estimation, a methodology by which a computer can infer the 3D coordinates of 32 key joints from a single frame.  

On our home page, we hope to have a demo where users can visualize how the application works and what is to be used for.  After completing it, users will be prompted to make a free account using GoogleOAuth 2.0.  With a personal account, users can take full advantage of the features offered below:

> We want this application to help individuals work on key punch in the form of learning modules.  For example, learning ***jab, cross, left uppercut*** would be learning module for users, where they are required to complete the combination 50 times to finish it.  

>  We will also have modules for body movement & footwork such as slips, weaves, and sliding left/right.  In addition, we hope to add a fun reaction-time game where users will 'face off' against a CPU character that will through punches that require specific dodge movements and counters.  This will help people visualize what a real opponent might do in a fight.

Long term, we hope to have a premium accounts with the following features below:

> Sparring analysis, analyzes a video of a spar and provides feedback on combos that land, good counters, and vulnerabilities

> We also will have customizable modules where users can add their own combinations and how many times they want to complete them.

## Context
We (Bharat, Jai, and Austin) are all majoring in Computer Science but  also practitioners of Thai Boxing.  We have realized that when training, its not always a given that you have a partner to train with, and training alone is not very constructive.  You have nobody to give you feedback, you have no one to hold you accountable, and you dont have a regimented schedule.  Most existing boxing apps only attempt to solve the last problem, but because they are not interactive, users are often not sure if they are moving correctly and lose motivation from seeing them all the way through.  We hope that our application can help inviduals engage in solo boxing training to the fullest, as their each and every movement is recongized by the application and acknowledged.  

## Non-goals
As of now, some of our non-goals include
> - We will not be able to indicate how good a punch or movement is
> - We will not be able to train in extremely different angles ( it is prefered the user faces the camera)
> - We cannot use this application with multiple people,  it only works for one person

## Proposed Solution

The proposed solution will be a fullstack fitness application.  

The ML model will be able to identify boxing puches and body/footwork.  The home page will include a demo of the ML model and its basic applications in a tutorial of sense.  After completing the tutorial, users will be prompted to make an account using their gmail for advanced features.  

Among these features will be training modules for practicing combos and advanced footwork, customizable modules for training custom combos, psuedo spar to test dodge reaction time.

### ML

The ML development will be entirely written in python

**Dependencies**: 
`openCV, mediapipe, scikit-learn, Tensorflow`

**Mechanism for Data Collection**
openCV will be used for the sake of collecting data from videos and live camera footage.  From here we will utilize mediapipes 1 person 3D pose estimation model and get 32 key point coordinates for a persons body.  An action will be considered 30 frames of collected body coordinates.  As a result our training data for punches and movements will be a large array of how many ever pieces of training data we plan to use made up of arrays of size 30(frames) by 32(keypoints)*3(x,y,z coords)

**Data Collection Procedure**
We will take 100 videos of people making every key movement we plan to record 
> - guarding
> - move left, move right, move back, move forward
> - slip left, slip right
> - weave left, weave right
> - jab, cross
> - left hook, right hook
> - left uppercut, right upercut
> - left roundhouse kick, right roundhouse kick
> - left teep, right teep

From here, we will run these videos through the mechanism for collecting key body coordinates.  These coordinate arrays will be stored in the form of numpy arrays stored in a data folder

**Training procedure**
Using scikit-learn's test train split we will save 5 percent of all videos for the sake of testing if our model can make accurate predictions.  The rest of the data will be labelled as what action they represent and then they will be passed into a 4 layer Neural Network using Tensorflow.  After this we should receive a a final NN file.

**Testing procedure**
We will run the our test files through the trained model.  We will then attempt to test if it works for live video as well

### Server


### Frontend


## Alternative Solutions

## Testing

## Open Questions

## Detailed Timeline
