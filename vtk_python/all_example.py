import sys
import vtk
from PyQt5.QtWidgets import *
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

from all_vtk_api import *

# 创建一个VTK渲染窗口和渲染器
class VTKWidget(QVTKRenderWindowInteractor):
    def __init__(self, parent=None):
        super(VTKWidget, self).__init__(parent)
        self.Initialize()  # 初始化VTK渲染窗口
        # self.Start()  # 开始渲染循环

        # 创建渲染器和渲染窗口
        self.renderer = vtk.vtkRenderer()
        self.GetRenderWindow().AddRenderer(self.renderer)
        sphere_actor = add_triangle()

        # sphere_actor.GetProerty().SetColor([0,0,1])
        # sphere_actor.GetProperty().SetColor(0, 0, 1) #两种方式均可
        sphere_actor.GetProperty().SetDiffuse(0.5)
        sphere_actor.GetProperty().SetAmbient(0)
        sphere_actor.GetProperty().SetSpecular(0)
        sphere_actor.GetProperty().SetSpecularPower(1)
        sphere_actor.GetProperty().SetDiffuse(1)
        # sphere_actor.GetProperty().SetDiffuseColor(1,0,0)
        # sphere_actor.GetProperty().SetSpecularColor(0, 1, 0)


        # self.renderer.SetActiveCamera(self.camera)


        # # 添加光源
        # self.light = vtk.vtkLight()
        # self.light.SetColor(0, 1, 0)  # 设置光源颜色
        # self.light.SetPosition(0, 0, 10)  # 设置光源位置 x 右，y上 z前
        # self.light.SetFocalPoint(self.renderer.GetActiveCamera().GetFocalPoint())  # 设置焦点
        # self.renderer.AddLight(self.light)

        # 将圆球添加到渲染器中
        self.renderer.AddActor(sphere_actor)
        self.renderer.ResetCamera() #这个会根据渲染器里面的物体动态调整,重置基础信息，不会重置角度


        self.GetRenderWindow().GetInteractor().SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera()) # 默认是 vtk.vtkInteractorStyleSwitch()
        # self.GetRenderWindow().SetSize(10,10)  #设置vtk独立窗口的大小，如果嵌入到qt中则没有效果

    # PyQt的主窗口类
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # 设置窗口布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 添加VTK渲染窗口
        self.vtk_widget = VTKWidget()
        layout.addWidget(self.vtk_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 创建主窗口
    window = MainWindow()
    window.show()
    # 运行PyQt应用程序
    sys.exit(app.exec_())