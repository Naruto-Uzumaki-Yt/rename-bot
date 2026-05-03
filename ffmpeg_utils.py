# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

import ffmpeg
import os

def add_metadata(input_path, output_path, title="", author="", artist="", audio="", subtitle="", video=""):
    try:
        stream = ffmpeg.input(input_path)

        output_kwargs = {
            "vcodec": "copy",
            "acodec": "copy",
            "map_metadata": 0
        }

        stream = ffmpeg.output(stream, output_path, **output_kwargs)

        # Apply metadata correctly using global_args (proper ffmpeg method)
        if title:
            stream = stream.global_args("-metadata", f"title={title}")

        if author:
            stream = stream.global_args("-metadata", f"artist={author}")

        if artist:
            stream = stream.global_args("-metadata", f"album_artist={artist}")

        if audio:
            stream = stream.global_args("-metadata", f"comment={audio}")

        if subtitle:
            stream = stream.global_args("-metadata", f"subtitle={subtitle}")

        if video:
            stream = stream.global_args("-metadata", f"description={video}")

        ffmpeg.run(stream, overwrite_output=True, quiet=True)

        return output_path

    except Exception as e:
        print("FFmpeg Error:", e)
        return input_path

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
