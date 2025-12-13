from __future__ import with_statement
from .badapple_frames import FRAMES
import time

import Live
import threading

from _Framework.ControlSurface import ControlSurface

FPS = 15
W = 64
H = 36


def messing(tracks):
    start_time = time.time()
    for i in range(len(FRAMES)):
        frame = FRAMES[i]
        start_time += 1 / FPS
        for x, clips in enumerate(tracks):
            for y, clip in enumerate(clips):
                try:
                    if frame[x + y * W] != clip.color_index:
                        clip.color_index = frame[x + y * W]
                except Exception:
                    pass
        if time.time() < start_time:
            time.sleep(1 / FPS)
    Live.Base.log(f"Threading!")


class BadApple(ControlSurface):
    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)

        self.frames = []
        Live.Base.log(f"Challenge ready with {len(FRAMES)} frames")
        self.tracks = []
        song = Live.Application.get_application().get_document()

        self.setup_set()
        t = threading.Thread(target=messing, args=(self.tracks,))
        song.add_loop_listener(lambda: t.start())

    def setup_set(self):
        song = Live.Application.get_application().get_document()
        for _ in range(H - 8):
            song.create_scene(0)
        for i in range(W):
            track = song.create_midi_track(0)
            clip_list = []
            self.tracks.append(clip_list)
            for clip_slot in track.clip_slots:
                clip_slot.create_clip(1)
                clip_slot.clip.color_index = 69
                clip_list.append(clip_slot.clip)

        self.tracks.reverse()
        for _ in range(4):
            song.delete_track(W)
