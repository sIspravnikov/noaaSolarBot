import os
import imageio
from natsort import natsorted
import moviepy.video.io.ImageSequenceClip

class Render:

    def __init__(self, paths: dict) -> None:
        self.paths = {}
        for key,value in paths.items():
            self.paths[key] = (os.path.join(os.getcwd(), value))

    def gif(self, outputgif: str) -> None:
        with imageio.get_writer(outputgif, mode='I') as writer:
            for filename in natsorted(os.listdir(self.paths['frames'])):
                print(f"adding frame: {filename}")
                image = imageio.imread(f"{self.paths['frames']}/{filename}")
                writer.append_data(image)

    def mp4(self, outputvideo: str, fps: int) -> None:
        image_files = []
        for filename in natsorted(os.listdir(self.paths['frames'])):
            image_files.append(os.path.join(self.paths['frames'], filename))
        clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
        clip.write_videofile(outputvideo)