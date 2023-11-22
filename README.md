# Youtube-Data-Analysis-
Analysis of selected data from the youtube using google API key

This Python script uses the YouTube Data API to fetch statistics about specific YouTube channels and their videos. Here's a brief explanation:

1. **Install Necessary Packages:**
   - It starts by installing and upgrading the required packages (`google-api-python-client`, `pandas`, `seaborn`).

2. **Set Up API Key:**
   - It sets up the YouTube Data API key.

3. **Channel Statistics:**
   - It defines a function (`get_channel_stats`) to retrieve statistics (such as subscribers, views, total videos) for a list of YouTube channels.

4. **Convert Data Types:**
   - It converts the data types of certain columns in the channel statistics DataFrame (`channels_data`) to numeric types for visualization.

5. **Visualize Channel Statistics:**
   - It uses `seaborn` to create bar plots for subscribers, views, and total videos of each channel.

6. **Get Video IDs from a Playlist:**
   - It defines a function (`get_video_ids`) to retrieve video IDs from a specified playlist.

7. **Get Video Details:**
   - It defines a function (`get_video_details`) to fetch details (title, published date, views, likes, comments) for a list of video IDs.

8. **Convert Video Data Types:**
   - It converts the data types of certain columns in the video details DataFrame (`video_data`) to numeric types and datetime objects.

9. **Visualize Top 10 Videos:**
   - It uses `seaborn` to create a bar plot for the top 10 videos based on views.

10. **Visualize Videos Published per Month:**
    - It creates a bar plot to show the number of videos published per month.

11. **Export Data:**
    - It exports the video details DataFrame to a CSV file (`Video_Details(Naa Anveshana).csv`).

Note: To run this script, you need to set up a Google Cloud Platform project, enable the YouTube Data API v3, and obtain an API key. Additionally, ensure that the required Python packages are installed.
