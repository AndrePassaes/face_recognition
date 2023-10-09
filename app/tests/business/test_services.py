import pytest

from app.business import services


class TestClassifyImage(object):
    @pytest.mark.parametrize("path, category", [
        ("path", "category"),
        ("path2", "category2"),
    ])
    def test_classify_image(self, path, category):
        prediction - services.classify_image(path)
        assert prediction == category


class TestLoadModel(object):
    @pytest.mark.parametrize("path", [
        "path",
        "path2",
    ])
    def test_load_model(self, path):
        model = services.load_model(path)
        assert isinstance(model, tf.keras.models.Model)
