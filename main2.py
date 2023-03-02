import av

input_filename = './hh.mp4'
output_filename = 'eiufduiowehfuew.mp4'

input_container = av.open(input_filename)
input_stream = input_container.streams.video[0]
output_container = av.open(output_filename, mode='w')

output_stream = output_container.add_stream('h264', input_stream.rate)
output_stream.pix_fmt = input_stream.pix_fmt
output_stream.width = input_stream.width
output_stream.height = input_stream.height
output_stream.time_base = input_stream.time_base

for frame in input_container.decode(video=0):
    resized_frame = resize_frame(frame.to_ndarray(), (640, 480))
    output_stream.encode(resized_frame)

output_container.close()
