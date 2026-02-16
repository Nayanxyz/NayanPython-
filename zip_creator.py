import zipfile as zp                                            #zipfile library for zip
import pathlib as pl                                           #pathlib library for destination

def make_archive(filepaths , dest_dir):
    dest_path = pl.Path(dest_dir, "compressed.zip")        #Path method shows path to directories and compressed zrip its name
    with zp.ZipFile(dest_path, 'w') as archive:            #ZipFile method to save as zip
        for filepath in filepaths:
            filepath = pl.Path(filepath)
            archive.write(filepath , arcname=filepath.name)  #arcname is used to only select the name of the file or we can say the file only


if __name__== "__main__":                                   #to check it works properly , we use this code as main file
    make_archive(filepaths=["basic.py",], dest_dir="dest")
