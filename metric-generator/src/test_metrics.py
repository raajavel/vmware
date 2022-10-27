import pytest
import metrics

class TestClassMetrics:
    def test_generate_metrics(self):
        assert None == metrics.generate_metrics()

    def test_generate_metrics_return(self):
        assert True == metrics.generate_metrics()
    