import platform

from data.constants import (
    EXIFTOOL_PATH, EXIFTOOL_FOLDER_PATH, EXIFTOOL_BIN_NAME,
    IMAGE_MAGICK_PATH,
    CJXL_PATH,
    DJXL_PATH,
    AVIFENC_PATH,
    AVIFDEC_PATH,
    OXIPNG_PATH
)
from core.process import runProcess
from core.exceptions import GenericException

def _runExifTool(*args):
    """For internal use only."""
    if platform.system() == "Windows":
        runProcess(EXIFTOOL_PATH, *args)
    elif platform.system() == "Linux":  # Relative path needed for Brotli dependency to work on Linux
        runProcess("./" + EXIFTOOL_BIN_NAME, *args, cwd=EXIFTOOL_FOLDER_PATH)

def copyMetadata(src, dst):
    """Copy all metadata from one file onto another."""
    _runExifTool('-tagsfromfile', src, '-overwrite_original', dst)

def deleteMetadata(dst):
    """Delete all metadata except color profile from a file."""
    _runExifTool("-all=", "--icc_profile:all", "-tagsFromFile", "@", "-ColorSpace", "-overwrite_original", dst)

def deleteMetadataUnsafe(dst):
    """Delete every last bit of metadata, even color profile. May mess up an image. Potentially destructive."""
    _runExifTool("-all=", "-overwrite_original", dst)

def runExifTool(src, dst, mode):
    """ExifTool wrapper."""
    match mode:
        case "ExifTool - Safe Wipe":
            deleteMetadata(dst)
        case "ExifTool - Preserve":
            copyMetadata(src, dst)
        case "ExifTool - Unsafe Wipe":
            deleteMetadataUnsafe(dst)

def getArgs(encoder, mode) -> []:
    """Return metadata arguments for the specified encoder.

    Example Usage:
        args = []
        args.extend(getArgs(encoder, mode))
    """
    match mode:
        case "Encoder - Wipe":
            if encoder == CJXL_PATH:
                return []
                # return ["-x strip=exif", "-x strip=xmp", "-x strip=jumbf"]    
                # return ["-x exif=", "-x xmp=", "-x jumbf="]
            elif encoder in (DJXL_PATH, AVIFDEC_PATH):
                return []
            elif encoder == IMAGE_MAGICK_PATH:
                return ["-strip"]
            elif encoder == AVIFENC_PATH:
                return  ["--ignore-exif", "--ignore-xmp"]
            elif encoder == OXIPNG_PATH:
                return ["--strip safe"]
            else:
                raise GenericException("M0", f"[Metadata - getArgs()] Unrecognized encoder ({encoder})")
        case "Encoder - Preserve":
            return []   # Encoders preserve metadata by default
        case _:
            return []