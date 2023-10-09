import pytest

from app.presentation import views


class TestIndexView(object):
    def test_index_view(self):
        response = views.index()
        assert response.status_code == 200
        assert response.template_name == "index.html"


class TestPredictView(object):

    @pytest.mark.parametrize("path", [
        "path",
        "path2",
    ])
    def test_predict_view(self, path):
        with mock.patch("flask.request.files") as mock_files:
            mock_files.getlist("image").return_value = [
                ("image", open(path, "rb"))
            ]
            response = views.predict()
            assert response.status_code == 200
            assert response.template_name == "prediction.html"
            assert response.context["category"] == "category"
