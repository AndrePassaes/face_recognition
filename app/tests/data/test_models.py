import os
import pytest

from app.data import models


class TestImage(object):

    def test_image(self):
        image = models.Image("path", "category", 1.0)
        assert image.path == "path"
        assert image.category == "category"
        assert image.score == 1.0

    def test_repr(self):
        image = models.Image("path", "category", 1.0)
        assert repr(image) == "Image('path', 'category', 1.0)"


class TestLoadImage(object):

    @pytest.mark.parametrize("path, category, score", [
        ("path", "category", 1.0),
        ("path2", "category2", 0.5),
    ])
    def test_load_image(self, path, category, score):
        image = models.load_image(path)
        assert image.path == path
        assert image.category == category
        assert image.score == score


class TestSaveImage(object):
    @pytest.fixture
    def image_data(self):
        return [
            ("path", "category", 1.0),
            ("path2", "category2", 0.5),
        ]

    @pytest.mark.parametrize("path, category, score", image_data())
    def test_save_image(self, path, category, score):
        try:
            if not isinstance(path, str):
                raise ValueError("Path must be a string")
            if not isinstance(category, str):
                raise ValueError("Category must be a string")
            if not isinstance(score, float):
                raise ValueError("Score must be a float")

            image = models.Image(path, category, score)
            models.save_image(image)

            if os.path.exists(path):
                loaded_image = models.load_image(path)
            else:
                loaded_image = None

            assert image == loaded_image
        except Exception as e:
            pytest.fail(f"An error occurred: {e}")

    def teardown_method(self):
        # Delete the test image after the test is completed
        models.delete_image(path)
