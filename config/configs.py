from abc import ABC, abstractmethod
from pydantic import BaseModel
import pandas as pd


class Config(BaseModel, ABC):
    @property
    @abstractmethod
    def data(self) -> pd.DataFrame:
        """Dữ liệu cần phân tích."""
        pass

    @property
    @abstractmethod
    def statistic(self) -> dict:
        """Trả về các đại lượng thống kê như mean, median, mode, min, max, variance, stdev, quartiles."""
        pass

    @property
    @abstractmethod
    def histogram(self):
        """Vẽ biểu đồ histogram cho dữ liệu số."""
        pass

    @property
    @abstractmethod
    def box_and_whiskers(self):
        """Vẽ biểu đồ box-and-whisker cho dữ liệu số."""
        pass

    @property
    @abstractmethod
    def bar(self):
        """Vẽ biểu đồ thanh cho dữ liệu phi số."""
        pass

    @property
    @abstractmethod
    def doughnut(self):
        """Vẽ biểu đồ doughnut cho dữ liệu phi số."""
        pass

    @property
    @abstractmethod
    def scatter(self):
        """Vẽ biểu đồ scatter để phân tích mối quan hệ giữa hai biến số."""
        pass

    @property
    @abstractmethod
    def confusion_matrix(self):
        """Tạo ma trận nhầm lẫn để đánh giá độ chính xác của mô hình."""
        pass

    @property
    @abstractmethod
    def frequency_table(self) -> pd.DataFrame:
        """Tạo bảng tần suất cho dữ liệu phi số."""
        pass

    @property
    @abstractmethod
    def summary_table(self) -> pd.DataFrame:
        """Tạo bảng thống kê tổng hợp cho tất cả các cột."""
        pass

    @abstractmethod
    def show(self):
        """Hiển thị tất cả các phân tích theo yêu cầu."""
        pass
