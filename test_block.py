from control_block_diagram import ControllerDiagram
from control_block_diagram import Point, Box, Connection

if __name__ == '__main__':
    doc = ControllerDiagram()

    box_control = Box(Point(0, 0), text='Control')
    box_block = Box(box_control.position.add_x(10), text='Block')
    box_diagram = Box(box_block.position.add_x(3), text='Diagram')

    Connection.connect(box_control.output, box_block.input)
    Connection.connect(box_block.output, box_diagram.input)
    Connection.connect(box_diagram.output, box_control.input)

    doc.save('pdf')
    doc.show()