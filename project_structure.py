import os


def create_project_structure(root_dir):
    # Define directory structure
    dirs = [
        'data/external',
        'data/interim',
        'data/processed',
        'data/raw',
        'models',
        'notebooks',
        'references',
        'reports/figures',
        'src/data',
        'src/features',
        'src/models',
        'src/visualization'
    ]

    # Create directories
    for d in dirs:
        os.makedirs(os.path.join(root_dir, d), exist_ok=True)

    # Create files
    files = [
        'README.md',
        'requirements.txt',
        'setup.py',
        'src/__init__.py',
        'src/data/__init__.py',
        'src/features/__init__.py',
        'src/models/__init__.py',
        'src/visualization/__init__.py',
        'src/data/make_dataset.py',
        'src/features/build_features.py',
        'src/models/train_model.py',
        'src/models/predict_model.py',
        'src/visualization/visualize.py'
    ]

    for f in files:
        open(os.path.join(root_dir, f), 'a').close()


# Call the function to create the project structure in the current directory
create_project_structure('.')
