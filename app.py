from flask import Flask
from flask import redirect, render_template, flash

from figures import *
from forms import *
from figures_draw import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sdiefoief968wef238'


@app.route('/')
def index():
    return redirect('http://127.0.0.1:5000/square')


@app.route('/square', methods=['get', 'post'])
def square_view():
    form = SquareForm()

    if form.validate_on_submit():
        square = Square(form.side.data)
        area = square.area()
        square_draw(form.side.data)
        return render_template('square.html', form=form, area=area, title=Square.get_title())

    return render_template('square.html', form=form, title=Square.get_title())


@app.route('/rectangle', methods=['get', 'post'])
def rectangle_view():
    form = RectangleForm()

    if form.validate_on_submit():
        rectangle = Rectangle(form.length.data, form.width.data)
        area = rectangle.area()
        rectangle_draw(form.length.data, form.width.data)
        return render_template('rectangle.html', form=form, area=area, title=Rectangle.get_title())

    return render_template('rectangle.html', form=form, title=Rectangle.get_title())


@app.route('/triangle', methods=['get', 'post'])
def triangle_view():
    form = TriangleForm()

    if form.validate_on_submit():
        side_c = sqrt(form.side_a.data ** 2 + form.side_b.data ** 2 -
                      2 * form.side_a.data * form.side_b.data * cos(radians(form.angle.data)))
        print(side_c)
        if Triangle.check(form.side_a.data, form.side_b.data, side_c):
            triangle = Triangle(form.side_a.data, form.side_b.data, form.angle.data)
            area = triangle.area()
            triangle_draw(form.side_a.data, form.side_b.data, form.angle.data)
            return render_template('triangle.html', form=form, area=area, title=Triangle.get_title())
        else:
            flash('Площадь для треугольника по введенным данным не удалось найти. Проверьте введенные данные.')

    return render_template('triangle.html', form=form, title=Triangle.get_title())


@app.route('/trapezoid', methods=['get', 'post'])
def trapezoid_view():
    form = TrapezoidForm()

    if form.validate_on_submit():
        trapezoid = Trapezoid(form.upper_base.data, form.lower_base.data, form.height.data)
        area = trapezoid.area()
        trapezoid_draw(form.upper_base.data, form.lower_base.data, form.height.data)
        return render_template('trapezoid.html', form=form, area=area, title=Trapezoid.get_title())

    return render_template('trapezoid.html', form=form, title=Trapezoid.get_title())


@app.route('/rhomb', methods=['get', 'post'])
def rhomb_view():
    form = RhombForm()

    if form.validate_on_submit():
        rhomb = Rhomb(form.side.data, form.angle.data)
        area = rhomb.area()
        rhomb_draw(form.side.data, form.angle.data)
        return render_template('rhomb.html', form=form, area=area, title=Rhomb.get_title())

    return render_template('rhomb.html', form=form, title=Rhomb.get_title())


@app.route('/circle', methods=['get', 'post'])
def circle_view():
    form = CircleForm()

    if form.validate_on_submit():
        circle = Circle(form.radius.data)
        area = circle.area()
        return render_template('circle.html', form=form, area=area, title=Circle.get_title())

    return render_template('circle.html', form=form, title=Circle.get_title())


@app.route('/pyramid', methods=['get', 'post'])
def pyramid_view():
    form = PyramidForm()

    if form.validate_on_submit():
        pyramid = Pyramid(form.base_side.data, form.height.data)
        area = pyramid.area()
        volume = pyramid.volume()
        pyramid_draw(form.base_side.data, form.height.data)
        return render_template('pyramid.html', form=form, area=area, title=Pyramid.get_title(), volume=volume)

    return render_template('pyramid.html', form=form, title=Pyramid.get_title())


@app.route('/cube', methods=['get', 'post'])
def cube_view():
    form = CubeForm()

    if form.validate_on_submit():
        cube = Cube(form.side.data)
        area = cube.area()
        volume = cube.volume()
        cube_draw(form.side.data)
        return render_template('cube.html', form=form, area=area, title=Cube.get_title(), volume=volume)

    return render_template('cube.html', form=form, title=Cube.get_title())


@app.route('/sphere', methods=['get', 'post'])
def sphere_view():
    form = SphereForm()

    if form.validate_on_submit():
        sphere = Sphere(form.radius.data)
        area = sphere.area()
        volume = sphere.volume()
        sphere_draw(form.radius.data)
        return render_template('sphere.html', form=form, area=area, title=Sphere.get_title(), volume=volume)

    return render_template('sphere.html', form=form, title=Sphere.get_title())


@app.route('/parallelepiped', methods=['get', 'post'])
def parallelepiped_view():
    form = ParallelepipedForm()

    if form.validate_on_submit():
        parallelepiped = Parallelepiped(form.length.data, form.width.data, form.height.data)
        area = parallelepiped.area()
        volume = parallelepiped.volume()
        parallelepiped_draw(form.length.data, form.width.data, form.height.data)
        return render_template('parallelepiped.html', form=form, area=area, title=Parallelepiped.get_title(), volume=volume)

    return render_template('parallelepiped.html', form=form, title=Parallelepiped.get_title())


@app.route('/cylinder', methods=['get', 'post'])
def cylinder_view():
    form = CylinderForm()

    if form.validate_on_submit():
        cylinder = Cylinder(form.height.data, form.radius.data)
        area = cylinder.area()
        volume = cylinder.volume()
        cylinder_draw(form.height.data, form.radius.data)
        return render_template('cylinder.html', form=form, area=area, title=Cylinder.get_title(), volume=volume)

    return render_template('cylinder.html', form=form, title=Cylinder.get_title())


@app.route('/cone', methods=['get', 'post'])
def cone_view():
    form = ConeForm()

    if form.validate_on_submit():
        cone = Cone(form.height.data, form.radius.data)
        area = cone.area()
        volume = cone.volume()
        cone_draw(form.height.data, form.radius.data)
        return render_template('cone.html', form=form, area=area, title=Cone.get_title(), volume=volume)

    return render_template('cone.html', form=form, title=Cone.get_title())


if __name__ == '__main__':
    app.run(debug=True)
