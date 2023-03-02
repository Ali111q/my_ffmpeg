import av

# Open the input video
input_file = av.open('./hh.mp4')

# Define the new size
new_width = 854
new_height = 480

# Open the output file for writing
output_file = av.open('iejdieid.mp4', 'w')

# Find the video stream in the input file
video_stream = next(s for s in input_file.streams if s.type == 'video')

# Create a video stream in the output file with the new size
output_stream = output_file.add_stream(template=video_stream)
output_stream.width = new_width
output_stream.height = new_height

# Enable hardware acceleration for encoding
output_stream.codec_context.options['vprofile'] = 'high444'
output_stream.codec_context.options['vpre'] = 'slow'
output_stream.codec_context.options['crf'] = '23'
output_stream.codec_context.options['b:v'] = '2M'
output_stream.codec_context.options['look_ahead'] = '1'

# Iterate over the input frames, resize them, and write them to the output file
for packet in input_file.demux(video_stream):
    for frame in packet.decode():
        resized_frame = frame.reformat(width=new_width, height=new_height)
        output_stream.encode(resized_frame)

# Close the input and output files
input_file.close()
output_file.close()
