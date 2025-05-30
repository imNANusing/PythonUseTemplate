import sys
import vtk
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QStandardPaths 
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor



# 创建一个VTK渲染窗口和渲染器
class VTKWidget_3D(QVTKRenderWindowInteractor):
    def __init__(self, parent=None):
        super(VTKWidget_3D, self).__init__(parent)
        self.Initialize()  # 初始化VTK渲染窗口
        # self.Start()  # 开始渲染循环

        self.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
        # 创建渲染器和渲染窗口
        self.renderer = vtk.vtkRenderer()
        self.GetRenderWindow().AddRenderer(self.renderer)

        self.current_actor = None
        

    def load_stl_file(self,file_path):
        if  self.current_actor:  # 删除旧模型（如果有）
            self.renderer.RemoveActor(self.current_actor)
            self.current_actor = None


        if file_path.lower().endswith(".stl"):
            reader = vtk.vtkSTLReader()
        else:
            print("不支持的文件格式")
        # 创建一个 STL 读取器
        reader.SetFileName(file_path)  # 替换为你的 STL 文件路径
        reader.Update()


        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(reader.GetOutputPort())

        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        self.renderer.AddActor(actor)

        self.current_actor = actor





class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("3D模型显示工具")
        # 设置窗口布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 添加VTK渲染窗口
        self.vtk_widget = VTKWidget_3D()
        layout.addWidget(self.vtk_widget)

        # 添加按钮
        self.load_button = QPushButton("加载 STL 文件")
        self.load_button.clicked.connect(self.load_stl_file)
        layout.addWidget(self.load_button)
    
    def load_stl_file(self):
        # 1. 弹出文件选择对话框
        desktop_path = QStandardPaths.writableLocation(QStandardPaths.DesktopLocation)
        file_path, _ = QFileDialog.getOpenFileName(self,"选择 3D 文件", desktop_path, "stl模型文件 (*.stl);;All Files (*)")
        if not file_path:
            return  # 用户取消选择
        self.vtk_widget.load_stl_file(file_path)




if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 创建主窗口
    window = MainWindow()
    window.show()
    # 运行PyQt应用程序
    sys.exit(app.exec_())