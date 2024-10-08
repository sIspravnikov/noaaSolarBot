import os
import imageio
from tqdm import tqdm
from natsort import natsorted
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip

class Render:

    def __init__(self, paths: dict, default_frames: int) -> None:
        self.paths = {}
        for key,value in paths.items():
            self.paths[key] = (os.path.join(os.getcwd(), value))
        self.default_frames = default_frames

    # def gif(self, outputgif: str) -> None:
    #     with imageio.get_writer(outputgif, mode='I') as writer:
    #         for filename in natsorted(os.listdir(self.paths['frames']))[-self.default_frames:]:
    #             image = imageio.imread(f"{self.paths['frames']}/{filename}")
    #             writer.append_data(image)

    async def mp4(self, outputvideo: str, fps: int) -> str:
        image_files = []
        try:
            for filename in natsorted(os.listdir(self.paths['frames']))[-self.default_frames:]:
                image_files.append(os.path.join(self.paths['frames'], filename))
            clip = ImageSequenceClip(image_files, fps=fps)
            clip.write_videofile(outputvideo)
        except Exception:
            return None
        else:
            clip.close()
            return True
        
    async def remove(self, outputvideo: str) -> None:
        if os.path.exists(outputvideo):
            os.remove(outputvideo)