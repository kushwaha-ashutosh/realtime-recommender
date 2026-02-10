import os


def test_feature_db_exists():
    # pipeline must have been run once
    assert os.path.exists("features.db")
