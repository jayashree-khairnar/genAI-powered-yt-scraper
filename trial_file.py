import yt_dlp
import logging as console

console.basicConfig(level=console.INFO)

def list_streams(video_url):
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
        'logger': console
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            console.info(f"Attempting to fetch streams from URL: {video_url}")
            info_dict = ydl.extract_info(video_url, download=False)
            formats = info_dict.get('formats', [])
            if not formats:
                console.error("No streams found")
                return "No streams found"

            for f in formats:
                console.info(f"Format: {f}")

            return formats

    except Exception as e:
        console.error(f'Error while fetching streams: {e}')
        console.error(traceback.format_exc())
        return f"Error: {e}"

# Test URLs
video_url = 'https://www.youtube.com/watch?v=2d05lQRznp4'
streams = list_streams(video_url)
print(streams)

video_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
streams = list_streams(video_url)
print(streams)
