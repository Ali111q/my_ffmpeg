from moviepy.video.io.VideoFileClip import VideoFileClip
import moviepy.video.fx.all as vfx

# Open the input video
clip = VideoFileClip('C:\\Users\\ali\\Downloads\\videoplayback.webm')

# Define the new size
new_width = 854
new_height = 480

# Resize the video
resized_clip = vfx.resize(clip, (new_width, new_height))

# Save the resized video to a new file
resized_clip.write_videofile('alij1.mp4', bitrate="400k")