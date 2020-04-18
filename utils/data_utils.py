import sys,os
sys.path.append(os.path.dirname(__file__) + os.sep + '../')
# sys.path.append("..")
from yolo3_deepsort.deep_sort.track import MotionState,SecurityState

class Camera:
    """
    储存相机数据
    """
    _defaults = {
        "XYZ":[0,0,0],
        "direction":0,
        "velocity":0,
        "curve":0,
        "acceleration": 0,
        "motion_state": MotionState.Pending,
    }
    def __init__(self,**kwargs):
        self.__dict__.update(self._defaults)
        self.__dict__.update(kwargs)

def load_frametime(filepath):
    '''
    读取"20191022_022500_time.txt"文件
    =============
    parameters:
        filepath: string
    =============
    return:
        frame_time: list
    '''
    frame_time = []
    with open(filepath) as f:
        line = f.readline().strip()
        while line:
            line = f.readline().strip()
            if len(line) ==0:
                break
            frame_time.append(float(line))
    return frame_time

def load_fuseddata(filepath):
    '''
    读取"fused_pose_planePoint_1022_022500.txt"文件
    =============
    parameters:
        filepath: string
    =============
    return:
        fused_data: dict with values(list)
            { time: ms
              x,y,z: coordinate(m)
              yaw,roll,pitch: pose(rad)
              speed: m/s
              infer_duration:
              infer_method:
              trace_type:
            }
    '''
    with open(filepath) as f:
        fused_data = { "time":[],"x":[],"y":[],"z":[],
               "yaw":[],"roll":[],"pitch":[],"speed":[],
               "infer_duration":[],"infer_method":[],
               "trace_type":[]}
        line = f.readline().strip()
        pre_time = -1
        while line:
            line = f.readline().strip()
            if len(line) ==0:
                break
            info = line.split(",",10)

            cur_time = float(info[0])
            if pre_time == cur_time:
                continue
            fused_data["time"].append(float(info[0]))
            fused_data["x"].append(float(info[1]))
            fused_data["y"].append(float(info[2]))
            fused_data["z"].append(float(info[3]))

            fused_data["yaw"].append(float(info[4]))
            fused_data["roll"].append(float(info[5]))
            fused_data["pitch"].append(float(info[6]))
            fused_data["speed"].append(float(info[7]))

            fused_data["infer_duration"].append(float(info[8]))
            fused_data["infer_method"].append(float(info[9]))
            fused_data["trace_type"].append(float(info[10]))
            pre_time = cur_time

    return fused_data