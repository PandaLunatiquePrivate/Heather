import enum


@enum.unique
class VideoEncodingFormat(enum.Enum):

    MP4 = 1
    GP3 = 2
    OGG = 3
    WMV = 4
    WEBM = 5
    FLV = 6
    AVI = 7
    QUICKTIME = 8
    HDV = 9
    MXF = 10
    MPEG_TS = 11
    MPEG2_PSTS = 12
    WAV = 13
    LXF = 14
    VOB = 15

@enum.unique
class VideoCodecs(enum.Enum):

    H_263 = 1
    H_264 = 2
    HEVC = 3
    MPEG4 = 4
    THEORA = 5
    GP3 = 6
    WINDOWS_MEDIA_8 = 7
    QUICKTIME = 8
    MPEG_4 = 9
    VP8 = 10
    VP6 = 11
    MPEG1 = 12
    MPEG2 = 13
    MPEG_TS = 14
    MPEG_4_2 = 15
    DNXHD = 16
    XDCAM = 17
    DVCPRO = 18
    XDCAM_IMX = 19
    JPEG_2000 = 20
    

@enum.unique
class AudioEncodingFormat(enum.Enum):

    MP3 = 1
    AAC = 2
    HE_AAC = 3
    AC3 = 4
    EAC3 = 5
    VORBIS = 6
    WMA = 7
    PCM = 8


@enum.unique
class ImageEncodingFormat(enum.Enum):

    TIFF = 1
    JPEG = 2
    GIF = 3
    PNG = 4


@enum.unique
class CaptionEncodingFormat(enum.Enum):

    WEBVTT = 1
    CEA_608 = 2
    CEA_708 = 3
    DFXP = 4
    SAMI = 5
    SCC = 6
    SRT = 7
    TTML = 8
    GPP3 = 9


@enum.unique
class FileType(enum.Enum):

    IMAGE = 1
    VIDEO = 2
    AUDIO = 3


class FileExtensions():

    IMAGE = ['png', 'jpg', 'jpeg']
    VIDEO = ['mp4', 'webm']
    AUDIO = ['mp3', 'wav', 'ogg']


    @staticmethod
    def is_supported(file):

        for vf in FileExtensions.IMAGE:
            
            if file.endswith(vf):

                return FileType.IMAGE

        for vf in FileExtensions.VIDEO:
            
            if file.endswith(vf):

                return FileType.VIDEO

        for vf in FileExtensions.AUDIO:
            
            if file.endswith(vf):

                return FileType.AUDIO

        return None