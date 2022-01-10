from enum import Enum


class ExecutionSpace(Enum):
    Cuda = "Cuda"
    HIP = "HIP"
    OpenMP = "OpenMP"
    Pthreads = "Pthreads"
    Serial = "Serial"
    Debug = "Debug"
    Default = "Default"
