import zipfile
import pathlib as pl


def make_archive(filepaths, dest_dir):
    dest_path = pl.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pl.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


if __name__ == "__main__":
    make_archive(filepaths=[''], dest_dir="dest")
