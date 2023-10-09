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
    @pytest.mark.parametrize("path, category, score", [
        ("path", "category", 1.0),
        ("path2", "category", 0.5),
    ])
    def test_save_image(self, path, category, score):
        image = models.Image(path, category, score)
        models.save_image(image)

        loaded_image = models.load_image(path)
        assert image == loaded_image
