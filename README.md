<h1>Module python version of SpotiFLAC.</h1>
<h2>Arguments</h2>
<i>service {tidal,qobuz,deezer,amazon}</i><br>
Specify the music service to use for downloading FLAC files. Specify multiple services separated by spaces to try them in order. Default is 'tidal'.<br><br>
<i>filename-format {title_artist,artist_title,title_only}</i><br>
Specify the format for naming downloaded files. Default is 'title_artist'.<br><br>
<i>use-track-numbers</i><br>
Include track numbers in the filenames.<br><br>
<i>use-artist-subfolders</i><br>
Organize downloaded files into subfolders by artist.<br><br>
<i>use-album-subfolders</i><br>
Organize downloaded files into subfolders by album.<br><br>
<i>loop minutes</i><br>
Specify the duration in minutes to keep retrying downloads in case of failures. Default is 0 (no retries).<br>


<h3>Usage (as Module)</h3>

```bash
from spotiFLAC import SpotiFLAC

spotiflac(
    url,
    output_dir,
    services=["tidal", "deezer", "qobuz", "amazon"],
    filename_format="title_artist",
    use_track_numbers=False,
    use_artist_subfolders=False,
    use_album_subfolders=False,
    loop=None
)
```

<h3>Example (Module Usage)</h3>

```bash
from spotiFLAC import SpotiFLAC

spotiflac(
    url="https://open.spotify.com/album/xyz",
    output_dir="/path/to/output_dir",
    services=["tidal", "deezer"],
    filename_format="artist_title",
    use_track_numbers=True,
    use_artist_subfolders=True,
    use_album_subfolders=True,
    loop=120
)

```