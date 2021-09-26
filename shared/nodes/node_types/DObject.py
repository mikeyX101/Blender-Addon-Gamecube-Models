from .. import Node

# DObject
class DObject(Node):
    class_name = "D Object"
    length = 16
    fields = [
        ('name', 'string'),
        ('next', 'DObject'),
        ('mobject', 'MObject'),
        ('pobject', 'PObject')
    ]

    # Parse struct from binary file.
    @classmethod
    def fromBinary(cls, parser, address):
        return parser.parseStruct(cls, address)

    # Tells the builder how to write this node's data to the binary file.
    # Returns the offset the builder was at before it started writing its own data.
    def writeBinary(self, builder):
        return builder.writeStruct(self)

    # Make approximation HSD struct from blender data.
    @classmethod
    def fromBlender(cls, blender_obj):
        pass

    # Make approximation Blender object from HSD data.
    def toBlender(self, context):
        pass