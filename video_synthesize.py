import cv2
import numpy as np
import os
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_audioclips


def images_to_video(image_dir, output_file, fps, frame_repeat):
    if os.path.exists(image_dir):
        pass
    else:
        os.mkdir(image_dir)
    images = sorted([img for img in os.listdir(image_dir) if img.endswith(".jpg")])
    frame = cv2.imread(os.path.join(image_dir, images[0]))
    height, width, layers = frame.shape
    video = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width,height))
    for image in images:
        frame = cv2.imread(os.path.join(image_dir, image))
        for _ in range(frame_repeat):
            video.write(frame)
    video.release()



def add_audio_to_video(video_file, audio_file, output_file):
    # Load video and audio
    video = VideoFileClip(video_file)
    audio = AudioFileClip(audio_file)

    # If the video is longer than the audio, loop the audio
    if video.duration > audio.duration:
        loop_times = video.duration // audio.duration + 1
        audio_clips = [audio] * int(loop_times)
        concatenated_audio = concatenate_audioclips(audio_clips)
        audio = concatenated_audio.subclip(0, video.duration)

    # If the audio is longer than the video, trim the audio
    elif audio.duration > video.duration:
        audio = audio.subclip(0, video.duration)

    # Add audio to video
    video_with_audio = video.set_audio(audio)

    # Save to file
    video_with_audio.write_videofile(output_file, codec='libx264')


topic = "ME"
# Call the function:
# image_dir is the path to your images
# output_file is the name of the output video file
# fps is the frames per second for the video
# frame_repeat is the number of frames each image will be repeated
images_to_video(f'{topic}/subtitles', f"{topic}/output.mp4", 1, 2)
add_audio_to_video(f'{topic}/output.mp4', 'BGM.mp3', f'{topic}/output_BGM.mp4')
