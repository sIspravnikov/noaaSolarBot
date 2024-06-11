import os
# import imageio
# from tqdm import tqdm
from natsort import natsorted
import moviepy.video.io.ImageSequenceClip

class Render:

    def __init__(self, paths: dict) -> None:
        self.paths = {}
        for key,value in paths.items():
            self.paths[key] = (os.path.join(os.getcwd(), value))

    # def gif(self, outputgif: str) -> None:
    #     with imageio.get_writer(outputgif, mode='I') as writer:
    #         for filename in tqdm(natsorted(os.listdir(self.paths['frames'])), desc = "Building gif"):
    #             image = imageio.imread(f"{self.paths['frames']}/{filename}")
    #             writer.append_data(image)

    def mp4(self, outputvideo: str, fps: int) -> str:
        image_files = []
        try:
            for filename in natsorted(os.listdir(self.paths['frames'])):
                image_files.append(os.path.join(self.paths['frames'], filename))
            clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
            clip.write_videofile(outputvideo)
        except Exception:
            return None
        else:
            return True
        
    def remove(self, outputvideo: str) -> None:
        if os.path.exists(outputvideo):
            os.remove(outputvideo)