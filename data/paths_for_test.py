from pathlib import Path
class PathsForTest:
    home_dir = Path.home()
    base_dir = Path("pyton_projects/Sprint_9")
    filename1 = "1.jpg"
    filename2 = "2.jpg"
    full_path1 = home_dir/ base_dir / "assets" / filename1
    full_path2 = home_dir/ base_dir / "assets" / filename2