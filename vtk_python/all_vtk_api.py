



import vtk



# 添加球体
def add_sphere( center: set = (0, 0, 0), radius: float = 5.0, set_phi_resolution: int = 10,
               set_theta_resolution: int = 10) -> vtk.vtkActor:
    sphere_source = vtk.vtkSphereSource()
    sphere_source.SetCenter(center)
    sphere_source.SetRadius(radius)
    sphere_source.SetPhiResolution(set_phi_resolution)
    sphere_source.SetThetaResolution(set_theta_resolution)
    sphere_source.Update()
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(sphere_source.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    return actor

# 添加圆柱体
def add_cylinder( height: float = 3.0, radius: float = 1.0, resolution: int = 20, center:set = (0,0,0)) -> vtk.vtkActor:
    cylinder = vtk.vtkCylinderSource()
    cylinder.SetHeight(height)
    cylinder.SetRadius(radius)
    cylinder.SetResolution(resolution)
    cylinder.SetCenter(center)
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(cylinder.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    return actor


def add_cone( radius: float = 5,
             height: float = 10,
             center: set = (0, 0, 0),
             resolution: int = 100, direction: set = (0, 0, 1)) -> vtk.vtkActor:
    cone = vtk.vtkConeSource()
    cone.SetRadius(radius)
    cone.SetHeight(height)
    cone.SetCenter(center)
    cone.SetDirection(direction)
    cone.SetResolution(resolution)
    cone_mapper = vtk.vtkPolyDataMapper()
    cone_mapper.SetInputConnection(cone.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(cone_mapper)
    return actor


def add_cube(bounds: set = (-1, 1, -1, 1, -1, 1)) -> vtk.vtkActor:
    cube = vtk.vtkCubeSource()
    cube.SetBounds(bounds) # bounds = (-1, 1, -1, 1, -1, 1) 创建一个中心在原点、边长为 2 的立方体。
    cube_mapper = vtk.vtkPolyDataMapper()
    cube_mapper.SetInputConnection(cube.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(cube_mapper)
    return actor


def add_square(
        origin: set = (0, 0, 0),
        point1: set = (1, 0, 0),
        point2: set = (0, 1, 0),) -> vtk.vtkActor:
    square = vtk.vtkPlaneSource()
    square.SetOrigin(origin)
    square.SetPoint1(point1)
    square.SetPoint2(point2)

    square_mapper = vtk.vtkPolyDataMapper()
    square_mapper.SetInputConnection(square.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(square_mapper)
    return actor

def add_triangle(
    points: list[set[float, float, float]] = [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (0.5, 1.0, 0.0)]) -> vtk.vtkActor:
    triangle = vtk.vtkTriangle()
    triangle.GetPointIds().SetId(0, 0)
    triangle.GetPointIds().SetId(1, 1)
    triangle.GetPointIds().SetId(2, 2)
    points_array = vtk.vtkPoints()
    for point in points:
        points_array.InsertNextPoint(point)

    triangles = vtk.vtkCellArray()
    triangles.InsertNextCell(triangle)

    triangle_polydata = vtk.vtkPolyData()
    triangle_polydata.SetPoints(points_array)
    triangle_polydata.SetPolys(triangles)

    triangle_mapper = vtk.vtkPolyDataMapper()
    triangle_mapper.SetInputData(triangle_polydata)
    actor = vtk.vtkActor()
    actor.SetMapper(triangle_mapper)
    return actor

# 添加点群
def add_points( center: set = (0, 0, 0), radius: float = 10.0,
               number_of_point: int = 1000) -> vtk.vtkActor:
    point_source = vtk.vtkPointSource()
    point_source.SetNumberOfPoints(number_of_point)  # 设置点的数量
    point_source.SetRadius(radius)
    point_source.SetCenter(center)
    point_source.Update()
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(point_source.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    return actor

def add_circle(
        radius: float = 5, center: set = (0, 0, 0), resolution: int = 100, normal:set = (0, 0, 1)
) -> vtk.vtkActor:
    circle = vtk.vtkRegularPolygonSource()
    circle.SetNumberOfSides(resolution)
    circle.SetRadius(radius)
    circle.SetCenter(center)
    circle.SetNormal(normal)

    circle_mapper = vtk.vtkPolyDataMapper()
    circle_mapper.SetInputConnection(circle.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(circle_mapper)
    return actor


def add_box( source) -> vtk.vtkActor:
    box_filter = vtk.vtkOutlineFilter()
    box_filter.SetInputConnection(source.GetOutputPort())
    box_filter.Update()
    # 获取数据集的边界
    bounds = box_filter.GetOutput().GetBounds()
    # 计算长宽高
    x_size = bounds[1] - bounds[0]
    y_size = bounds[3] - bounds[2]
    z_size = bounds[5] - bounds[4]
    print(f"Size: {x_size}, {y_size}, {z_size}")
    box_mapper = vtk.vtkPolyDataMapper()
    box_mapper.SetInputConnection(box_filter.GetOutputPort())
    box_actor = vtk.vtkActor()
    box_actor.SetMapper(box_mapper)
    box_actor.GetProperty().SetColor(255, 255, 255)
    return box_actor

def add_camera() -> vtk.vtkCamera:
    camera = vtk.vtkCamera()
    camera.SetClippingRange(0.01, 1000.01) # 设置前后裁剪面 默认(0.01, 1000.01)，
    camera.SetPosition(0.0, 0.0, 100.0) # 默认(0.0, 0.0, 1.0)
    camera.SetViewUp(0.0, 1.0, 0.0) # 默认 (0.0, 1.0, 0.0)  可以理解为一个向量，这个向量正指向上方。
    camera.SetFocalPoint(0.0, 0.0, 0.0) # 默认(0.0, 0.0, 0.0)

    camera.Azimuth(60) # 以焦点为中心，围绕朝上方向方向向量，即在焦点为中心，焦距为半径的圆球的维度线上水平旋转；
    camera.Elevation(60) #以焦点为中心，在焦点为中心，焦距为半径的圆球的经度线方向上旋转垂直旋转；
    camera.Roll(30) #绕着相机的视线方向旋转（类似相机自身的旋转），调整相机“上方向”的角度。旋转的轴是沿相机方向的轴线。 围绕投影方向旋转相机

    camera.Yaw(30) #同Azimuth相似，以相机为中心，移动焦点坐标；
    camera.Pitch(30) # 同Elevation相似，以相机为中心，移动焦点坐标；

    camera.Dolly(0.5) #相机向后撤
    camera.Zoom(0.5) #图像放大缩小
    return camera
