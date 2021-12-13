import fiftyone as fo


# The directory containing the source images
data_path = "./images"

# The path to the COCO labels JSON file
labels_path = "./annotations/annotations.json"

# Import the dataset
dataset = fo.Dataset.from_dir(
    dataset_type=fo.types.COCODetectionDataset,
    data_path=data_path,
    labels_path=labels_path,
)