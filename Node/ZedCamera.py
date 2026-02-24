# ZedNode

import os
import numpy as np
import pyzed.sl as sl
from cv2 import VideoCapture
from cv2.typing import MatLike  # A matrix
from Utility import TimeUtil as tu


class ZedCamera:
    def __init__(self, inputDirectory: str | None = None) -> None:
        """
        :description: creates an object and a place where the data is.
        :param inputDirectory: the folder where images resides
        """

        self.inputDirectory: str | None = inputDirectory
        self.depthCapture: VideoCapture | None = None  # gets depth reader of zed
        self.imageCapture: VideoCapture | None = None  # get image reader of zed

        self.image: MatLike | None = None  # stores pixel's color in a matrix
        self.imageTimeStamp: str | None = None

        # Cannot find directory
        if inputDirectory is None:
            cameraParams: dict = dict(
                camera_resolution=sl.RESOLUTION.RESOLUTION_HD720,
                depth_mode=sl.DEPTH_MODE.DEPTH_MODE_MEDIUM,
                coordinate_units=sl.UNIT.UNIT_METER,
                camera_fps=10,
                camera_buffer_count_linux=1
            )
            pass

        pass
