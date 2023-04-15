import launch

if not launch.is_installed("ffmpeg-python"):
    launch.run_pip("install ffmpeg-python", "requirements for TemporalKit extension")

if not launch.is_installed("moviepy"):
    launch.run_pip("install moviepy", "requirements for TemporalKit extension")

if not launch.is_installed("tensorflow"):
    launch.run_pip("install tensorflow", "requirements for TemporalKit extension")

if not launch.is_installed("imageio_ffmpeg"):
    launch.run_pip("install imageio_ffmpeg", "requirements for TemporalKit extension")
