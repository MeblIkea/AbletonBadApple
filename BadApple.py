from __future__ import with_statement

import random
import time

import Live
import threading
from _Framework.ControlSurface import ControlSurface

def messing(tracks):
    while True:
        for clips in tracks:
            for clip in clips:
                try:
                    clip.color_index = random.randint(20, 50)
                except Exception:
                    pass
        time.sleep(0.01)
    Live.Base.log(f"Threading! {colors}")

class BadApple(ControlSurface):
    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        Live.Base.log("Challenge ready!")
        self.checkIfReady()
        song = Live.Application.get_application().get_document()
        clips = []
        w = 16
        h = 9
        for _ in range(h-8):
            song.create_scene(0)
        for i in range(w):
            track = song.create_midi_track(0)
            clip_list = []
            clips.append(clip_list)
            for clip_slot in track.clip_slots:
                clip_slot.create_clip(1)
                clip_slot.clip.color_index = 69
                clip_list.append(clip_slot.clip)
                Live.Base.log(f"Challenge ready! {clip_slot.clip._live_ptr}")

        for _ in range(4):
            song.delete_track(w)
        threading.Thread(target=messing, args=(clips,)).start()

        #for ret in song.return_tracks:
        #    song.delete_return_track(ret)


    @staticmethod
    def checkIfReady():
        Live.Base.log(Live.Application.get_application().get_document().master_track.name)
