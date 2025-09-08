<p align="center">
   <img src="https://i.ibb.co/8gsGZ9x9/20250903-0334-remix-01k46ft3hhf4dv826ckv8nnxnx.png" alt="YouTube Explorer">
</p>
<p align="center">
   <img src="https://img.shields.io/badge/Code_Editor-VS%20Code-blue" alt="Code Editor VS Code">
   <img src="https://img.shields.io/badge/Version-Pre--Release-red" alt="Version Pre-Release">
   <img src="https://img.shields.io/badge/License-MIT-green" alt="License MIT">
</p>

# (Console Beta vesion)  

YouTube Explorer is an unofficial tool for searching, filtering, and displaying comments from YouTube videos by keywords using the YouTube Data API v3.  

## Important clarification!!!  

The .exe file is in releases. This `.exe` file does not have viruses. It was created for convenience. I made this file thanks to `python -m PyInstaller --strip --icon="../Icon/IconYE.ico" YouTubeExplorer.py`. If you do not trust the `.exe` file, I recommend you to use the `.py` file in `Sources`.

## Table of Contents  

- [What do you have to use YouTube Explorer?](#what-do-you-have-to-use-youtube-explorer)
- [Now the program provides:](#-now-the-program-provides)
- [Functionality](#%EF%B8%8F-functionality)
- [How to get the YouTube API key?](#-how-to-get-the-youtube-api-key)
- [What do I plan to make in the future?](#-what-do-i-plan-to-make-in-the-future)


## What do you need to use YouTube Explorer?  
1. The YouTube API key.
2. The video URL.
3. Your desire to use **YouTube Explorer**.

## `Key.py` provides:
- Creating the `Key.bin` file in the folder.

##

## 📌 The Comment Explorer provides  
- To receive the list of comments from YouTube videos in the console.
- To filter comments by keyword.
- To sort `by time` or `by relevance`.
- to limit the number of output results.
- To find out the channel's name where the video is hosted.
- Uninterrupted operation of this extention.

## The Video Explorer provides:
- Search videos by your prompt.
- You must enter your region.
- You can enter certain date of videos' releases; you can also enter a duration of videos.
- After exploring videos you should enter how many videos you want to receive.
- For one video you will receive information block. The title of the video, a link, views, likes, dislikes, amount of comments. Also the date, the channel and its YouTube link.
- Uninterrupted operation of this extention.


## ⚙️ Functionality
- **The API key** from Google Cloud Console (YouTube Data API v3) is being analyzed. If there is an error, it will ask you to enter it again.
- the `video id`, which is required for the YouTube Data API, is extracted from the **YouTube video URL**.
- **Keywords (optional)** — to filter comments. YouTube Explorer will search for comments on these keywords. YouTube Data API will not help it.
- **The sorting method** is `by relevance` or `by time`. If you press Enter, `by relevance` will be entered.
- **Number of comments** — output is limited at the user's request.

## ❓ How to get the YouTube API key?  
1. You need to follow the link: https://console.cloud.google.com.

2. You need to register for a Google account or log in to it.
   
3. Next, you press the `Create or select a project` button in the center of the page → `New project`

4. Next, you write the project name (Google can **automatically** specify the name, you do not have to write this name if you want) → If you do not have an organisation, just do not touch the `Location` item. → Press `Create`.
   
5. Without leaving the site, you need to press `Select project` and choose your project. You write to the search engine: **YouTube Data API v3** → `Enable`
    
6. You will be redirected to the API configuration. In the left column, you should press `Credentials`.
    
7. At the top, click `Create credentials` → `API key`.
    
8. The end of the way! Just copy your API key and paste it into the Windows notepad or somewhere else.

## 🔧 What do I plan to make in the future?  
1. Add exception handling.
2. The ability to save received comments.
3. Search for videos and explore the channels.
